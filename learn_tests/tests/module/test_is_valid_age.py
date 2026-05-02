from src.constants import VALID_AGE
from src.functions import is_valid_age
from random import randint


def test_is_valid_age_return_true():
    age = randint(*VALID_AGE)
    assert is_valid_age(age) is True


def test_is_valid_age_return_false():
    lower_than_left_bound = randint(VALID_AGE[0] - 100_000, VALID_AGE[0] - 1)
    higher_than_right_bound = randint(VALID_AGE[1] + 1, VALID_AGE[1] + 100_000)
    assert is_valid_age(lower_than_left_bound) is False
    assert is_valid_age(lower_than_left_bound) is False
