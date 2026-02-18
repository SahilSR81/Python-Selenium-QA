# ============================================================
# Reporting Plugin (Day 32 Add-on)
# This file extends pytest with HTML report customization
# without modifying existing conftest.py
# ============================================================


def pytest_configure(config):
    # Preserve existing metadata if present
    if hasattr(config, "_metadata"):
        config._metadata["Project"] = "Python Selenium QA Framework"
        config._metadata["Execution Mode"] = "Parallel Supported"
        config._metadata["Browser Param"] = "Multi-browser"
        config._metadata["Tester"] = "Sahil Singh"


def pytest_html_report_title(report):
    report.title = "Automation Execution Report"
