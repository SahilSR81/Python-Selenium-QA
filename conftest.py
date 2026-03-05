import sys
import os
import pytest
import time

# ---------------- PATH SETUP ----------------
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

# ---------------- IMPORTS ----------------
from utils.driver_factory import get_driver
from utils.screenshot_utils import capture_screenshot
from utils.execution_metrics import ExecutionMetrics
from utils.data_provider import load_login_data
from utils.flaky_tracker import FlakyTracker
from utils.data_provider import load_dataset, validate_dataset_structure
from utils.config_manager import ConfigManager

# ---------------- GLOBAL METRICS OBJECT ----------------
metrics = ExecutionMetrics()
flaky_tracker = FlakyTracker()

# ---------------- APP URL CONFIG ----------------
APP_URLS = {
    "saucedemo": "https://www.saucedemo.com/",
    "orangehrm": "https://opensource-demo.orangehrmlive.com/",
    "the_internet": "https://the-internet.herokuapp.com/",
}


# ---------------- CLI OPTIONS ----------------
def pytest_addoption(parser):
    parser.addoption(
        "--app", action="store", default="saucedemo", help="Application under test"
    )

    parser.addoption(
        "--env", action="store", default="qa", help="Environment profile (dev/qa/prod)"
    )

    parser.addoption(
        "--headless", action="store_true", help="Run browser in headless mode"
    )

    parser.addoption(
        "--fail-fast", action="store_true", help="Stop execution on first failure"
    )

    parser.addoption(
        "--max-failures",
        action="store",
        default=None,
        help="Stop execution after N failures",
    )

    parser.addoption(
        "--ci-mode",
        action="store_true",
        help="Enable strict CI validation mode",
    )


# ---------------- DRIVER FIXTURE ----------------
@pytest.fixture(params=["chrome", "firefox", "edge"])
def driver(request):
    app_name = request.config.getoption("--app")

    if app_name not in APP_URLS:
        raise ValueError(f"Invalid app name: {app_name}")

    headless = request.config.getoption("--headless")
    driver = get_driver(request.param, headless=headless)

    driver.get(APP_URLS[app_name])

    yield driver
    driver.quit()


# ---------------- TEST DURATION TRACKER ----------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call(item):
    start = time.time()
    yield
    duration = time.time() - start
    metrics.record_test(item.name, duration)


# ---------------- PYTEST REPORT HOOK ----------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.hookimpl
def pytest_runtest_logreport(report):
    if report.when == "call" and report.failed:
        flaky_tracker.record_retry(report.nodeid)


# ---------------- SCREENSHOT ON FAILURE ----------------
@pytest.fixture(autouse=True)
def screenshot_on_failure(request, driver):
    yield
    if request.node.rep_call.failed:
        capture_screenshot(driver, request.node.name)


# ---------------- MARKER REGISTRATION + REPORT METADATA ----------------
def pytest_configure(config):
    config.addinivalue_line("markers", "smoke: Smoke tests")
    config.addinivalue_line("markers", "regression: Regression tests")
    config.addinivalue_line("markers", "sanity: Sanity tests")

    if hasattr(config, "_metadata"):
        config._metadata["Project"] = "Python Selenium QA Framework"
        config._metadata["Execution Mode"] = "Parallel Supported"
        config._metadata["Browser Param"] = "Multi-browser"
        config._metadata["Tester"] = "Sahil Singh"


# ---------------- HTML REPORT TITLE ----------------
def pytest_html_report_title(report):
    report.title = "Automation Execution Report"


# ---------------- PARALLEL EXECUTION INFO ----------------
@pytest.fixture(autouse=True)
def print_worker_info(request):
    worker_id = (
        request.config.workerinput["workerid"]
        if hasattr(request.config, "workerinput")
        else "master"
    )
    print(f"\n[Running on worker: {worker_id}]")


# ---------------- ENVIRONMENT PROFILE FIXTURE ----------------
@pytest.fixture(scope="session")
def env_config(request):
    from utils.env_loader import load_environment

    env_name = request.config.getoption("--env")
    return load_environment(env_name)


# ---------------- DATA PROVIDER FIXTURES ----------------
@pytest.fixture(scope="session")
def valid_login_data():
    return load_login_data("valid")


@pytest.fixture(scope="session")
def invalid_login_data():
    return load_login_data("invalid")


@pytest.fixture(scope="session")
def login_dataset():
    dataset = load_dataset("test_login_dataset")
    validate_dataset_structure(dataset)
    return dataset


# ---------------- SESSION FINISH (EXECUTION CONTROL + METRICS) ----------------
def pytest_sessionfinish(session, exitstatus):
    config = session.config

    # ----- Fail Fast -----
    if config.getoption("--fail-fast") and session.testsfailed > 0:
        session.shouldstop = "Fail-fast activated."

    # ----- Max Failures -----
    max_failures = config.getoption("--max-failures")
    if max_failures:
        try:
            max_failures = int(max_failures)
            if session.testsfailed >= max_failures:
                session.shouldstop = f"Max failure limit {max_failures} reached."
        except ValueError:
            pass

        # ----- Execution Metrics -----
    env = config.getoption("--env")
    browser_mode = "headless" if config.getoption("--headless") else "headed"

    summary = metrics.generate_summary(env, browser_mode)
    path = metrics.export_summary(summary)

    print("\n==== EXECUTION SUMMARY ====")
    print(summary)
    print(f"\nReport saved at: {path}")

    # ----- CI Mode Strict Validation -----
    if config.getoption("--ci-mode"):
        if session.testscollected == 0:
            raise RuntimeError("CI Mode: No tests were collected.")

        if session.testsfailed > 0:
            raise RuntimeError("CI Mode: Test failures detected.")

    # ----- Flaky Test Summary -----
    flaky_tests = flaky_tracker.get_flaky_tests()
    summary["flaky_tests"] = flaky_tests

# ---------------- CONFIG MANAGER FIXTURE ----------------

@pytest.fixture(scope="session")
def config_manager():
    manager = ConfigManager()
    config = manager.load_config("qa")
    manager.validate_config(config)
    return config
