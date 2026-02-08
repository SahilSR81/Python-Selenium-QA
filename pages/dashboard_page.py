from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DashboardPage(BasePage):

    PAGE_TITLE = (By.CLASS_NAME, "title")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def is_dashboard_loaded(self):
        return self.get_text(self.PAGE_TITLE) == "Products"

    def open_menu(self):
        self.click(self.MENU_BUTTON)

    def logout(self):
        self.open_menu()
        self.click(self.LOGOUT_LINK)
