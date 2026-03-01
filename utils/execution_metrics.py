import time
import json
import os


class ExecutionMetrics:
    def __init__(self):
        self.start_time = time.time()
        self.test_durations = {}
        self.report_path = os.path.join(
            os.getcwd(), "reports", "execution_summary.json"
        )

    def record_test(self, test_name, duration):
        self.test_durations[test_name] = duration

    def generate_summary(self):
        total_time = time.time() - self.start_time

        slow_tests = {
            name: round(dur, 2) for name, dur in self.test_durations.items() if dur > 2
        }

        return {
            "total_execution_time": round(total_time, 2),
            "total_tests": len(self.test_durations),
            "slow_tests": slow_tests,
        }

    def export_summary(self, summary):
        reports_dir = os.path.join(os.getcwd(), "reports")
        os.makedirs(reports_dir, exist_ok=True)

        with open(self.report_path, "w") as f:
            json.dump(summary, f, indent=4)
