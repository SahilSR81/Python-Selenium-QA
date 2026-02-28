import pytest
def pytest_runtest_logreport(report):
    if report.when == "call" and report.failed:
        config = report.session.config

        if config.getoption("--fail-fast"):
            pytest.exit("Fail-fast activated.", returncode=1)

        max_failures = config.getoption("--max-failures")
        if max_failures:
            try:
                max_failures = int(max_failures)
                if report.session.testsfailed >= max_failures:
                    pytest.exit(
                        f"Max failure limit {max_failures} reached.", returncode=1
                    )
            except ValueError:
                pass
