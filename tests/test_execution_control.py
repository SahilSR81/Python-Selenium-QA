import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_combined_marker(driver):
    assert driver.title != ""
