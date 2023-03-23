import pytest


def always_returns_true():
    cherries = "the best fruit"
    return True


def test_always_returns_true():
    assert always_returns_true()
