from utils.wait_utils import wait_visible


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def click(self, locator):
        wait_visible(self.driver, locator).click()

    def type(self, locator, text):
        element = wait_visible(self.driver, locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return wait_visible(self.driver, locator).text
