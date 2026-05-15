from src.checkout_service import CheckoutService
from src.payment_service import PaymentService
from src.exceptions import PaymentError, OrderEmptyError
from src.order import Order
import pytest

from unittest.mock import patch, Mock


@patch('src.payment_service.requests.post', )
def test_checkout_success(mock_post, filled_order):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "json": {"amount":  filled_order.total()},
    }

    mock_post.return_value = mock_response

    checkout_service = CheckoutService(PaymentService())

    checkout_service.checkout(filled_order)

    assert filled_order.is_paid is True


def test_checkout_with_zero_cost():
    order = Order()
    checkout_service = CheckoutService(PaymentService())

    with pytest.raises(OrderEmptyError):
        checkout_service.checkout(order)


@patch('src.payment_service.requests.post', )
def test_checkout_payment_return_not_success(mock_post, filled_order):

    mock_response = Mock()
    mock_response.status_code = 404

    mock_post.return_value = mock_response

    checkout_service = CheckoutService(PaymentService())

    with pytest.raises(PaymentError):
        checkout_service.checkout(filled_order)
