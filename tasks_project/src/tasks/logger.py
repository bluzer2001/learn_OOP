class Logger:

  def __init__(self):
    self.log_messages = []

  def write_log(self, log_message: str):
    self.log_messages.append(log_message)