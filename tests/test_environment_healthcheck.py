import platform
import sys


def test_python_version():
    assert sys.version_info.major >= 3


def test_os_information():
    assert platform.system() in ["Linux", "Windows", "Darwin"]
