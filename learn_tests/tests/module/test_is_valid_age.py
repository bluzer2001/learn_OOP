from src.constants import VALID_AGE
from src.functions import is_valid_age
from random import randint
import pytest


def test_is_valid_age_return_true():
    age = randint(*VALID_AGE)
    assert is_valid_age(age) is True


@pytest.mark.parametrize('low,high',
                         [(VALID_AGE[0] - 100_000, VALID_AGE[0] - 1),
                          (VALID_AGE[1] + 1, VALID_AGE[1] + 100_000)])
def test_is_valid_age_return_false(low, high):
    bounds = randint(low, high)
    assert is_valid_age(bounds) is False
