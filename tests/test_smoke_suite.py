import pytest


@pytest.mark.smoke
def test_homepage_title(driver):
    assert "Swag Labs" in driver.title or "The Internet" in driver.title


@pytest.mark.smoke
def test_current_url(driver):
    assert driver.current_url.startswith("http")
