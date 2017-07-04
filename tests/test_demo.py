from src import demo


def test_greeting():
    assert demo.greeting() == "Hello"


def test_farewell():
    assert demo.farewell() == "Goodbye!"
