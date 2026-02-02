import pytest

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 5),
        (10, 5, 15),
        (-1, 1, 0),
        (0, 0, 0),
    ]
)
def test_addition(a, b, expected):
    assert a + b == expected


if __name__ == "__main__":
    print("Day 17 calculator parametrize tests executed.")

