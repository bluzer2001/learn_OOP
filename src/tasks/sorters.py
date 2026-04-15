from abc import ABC, abstractmethod
from src.tasks.task import Task

class TaskSorter(ABC):
  
  @abstractmethod
  def sort_tasks(self, tasks: list[Task], asc=False):
    pass


class TaskByPrioritySorter(TaskSorter):
  # TODO: Подумать как сократить

  def sort_tasks(self, tasks: list[Task], desc=False):
    return sorted(tasks, key=lambda x: x.priority, reverse=desc)


class TaskByStatusSorter(TaskSorter):

  def sort_tasks(self, tasks: list[Task], desc=False):
    return sorted(tasks, key=lambda x: x.is_done, reverse=desc)


class TaskByNameSorter(TaskSorter):

  def sort_tasks(self, tasks: list[Task], desc=False):
    return sorted(tasks, key=lambda x: x.name, reverse=desc)


class TaskByCommentsSorter(TaskSorter):

  def sort_tasks(self, tasks: list[Task], desc=False):
    return sorted(tasks, key=lambda x: len(x.comments), reverse=desc)