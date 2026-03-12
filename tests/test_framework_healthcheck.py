import os
import utils.driver_factory
import utils.execution_metrics
import utils.retry_utils


def test_framework_core_modules():
    assert utils.driver_factory is not None
    assert utils.execution_metrics is not None
    assert utils.retry_utils is not None


def test_project_structure():
    assert os.path.exists("pages")
    assert os.path.exists("utils")
    assert os.path.exists("tests")


def test_reports_folder_exists():
    assert os.path.isdir("reports")


def test_logs_folder_exists():
    assert os.path.isdir("logs")
