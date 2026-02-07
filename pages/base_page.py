from utils.wait_utils import wait_visible
from utils.retry_utils import retry  # NEW import


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # Open any URL
    def open(self, url):
        self.driver.get(url)

    # Click element after waiting for visibility
    def click(self, locator):
        wait_visible(self.driver, locator).click()

    # Type text safely into input field
    def type(self, locator, text):
        element = wait_visible(self.driver, locator)
        element.clear()
        element.send_keys(text)

    # Get visible text from element
    def get_text(self, locator):
        return wait_visible(self.driver, locator).text

    # Get current page title
    def get_title(self):
        return self.driver.title

    # -------------------- NEW ADDITIONS (DAY 22) --------------------

    # Safe click with retry to reduce flaky failures
    def safe_click(self, locator):
        return retry(lambda: self.click(locator))

    # Check if element is visible on page (returns True/False)
    def is_visible(self, locator):
        try:
            wait_visible(self.driver, locator)
            return True
        except:
            return False

    # Validate navigation by checking URL content
    def wait_for_url(self, text):
        assert text in self.driver.current_url
