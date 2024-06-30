from src.hello import more_hello, more_bye


def test_more_hello():
    assert "hi jk" == more_hello()


def test_more_bye():
    assert "bye jk" == more_bye()
