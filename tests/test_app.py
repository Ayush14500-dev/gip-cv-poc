from app import greet, add


def test_greet():
    assert greet("GIP") == "Hello, GIP"


def test_add():
    assert add(2, 3) == 5


def test_greet_not_empty():
    assert greet("POC") != ""
