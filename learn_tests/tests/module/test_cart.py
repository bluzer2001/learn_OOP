from src.cart import Cart
from random import uniform, randint
import pytest


def test_cart_init_empty(empty_cart):
    assert empty_cart.items == list()


@pytest.mark.parametrize('price', [0, uniform(-100_000, 0)])
def test_cart_add_item_raise_error(price, empty_cart):

    with pytest.raises(ValueError):
        empty_cart.add(price)


def test_cart_add_item(empty_cart):
    cart = empty_cart
    n = randint(1, 40)
    generated_prices = [uniform(1, 100_000) for i in range(n)]
    for price in generated_prices:
        cart.add(price)
    assert cart.items == generated_prices


def test_cart_total_empty(empty_cart):
    assert empty_cart.total() == 0


def test_cart_total(empty_cart):
    cart = empty_cart
    n = randint(1, 40)
    generated_prices = [uniform(1, 100_000) for i in range(n)]
    for price in generated_prices:
        cart.add(price)
    assert cart.total() == sum(generated_prices)
