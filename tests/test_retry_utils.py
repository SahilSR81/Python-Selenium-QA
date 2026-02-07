import pytest
from utils.retry_utils import retry


def test_retry_success_first_attempt():
    """Retry should return immediately if action succeeds"""

    def action():
        return "OK"

    result = retry(action, retries=3)
    assert result == "OK"


def test_retry_success_after_failure():
    """Retry should succeed if action fails initially but succeeds later"""
    attempts = {"count": 0}

    def action():
        attempts["count"] += 1
        if attempts["count"] < 2:
            raise Exception("Temporary failure")
        return "SUCCESS"

    result = retry(action, retries=3)
    assert result == "SUCCESS"
    assert attempts["count"] == 2


def test_retry_failure_after_all_attempts():
    """Retry should raise exception if all attempts fail"""

    def action():
        raise Exception("Always fails")

    with pytest.raises(Exception):
        retry(action, retries=2)
