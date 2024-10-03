from bank import value
import pytest


def test_hello():
    assert value("hello sir") == 0


def test_Hello():
    assert value("Hello sir") == 0


def test_h():
    assert value("how are you sir") == 20


def test_H():
    assert value("How are you sir") == 20


def test_helo():
    assert value("bye sir") == 100


def main():
    value()


if __name__ == "__main__":
    main()
