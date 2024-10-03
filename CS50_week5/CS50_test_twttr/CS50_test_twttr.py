from CS50_twttr import shorten
import pytest


def main():
    test_upper_lower_case()
    test_number


def test_upper_lower_case():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("TwItTeR") == "TwtTR"


def test_number():
    assert shorten("1234") == "1234"


def test_punctuation():
    assert shorten("!?.,") == "!?.,"


if __name__ == "__main__":
    main()
