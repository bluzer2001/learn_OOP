from src.constants import ADULT_AGE
from src.functions import is_adult
from random import randint


def test_is_adult_return_false():
    age = randint(0, ADULT_AGE - 1)
    assert is_adult(age) is False


def test_is_adult_return_true():
    age = randint(ADULT_AGE, 100_000)
    assert is_adult(age) is True
