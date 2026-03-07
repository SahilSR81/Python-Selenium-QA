def test_tag_cli_option(pytestconfig):

    value = pytestconfig.getoption("--tag")

    assert value is None or isinstance(value, str)
