

class CheckoutError(Exception):
    pass


class OrderEmptyError(CheckoutError):

    def __init__(self, value = "Заказ пустой"):
        super().__init__(value)


class PaymentError(CheckoutError):

    def __init__(self, value = "Ошибка оплаты"):
        super().__init__(value)