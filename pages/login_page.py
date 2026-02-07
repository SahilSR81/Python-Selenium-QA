from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MSG = (By.CSS_SELECTOR, "h3[data-test='error']")

    # Perform login action
    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    # Get error message text on invalid login
    def get_error_message(self):
        return self.get_text(self.ERROR_MSG)

    # -------------------- NEW ADDITION (DAY 22) --------------------

    # Check if login button is still enabled after failure
    def is_login_button_enabled(self):
        return self.driver.find_element(*self.LOGIN_BTN).is_enabled()
