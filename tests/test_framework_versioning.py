import sys


def test_python_version():
    assert sys.version_info.major == 3


def test_framework_core_imports():

    import utils.driver_factory
    import utils.execution_metrics
    import utils.retry_utils
    import utils.tag_manager

    assert True
