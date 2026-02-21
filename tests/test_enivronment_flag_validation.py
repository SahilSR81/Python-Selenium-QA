import os


def test_environment_variable_presence():
    os.environ["TEST_ENV"] = "QA"
    assert os.getenv("TEST_ENV") == "QA"
