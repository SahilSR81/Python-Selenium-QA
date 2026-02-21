class SoftAssert:
    def __init__(self):
        self.errors = []

    def assert_true(self, condition, message):
        if not condition:
            self.errors.append(message)

    def assert_equal(self, actual, expected, message):
        if actual != expected:
            self.errors.append(f"{message} | Expected: {expected}, Got: {actual}")

    def assert_all(self):
        if self.errors:
            raise AssertionError("\n".join(self.errors))
