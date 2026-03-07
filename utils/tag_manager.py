import os
import json


class TagManager:

    def __init__(self):
        self.tags = {}

    def register_test(self, test_name, tags):

        if not isinstance(tags, list):
            tags = [tags]

        self.tags[test_name] = tags

    def get_tags(self, test_name):
        return self.tags.get(test_name, [])

    def filter_tests(self, selected_tag):

        result = []

        for test, tags in self.tags.items():
            if selected_tag in tags:
                result.append(test)

        return result

    def export_tags(self):

        reports_dir = os.path.join(os.getcwd(), "reports")
        os.makedirs(reports_dir, exist_ok=True)

        path = os.path.join(reports_dir, "tag_registry.json")

        with open(path, "w") as f:
            json.dump(self.tags, f, indent=4)

        return path
