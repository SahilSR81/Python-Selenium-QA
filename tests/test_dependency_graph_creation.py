from utils.dependency_graph_builder import DependencyGraphBuilder


def test_graph_builder():

    builder = DependencyGraphBuilder()

    graph = builder.build_graph()

    assert isinstance(graph, dict)
