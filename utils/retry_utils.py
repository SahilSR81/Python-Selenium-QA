import time


def retry(action, retries=3, delay=1):
    last_exception = None

    for _ in range(retries):
        try:
            return action()
        except Exception as e:
            last_exception = e
            time.sleep(delay)

    # If all retries failed, raise the last captured exception
    if last_exception:
        raise last_exception
    else:
        raise Exception("Retry failed without capturing an exception")
