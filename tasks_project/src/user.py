from src.tasks.models import Tag
from src.tasks.task import Task

from src.project import Project


class User:

  def __init__(self):
    self.projects = []
    self.tasks = []

  def create_task(self, name, tags: list[Tag] | None = None, projects: list[Project] | None = None):
    new_task = Task(name)
    if tags:
      new_task.add_tags(*tags)
    self.tasks.append(new_task)
    if projects:
      for project in projects:
        project.add_task(new_task)

  def create_project(self, name):
    new_project = Project(name)
    self.projects.append(new_project)

  def delete_project(self, project):
    if project in self.projects:
      self.projects.remove(project)

  @property
  def progress(self):
    if not self.projects:
      return 0
    return sum(project.progress for project in self.projects) / len(self.projects)