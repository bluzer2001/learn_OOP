from src.tasks.task import Task
from pathlib import Path
from abc import ABC, abstractmethod


class TaskExporter(ABC):
    
    @abstractmethod
    def export_tasks(self, task_list: list[Task], *args, **kwargs):
        pass


class JsonTaskExporter(TaskExporter):

    def export_tasks(self, task_list: list[Task], path_to_save: str | Path):
        import json
        serialized_tasks = []
        for task in task_list:
            serialized_task = {
                "name": task.name,
                "is_done": task.is_done,
                "comments": task.comments,
                "tags": task.tags,
                "priority": task.priority
            }
            serialized_tasks.append(serialized_task)
        
        with open(path_to_save, 'w', encoding='UTF-8') as f:
            json.dump(serialized_tasks, f)


class TxtTaxtExporter(TaskExporter):

    def export_tasks(self, task_list: list[Task], path_to_save: str | Path):
        with open(path_to_save, 'w', encoding='UTF-8') as f:
    
            for task in task_list:
                serialized_task = {
                    "name": task.name,
                    "is_done": task.is_done,
                    "comments": task.comments,
                    "tags": task.tags,
                    "priority": task.priority
                }
                print(serialized_task, file=f, end='\n')
            
        