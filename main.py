from src.user import User
from src.project import Project
from src.tasks.task import Task
from src.tasks.sorters import TaskByPrioritySorter

from src.notifiers import EmailNotifier


user = User()

print(user)

task = Task('Сделать дз', EmailNotifier())

print(task)

project = Project('ДЗ')

print(project)

sorter = TaskByPrioritySorter()

print(sorter)