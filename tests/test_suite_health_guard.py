import pytest


@pytest.mark.regression
def test_suite_has_minimum_tests(request):
    session = request.session
    collected = session.testscollected
    assert collected >= 1
