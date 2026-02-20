from utils.assertion_utils import assert_true, assert_equal


def test_custom_assertions(driver):
    assert_true(driver.title != "")
    assert_equal(1, 1)
