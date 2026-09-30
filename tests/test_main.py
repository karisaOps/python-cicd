from hello_python.main import greet


def test_greet():
    assert greet("John") == "Hello, John!"


def test_greet_different_name():
    assert greet("Alice") == "Hello, Alice!"