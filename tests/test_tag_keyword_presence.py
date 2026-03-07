import pytest


@pytest.mark.smoke
def test_smoke_marker():
    assert True


@pytest.mark.regression
def test_regression_marker():
    assert True


@pytest.mark.sanity
def test_sanity_marker():
    assert True
