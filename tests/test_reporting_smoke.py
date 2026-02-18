import pytest


@pytest.mark.smoke
def test_report_title_validation(driver):
    assert driver.title != ""
