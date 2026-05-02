import pytest
from random import uniform

from src.cart import Cart
from src.counter import Counter


@pytest.fixture
def counter():
    n = uniform(-100_000, 100_000)
    counter = Counter(n)
    return counter


@pytest.fixture
def empty_cart():
    return Cart()
