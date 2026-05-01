from .constants import VALID_AGE, ADULT_AGE


def is_positive(n: int | float) -> bool:
    if n > 0:
        return True
    return False


def is_valid_age(age):
    if VALID_AGE[0] <= age <= VALID_AGE[1]:
        return True
    return False


def is_adult(age):
    if age >= ADULT_AGE:
        return True
    return False


def can_register(age):
    if is_valid_age(age) and is_adult(age):
        return True
    return False


def is_palindrome(s):
    if s == s[::-1]:
        return True
    return False


def reformat_name(name: str):
    return name.strip().capitalize()