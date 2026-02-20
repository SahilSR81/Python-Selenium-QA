def assert_true(condition, message="Condition failed"):
    assert condition, message


def assert_equal(actual, expected, message="Values are not equal"):
    assert actual == expected, f"{message} | Expected: {expected}, Got: {actual}"


def assert_in(member, container, message="Value not found"):
    assert member in container, f"{message} | '{member}' not in container"
