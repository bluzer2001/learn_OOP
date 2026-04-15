class BaseNotifier:

  def notify(self, message):
    print(f"Отправка: {message}")


class EmailNotifier(BaseNotifier):

  def notify(self, message):
    print(f"Отправка по email: {message}")


class SMSNotifier(BaseNotifier):

  def notify(self, message):
    print(f"Отправка по sms: {message}")