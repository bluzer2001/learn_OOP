class BaseNotifier:

  def notify(self, message):
    print(f"Отправка: {message}")


class EmailNotifier(BaseNotifier):

  def notify(self, message):
    print(f"Отправка по email: {message}")


class SMSNotifier(BaseNotifier):

  def notify(self, message):
    print(f"Отправка по sms: {message}")


class MultyNotifier:

  def __init__(self, notifiers: list[BaseNotifier]):
    self.notifiers = notifiers

  def notify(self, message):
    for notifier in self.notifiers:
      notifier.notify(message)