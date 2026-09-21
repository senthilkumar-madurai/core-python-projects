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
    created_at: str = field(default_factory= datetime.now)
    updated_at: str = field(default_factory= datetime.now)

    @staticmethod
    def allowed_fields():
        return ["title", "status"]

    @staticmethod
    def validate_title(title:str) -> str:
        title = title.strip()
        if not title:
            raise ValueError("Title can't be empty")
        
        return title

    @staticmethod
    def validate_status(status:str) -> Status:
        status = status.strip().lower()
        if not status:
            raise ValueError("Status can't be empty")
        
        try:
            return Status(status)
        except ValueError:
            raise ValueError("Invalid Status. Only allowed pending, in_progress, completed.")
    
class TasksBase(ABC):
    def __init__(self):
        super().__init__()

        self.tasks:dict[int, Task] = {}

    @abstractmethod
    def get_all(self) -> dict:
        pass
    
    @abstractmethod
    def get(self, id:int) -> Task:
        pass

    @abstractmethod
    def create(self, title: str, status: Status) -> tuple[bool, Task]:
        pass
    
    @abstractmethod
    def update(self) -> Task:
        pass
    
    @abstractmethod
    def delete(self) -> bool:
        pass

    def _task_exists(self, task_id: int) -> bool:
        return task_id in self.tasks