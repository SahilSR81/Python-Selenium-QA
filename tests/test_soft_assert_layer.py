from utils.soft_assert_utils import SoftAssert


def test_soft_assert_validation(driver):
    sa = SoftAssert()

    sa.assert_true(driver.title != "", "Title should not be empty")
    sa.assert_equal(2 + 2, 4, "Math validation failed")

    sa.assert_all()
