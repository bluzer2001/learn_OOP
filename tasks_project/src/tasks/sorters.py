from abc import ABC, abstractmethod
from src.tasks.task import Task

class TaskSorter(ABC):

  def __init__(self):
    self.key = lambda x: x
  
  def sort_tasks(self, tasks: list[Task], asc=False):
    return sorted(tasks, key=self.key, reverse=desc)


class TaskByPrioritySorter(TaskSorter):

  def __init__(self):
    self.key = lambda x: x.priority


class TaskByStatusSorter(TaskSorter):

  def __init__(self):
    self.key = lambda x: x.is_done


class TaskByNameSorter(TaskSorter):

  def __init__(self):
    self.key = lambda x: x.name


class TaskByCommentsSorter(TaskSorter):

  def __init__(self):
    self.key = lambda x: len(x.comments)
