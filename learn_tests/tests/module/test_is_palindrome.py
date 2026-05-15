from src.functions import is_palindrome
from random import choice, randint
import string

CHARACTERS = string.ascii_letters + string.digits

def gen_random_string():
    len_str = randint(0, 100_000)
    return "".join(choice(CHARACTERS) for _ in range(len_str))

def test_is_palindrome_return_true_case1():
    random_str = gen_random_string()
    palindrome_str = random_str + random_str[::-1]
    assert is_palindrome(palindrome_str) is True
    # palindromes = ["ABBA", "rotor", "OpWefeWpO"]
    # for palindrome in palindromes:
    #     assert is_palindrome(palindrome) is True


def test_is_palindrome_return_true_case2():
    random_str = gen_random_string()
    palindrome_str = random_str[:-1] + random_str[::-1]
    assert is_palindrome(palindrome_str) is True


def test_is_palindrome_return_false():
    random_str = gen_random_string()
    if random_str[0] == random_str[-1]:
        random_str += choice(CHARACTERS)
    assert is_palindrome(random_str) is False
