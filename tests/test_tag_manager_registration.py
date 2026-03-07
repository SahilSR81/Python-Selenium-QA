from utils.tag_manager import TagManager


def test_tag_registration():

    manager = TagManager()

    manager.register_test("test_sample", ["smoke"])

    assert "test_sample" in manager.tags
