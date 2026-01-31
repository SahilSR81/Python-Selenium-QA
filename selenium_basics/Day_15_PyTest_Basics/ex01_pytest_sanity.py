def test_pytest_is_working():
    assert 1 == 1


if __name__ == "__main__":
    try:
        test_pytest_is_working()
        print("ex01_pytest_sanity.py → ALL TESTS PASSED")
    except AssertionError:
        print("ex01_pytest_sanity.py → TEST FAILED")

