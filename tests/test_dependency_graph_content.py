from utils.dependency_graph_builder import DependencyGraphBuilder


def test_graph_content():

    builder = DependencyGraphBuilder()

    builder.register_dependency("dashboard", "test_dashboard_pom.py")

    assert "test_dashboard_pom.py" in builder.graph["dashboard"]
