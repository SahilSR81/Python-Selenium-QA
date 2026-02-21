import pytest


@pytest.mark.smoke
def test_marker_smoke(driver):
    assert driver.title != ""


@pytest.mark.regression
def test_marker_regression(driver):
    assert driver.current_url.startswith("http")
