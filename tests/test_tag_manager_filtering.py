from utils.tag_manager import TagManager


def test_tag_filter():

    manager = TagManager()

    manager.register_test("test_a", ["smoke"])
    manager.register_test("test_b", ["regression"])

    result = manager.filter_tests("smoke")

    assert "test_a" in result
