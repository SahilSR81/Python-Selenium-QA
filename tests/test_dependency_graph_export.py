import os
from utils.dependency_graph_builder import DependencyGraphBuilder


def test_export_graph():

    builder = DependencyGraphBuilder()

    builder.register_dependency("sample", "test_sample.py")

    path = builder.export_graph()

    assert os.path.exists(path)
