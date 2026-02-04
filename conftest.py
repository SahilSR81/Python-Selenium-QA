import sys
import os


ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

import pytest
from utils.driver_factory import get_driver


@pytest.fixture(params=["chrome", "firefox","edge"])
def driver(request):
    driver = get_driver(request.param)
    yield driver
    driver.quit()


from utils.screenshot_utils import capture_screenshot


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(autouse=True)
def screenshot_on_failure(request, driver):
    yield
    if request.node.rep_call.failed:
        capture_screenshot(driver, request.node.name)
