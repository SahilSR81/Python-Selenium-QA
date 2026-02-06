from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):

    TITLE = (By.CLASS_NAME, "title")
    MENU_BTN = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def get_page_title(self):
        return self.get_text(self.TITLE)

    def logout(self):
        self.click(self.MENU_BTN)
        self.click(self.LOGOUT_LINK)
