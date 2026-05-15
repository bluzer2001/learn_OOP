import pytest
from random import uniform, randint

from src.cart import Cart
from src.counter import Counter
from src.order import Order


@pytest.fixture
def counter():
    n = uniform(-100_000, 100_000)
    counter = Counter(n)
    return counter


@pytest.fixture
def empty_cart():
    return Cart()


@pytest.fixture
def filled_order():
    order = Order()
    for i in range(randint(1, 100)):
        order.add(uniform(1, 10_000))
    return order