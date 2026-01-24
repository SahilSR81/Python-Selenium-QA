# Protected member example

class BaseTest:
    def __init__(self):
        self._browser = "Chrome"   # protected variable


class LoginTest(BaseTest):
    def show_browser(self):
        print(self._browser)


test = LoginTest()
test.show_browser()

# Output:
# Chrome

