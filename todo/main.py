from base import Task, TasksBase, Status, InvalidTaskId

class TodoAPI(TasksBase):
    def __init__(self):
        super().__init__()

    def get(self, task_id: int):
        if not self._task_exists(task_id=task_id):
            raise InvalidTaskId()
        
        return self.tasks[task_id]
        
    def get_all(self):
        return self.tasks
    
    def create(self, title, status = Status.PENDING):
        last_id = next(reversed(self.tasks)) if self.tasks else 0
        task_id = last_id + 1
        task = Task(id=task_id, title=title, status=status)
        
        self.tasks[task_id] = task
        return task

    def update(self, task_id:int, **kwargs):
        if not self._task_exists(task_id=task_id):
            raise InvalidTaskId()

        updated = False
        task = self.tasks[task_id]
        
        if(not kwargs):
            return False, task
        
        for field, value in kwargs.items():
            if(field not in Task._allowed_fields()):
                continue

            setattr(task, field, value)
            updated = True

        return updated, task
        

    def delete(self, task_id: int):
        if not self._task_exists(task_id=task_id):
            raise InvalidTaskId()

        self.tasks.pop(task_id)
        return True
        
    @staticmethod
    def input_task_details():
        data = {}
        fields = vars(Task()).keys()
        for field in fields:
            if field not in Task._allowed_fields():
                continue
            
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
                    for task in tasks.values():
                        print(f"{task.id}\t{task.title}\t{task.status.value}\t{task.created_at}")
                else:
                    print("\t\tNo tasks are found.")
                    
            case 2:
                try:
                    task_id = int(input("Enter the Task ID : "))
                    task = todo.get(task_id=task_id)
                    print(f"ID : {task.id}")
                    print(f"Title : {task.title}")
                    print(f"Status : {task.status}")
                    print(f"Created At : {task.created_at}")
                    print(f"Updated At : {task.updated_at}")
                except(ValueError, InvalidTaskId):
                    print("Invaild ID. Try again.")
                except Exception as e:
                    print("Can't get the data")
                    
            case 3:
                try:
                    title = input("Enter the title of the Task : ")
                    status = Status(input("Enter the status of the Task : "))
                except ValueError:
                    print("Invalid status")
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
                        raise InvalidTaskId()
                except(ValueError, InvalidTaskId):
                    print("Invaild ID. Try again.")
                    continue

                try:
                    title = input("Enter the title of the Task : ")
                    status = Status(input("Enter the status of the Task : "))
                except ValueError:
                    print("Invalid status")
                    continue
                try:
                    updated, task = todo.update(task_id=task_id, title=title, status=status)
                    if(updated):
                        print(f"[{task.id}] Task updated successfuly.")
                    else:
                        print("Nothing to update.")
                except(InvalidTaskId):
                    print("Invaild ID. Try again.")
                except Exception as e:
                    print("Can't update task.", e)
                    
            case 5:
                try:
                    id = int(input("Enter the ID of the Task : "))
                    deleted = todo.delete(id=id)
                    if(deleted):
                       print(f"\n[{task_id}] Task deleted successfuly....")
                except(ValueError, InvalidTaskId):
                    print("Invaild ID. Try again.")
                except Exception as e:
                    print("Can't delete the task.")
                        
            case 6:
                print("\n Thank You for Visiting... \n")
                break