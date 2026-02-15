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


# ---------------- DRIVER FIXTURE ----------------
@pytest.fixture(params=["chrome", "firefox", "edge"])
def driver(request):
    app_name = request.config.getoption("--app")

    if app_name not in APP_URLS:
        raise ValueError(f"Invalid app name: {app_name}")

    driver = get_driver(request.param)
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


# ---------------- MARKER REGISTRATION ----------------
def pytest_configure(config):
    config.addinivalue_line("markers", "smoke: Smoke tests")
    config.addinivalue_line("markers", "regression: Regression tests")
    config.addinivalue_line("markers", "sanity: Sanity tests")
