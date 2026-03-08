from utils.test_impact_analyzer import TestImpactAnalyzer


def test_mapping_logic():
    analyzer = TestImpactAnalyzer()
    analyzer.changed_files = ["login_page.py"]
    affected = analyzer.map_tests()
    assert isinstance(affected, list)
