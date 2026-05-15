from src.exceptions import PaymentError, OrderEmptyError


class CheckoutService:

    def __init__(self, payment_service):
        self.payment_service =  payment_service

    def checkout(self, order):
        amount = order.total()

        if amount == 0:
            raise OrderEmptyError

        payment_status = self.payment_service.pay(amount)

        if not payment_status:
            raise PaymentError

        order.is_paid = True