import os
import json


class FailureRootAnalyzer:

    def __init__(self):
        self.failures = []

    def record_failure(self, test_name, error_message):

        entry = {"test_name": test_name, "error": error_message}

        self.failures.append(entry)

    def generate_report(self):

        report = {"total_failures": len(self.failures), "failures": self.failures}

        return report

    def export_report(self):

        reports_dir = os.path.join(os.getcwd(), "reports")
        os.makedirs(reports_dir, exist_ok=True)

        path = os.path.join(reports_dir, "failure_analysis.json")

        with open(path, "w") as f:
            json.dump(self.generate_report(), f, indent=4)

        return path
