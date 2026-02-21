import random
from utils.retry_utils import retry


def unstable_operation():
    if random.randint(0, 1) == 0:
        raise Exception("Random failure")
    return True


def test_retry_wrapper():
    result = retry(unstable_operation, retries=2, delay=1)
    assert result is True

