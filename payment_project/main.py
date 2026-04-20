from abc import ABC, abstractmethod


class Order:

  def __init__(self, cost: int):
    self.is_paid = False
    self.is_reserved = False
    self.cost = cost


class Payment(ABC):

  def __init__(self, order: Order, amount: int):
    self.order = order
    self.amount = amount

  def _validate(self):
    if self.order.cost > 0 and self.amount > self.order.cost:
      return True
    raise Exception("Валидация не пройдена")

  @abstractmethod
  def make_payment(self):
    pass
  
  @abstractmethod
  def cancel_payment(self):
    pass

  def save_payment(self):
    print(f"Сохраняем оплату для заказа: {self.order} - сумма: {self.amount}")

  def send_check(self):
    print(f"Чек по заказу {self.order} на сумму {self.amount}")


class CardPayment(Payment):

  def make_payment(self):
    self._validate()
    self.order.is_paid = True

  def cancel_payment(self):
    self.order.is_paid = False


class ReservationPayment(Payment):
  
  def make_payment(self):
    self._validate()
    self.order.is_reserved = True

  def cancel_payment(self):
    self.order.is_reserved = False


# def checkout(order: Order, payment_type: Payment):
#     processor.make_payment()

#     if not order.is_paid or not order.is_reserved:
#       raise Exception("Ошибка оплаты")


card_order = Order(100)
reservation_order = Order(10)

card_payment = CardPayment(card_order, 100)
reservation_payment = ReservationPayment(reservation_order, 10)

# checkout(card_order, card_payment)
# checkout(reservation_order, reservation_payment)
