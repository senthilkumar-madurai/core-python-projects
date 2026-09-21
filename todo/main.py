from base import Task, TasksBase, Status
from datetime import datetime

class TodoAPI(TasksBase):
    def __init__(self):
        super().__init__()

    def get(self, task_id: int):
        if not self._task_exists(task_id=task_id):
            raise ValueError("Invaild ID. Try again.")
        
        return self.tasks[task_id]
        
    def get_all(self):
        return list(self.tasks.values())
    
    def create(self, title, status = Status.PENDING):
        # title = Task.validate_title(title)
        # status = Task.validate_status(status)

        last_id = next(reversed(self.tasks)) if self.tasks else 0
        task_id = last_id + 1
        task = Task(id=task_id, title=title, status=status)
        
        self.tasks[task_id] = task
        return task

    def update(self, task_id:int, **kwargs):
        if not self._task_exists(task_id=task_id):
            raise ValueError("Invaild ID. Try again.")

        updated = False
        task = self.tasks[task_id]
        
        if not kwargs:
            return False, task
        
        for field, value in kwargs.items():
            if(field not in Task.allowed_fields()):
                raise ValueError(f"Invalid field [{field}]")

            setattr(task, field, value)
            updated = True

        task.updated_at = datetime.now()
        return updated, task

    def delete(self, task_id: int):
        if not self._task_exists(task_id=task_id):
            raise ValueError("Invaild ID. Try again.")

        self.tasks.pop(task_id)
        return True
        
    @staticmethod
    def input_task_details():
        data = {}
        fields = Task.allowed_fields()
        for field in fields:
            data[field] = input(f"Enter the {field} of the Task : ")

        return data
                    
if __name__ == "__main__":
    todo = TodoAPI()
    while True:
        print("\t\t\t ToDo List")
        print("\t\t\t==========")
        print("1. Get All Tasks")
        print("2. Get one task by ID")
        print("3. Create new task")
        print("4. Update task by ID")
        print("5. Delete task by ID")
        print("6. Exit")
        
        choice = int(input("Enter your choice : "))
        match(choice):
            case 1:
                tasks = todo.get_all()
                print("\n ID \t Title \t Status \t Created At")
                print("====\t=======\t========\t============")
                    
                if(tasks):
                    for task in tasks:
                        print(f"{task.id}\t{task.title}\t{task.status.value}\t{task.created_at}")
                else:
                    print("\t\tNo tasks are found.")
                    
            case 2:
                try:
                    task_id = int(input("Enter the Task ID : "))
                    task = todo.get(task_id=task_id)
                    print(f"ID : {task.id}")
                    print(f"Title : {task.title}")
                    print(f"Status : {task.status.value}")
                    print(f"Created At : {task.created_at}")
                    print(f"Updated At : {task.updated_at}")
                except ValueError as error:
                    print(error)
                except Exception as e:
                    print("Can't get the data")
                    
            case 3:
                try:
                    title = Task.validate_title(input("Enter the title of the Task : "))
                    status = Task.validate_status(input("Enter the status of the Task : "))
                except ValueError as error:
                    print(error)
                    continue

                try:
                    task = todo.create(title=title, status=status)
                    print(f"\n[{task.id}] Task created successfuly.")
                except Exception as e:
                    print("Can't create task.")
            case 4:
                try:
                    task_id = int(input("Enter the ID of the Task : "))
                    if not todo._task_exists(task_id=task_id):
                        raise ValueError("Invaild ID. Try again.")
                except ValueError as error:
                    print(error)
                    continue

                try:
                    title = Task.validate_title(input("Enter the title of the Task : "))
                    status = Task.validate_status(input("Enter the status of the Task : "))
                except ValueError as error:
                    print(error)
                    continue

                try:
                    updated, task = todo.update(task_id=task_id, title=title, status=status)
                    if(updated):
                        print(f"[{task.id}] Task updated successfuly.")
                    else:
                        print("Nothing to update.")
                except ValueError as error:
                    print(error)
                except Exception as e:
                    print("Can't update task.", e)
                    
            case 5:
                try:
                    id = int(input("Enter the ID of the Task : "))
                    deleted = todo.delete(id=id)
                    if(deleted):
                       print(f"\n[{task_id}] Task deleted successfuly....")
                except ValueError as error:
                    print(error)
                except Exception as e:
                    print("Can't delete the task.")
                        
            case 6:
                print("\n Thank You for Visiting... \n")
                break