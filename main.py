import pytest


def always_returns_true():
    cherries = "the best fruit"
    asparagus = "I don't know how to spell it"
    cats = "The best"
    return True


def test_always_returns_true():
    assert always_returns_true()
