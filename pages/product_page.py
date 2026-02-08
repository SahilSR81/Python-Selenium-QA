from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):

    FIRST_ADD_TO_CART = (By.CSS_SELECTOR, ".btn_inventory")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def add_first_product_to_cart(self):
        self.click(self.FIRST_ADD_TO_CART)

    def is_product_added_to_cart(self):
        return self.is_visible(self.CART_BADGE)
