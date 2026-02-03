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
