class FlakyTracker:
    def __init__(self):
        self.retry_counts = {}

    def record_retry(self, test_name):
        self.retry_counts[test_name] = self.retry_counts.get(test_name, 0) + 1

    def get_flaky_tests(self):
        return {k: v for k, v in self.retry_counts.items() if v > 0}
