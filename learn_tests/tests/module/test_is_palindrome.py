from src.functions import is_palindrome
from random import choice, randint
import string

CHARACTERS = string.ascii_letters + string.digits

# TODO: разбить на 2 теста и сделать функцию для генерации тестовых данных
def test_is_palindrome_return_true():
    len_str = randint(0, 100_000)
    random_str = ''.join(choice(CHARACTERS) for _ in range(len_str))
    res_str_case1 = random_str + random_str[::-1]
    res_str_case2 = random_str[:-1] + random_str[::-1]
    assert is_palindrome(res_str_case1) is True
    assert is_palindrome(res_str_case2) is True
    # palindromes = ["ABBA", "rotor", "OpWefeWpO"]
    # for palindrome in palindromes:
    #     assert is_palindrome(palindrome) is True


def test_is_palindrome_return_false():
    len_str = randint(0, 100_000)
    random_str = ''.join(choice(CHARACTERS) for _ in range(len_str))
    if random_str[0] == random_str[-1]:
        random_str += choice(CHARACTERS)
    assert is_palindrome(random_str) is False
