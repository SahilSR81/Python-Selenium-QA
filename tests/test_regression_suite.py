import pytest
from selenium.webdriver.common.by import By


@pytest.mark.regression
def test_page_source_not_empty(driver):
    assert len(driver.page_source) > 100


@pytest.mark.regression
def test_find_body_tag(driver):
    body = driver.find_element(By.TAG_NAME, "body")
    assert body is not None
