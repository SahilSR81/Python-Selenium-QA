import pytest
from utils.driver_factory import get_driver


@pytest.fixture(params=["chrome", "firefox"], scope="function")
def driver(request):
    driver = get_driver(request.param)
    yield driver
    driver.quit()

