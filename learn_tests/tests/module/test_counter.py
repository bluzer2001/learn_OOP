import random

from src.counter import Counter
from random import uniform
import pytest


@pytest.mark.parametrize('n', [0, random.uniform(-100_000, 100_000)])
def test_counter_init_with_zero(n):
    counter = Counter(n)
    assert counter.count == n


def test_counter_increment(counter):
    n = counter.count
    counter.increment()
    assert counter.count == n + 1


def test_counter_decrement(counter):
    n = counter.count
    counter.decrement()
    assert counter.count == n - 1


def test_counter_reset(counter):
    counter.reset()
    assert counter.count == 0
