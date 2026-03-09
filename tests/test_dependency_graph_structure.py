from utils.dependency_graph_builder import DependencyGraphBuilder


def test_graph_structure():

    builder = DependencyGraphBuilder()

    builder.register_dependency("login", "test_login_pom.py")

    graph = builder.graph

    assert "login" in graph
