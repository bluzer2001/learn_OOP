from src.notifiers import BaseNotifier
from src.enums import Priority
from .models import Comment, Tag
from .logger import Logger

class Task:


  def __init__(self, name, notifier: BaseNotifier, priority: Priority = Priority.MEDIUM):
    self.name = name
    self.is_done = False
    self.comments = []
    self.tags = []
    self.priority = priority
    self.logger = Logger()
    self.notifier = notifier

  def do(self):
    self.is_done = True
    self.logger.write_log("Задача сделана")
    self.notifier.notify("Задача сделана")
    

  def add_comment(self, text):
    new_comment = Comment(text)
    self.comments.append(new_comment)

  def add_tags(self, *tags: tuple[Tag]):
    self.tags.extend(tags)

  def change_priority(self, priority):
    self.priority = priority
    self.logger.write_log(f"Поменялся приоритет на {priority}")