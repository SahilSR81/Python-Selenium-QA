import os
import json


class DependencyGraphBuilder:

    def __init__(self):
        self.graph = {}

    def register_dependency(self, module, test_name):

        if module not in self.graph:
            self.graph[module] = []

        if test_name not in self.graph[module]:
            self.graph[module].append(test_name)

    def build_graph(self, tests_dir="tests"):

        for root, _, files in os.walk(tests_dir):

            for file in files:

                if not file.startswith("test_"):
                    continue

                path = os.path.join(root, file)

                module_name = file.replace("test_", "").replace(".py", "")

                self.register_dependency(module_name, file)

        return self.graph

    def export_graph(self):

        reports_dir = os.path.join(os.getcwd(), "reports")
        os.makedirs(reports_dir, exist_ok=True)

        path = os.path.join(reports_dir, "dependency_graph.json")

        with open(path, "w") as f:
            json.dump(self.graph, f, indent=4)

        return path
