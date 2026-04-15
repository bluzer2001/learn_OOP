from src.tasks.task import Task
from src.tasks.sorters import TaskSorter


class Project:

  def __init__(self, name: str):
    self.name = name
    self.tasks: list[Task] = []

  def add_task(self, task: Task):
    self.tasks.append(task)

  def remove_task(self, task: Task):
    if task in self.tasks:
      self.tasks.remove(task)

  @property
  def progress(self):
    if not self.tasks:
      return 0

    return sum(task.is_done for task in self.tasks) / len(self.tasks)

  def finish_project(self):
    for task in self.tasks:
      task.do()

  def get_sorted_tasks(self, sorter: TaskSorter):
    return sorter.sort_tasks(self.tasks)