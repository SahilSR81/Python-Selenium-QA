import sys
import os
import pytest

# ---------------- PATH SETUP ----------------
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

# ---------------- IMPORTS ----------------
from utils.driver_factory import get_driver
from utils.screenshot_utils import capture_screenshot

# ---------------- APP URL CONFIG ----------------
APP_URLS = {
    "saucedemo": "https://www.saucedemo.com/",
    "orangehrm": "https://opensource-demo.orangehrmlive.com/",
    "the_internet": "https://the-internet.herokuapp.com/",
}


# ---------------- CLI OPTION ----------------
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


# ---------------- PYTEST HOOK ----------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


# ---------------- SCREENSHOT ON FAILURE ----------------
@pytest.fixture(autouse=True)
def screenshot_on_failure(request, driver):
    yield
    if request.node.rep_call.failed:
        capture_screenshot(driver, request.node.name)


# ---------------- MARKER REGISTRATION + REPORT METADATA ----------------
def pytest_configure(config):
    # Register markers
    config.addinivalue_line("markers", "smoke: Smoke tests")
    config.addinivalue_line("markers", "regression: Regression tests")
    config.addinivalue_line("markers", "sanity: Sanity tests")

    # Add metadata for pytest-html (if plugin active)
    if hasattr(config, "_metadata"):
        config._metadata["Project"] = "Python Selenium QA Framework"
        config._metadata["Execution Mode"] = "Parallel Supported"
        config._metadata["Browser Param"] = "Multi-browser"
        config._metadata["Tester"] = "Sahil Singh"


# ---------------- HTML REPORT TITLE ----------------
def pytest_html_report_title(report):
    report.title = "Automation Execution Report"


# ============================================================
# ---------------- PARALLEL EXECUTION INFO ----------------
# Prints worker id when running with pytest-xdist
# ============================================================
@pytest.fixture(autouse=True)
def print_worker_info(request):
    worker_id = (
        request.config.workerinput["workerid"]
        if hasattr(request.config, "workerinput")
        else "master"
    )
    print(f"\n[Running on worker: {worker_id}]")

# ============================================================
# ENVIRONMENT PROFILE FIXTURE
# ============================================================

@pytest.fixture(scope="session")
def env_config(request):
    from utils.env_loader import load_environment

    env_name = request.config.getoption("--env")
    return load_environment(env_name)
