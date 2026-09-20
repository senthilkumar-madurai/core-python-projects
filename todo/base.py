from abc import ABC, abstractmethod
from datetime import datetime
from dataclasses import dataclass, field
from enum import Enum

class Status(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

@dataclass
class Task:
    id: int = 0
    title: str = ""
    status: Status = Status.PENDING
    created_at: str = field(default_factory= datetime.now())
    update_at: str = field(default_factory= datetime.now())

    @staticmethod
    def _allowed_fields():
        return ["title", "status"]
    
class TaskManager(ABC):
    def __init__(self):
        super().__init__()

        self.tasks:dict[int, Task] = {}

    @abstractmethod
    def get_all(self):
        pass
    
    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def create(self):
        pass
    
    @abstractmethod
    def update(self):
        pass
    
    @abstractmethod
    def delete(self):
        pass

    def _task_exists(self, task_id: int) -> bool:
        return task_id in self.tasks
