from src.functions import is_positive
from random import uniform


def test_is_positive_return_true():
    n = uniform(1, 100_000)
    assert is_positive(n) is True


def test_is_positive_return_false():
    n = uniform(-100_000, 0)
    assert is_positive(n) is False

