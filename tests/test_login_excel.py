import pytest
from utils.driver_factory import get_driver

# 🔹 TEMP DATA (Excel ka replacement)
TEST_DATA = [
    ("tomsmith", "SuperSecretPassword!", "You logged into a secure area"),
    ("wrong", "SuperSecretPassword!", "Your username is invalid"),
    ("tomsmith", "wrongpass", "Your password is invalid"),
]

# ============================================================
# FUTURE EXCEL INTEGRATION (DO NOT DELETE)
# ------------------------------------------------------------
# To enable Excel-based testing:
#
# 1. Create file:
#    testdata/login_data.xlsx
#
# 2. Sheet name: Sheet1
#
# 3. Columns:
#    | username | password | expected |
#
# 4. Uncomment below lines and remove TEST_DATA above
#
# from utils.excel_utils import get_test_data
# TEST_DATA = get_test_data("testdata/login_data.xlsx", "Sheet1")
#
# ============================================================

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    driver = get_driver(request.param)
    driver.get("https://the-internet.herokuapp.com/login")
    yield driver
    driver.quit()


@pytest.mark.parametrize("username,password,expected", TEST_DATA)
def test_login_multi_browser(driver, username, password, expected):
    driver.find_element("id", "username").send_keys(username)
    driver.find_element("id", "password").send_keys(password)
    driver.find_element("css selector", "button.radius").click()

    message = driver.find_element("id", "flash").text
    assert expected in message
