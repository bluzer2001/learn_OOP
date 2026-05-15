from src.constants import ADULT_AGE, VALID_AGE
from src.functions import can_register
from random import randint


def test_can_register_return_true():
    age = randint(ADULT_AGE, VALID_AGE[1])
    assert can_register(age) is True


def test_can_register_not_adult():
    age = randint(VALID_AGE[0], ADULT_AGE - 1)
    assert can_register(age) is False


def test_can_register_not_valid_age():
    age_too_low = randint(VALID_AGE[0] - 100_000, VALID_AGE[0] - 1)
    age_too_high = randint(VALID_AGE[1] + 1, VALID_AGE[1] + 100_000)
    assert can_register(age_too_low) is False
    assert can_register(age_too_high) is False
