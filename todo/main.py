from base import Task, TaskManager

class Todo(TaskManager):
    def __init__(self):
        super().__init__()
        
    def get_all(self):
        print("\n ID \t Title \t Status \t Created At")
        print("====\t=======\t========\t============")
            
        if(self.tasks):
            for task in self.tasks.values():
                print(f"{task.id}\t{task.title}\t{task.status}\t {task.created_at}")
        else:
            print("\t\tNo tasks are found.")

        print()
    
    def create(self, title:str, status:str = "pending"):
        last_id = next(reversed(self.tasks)) if self.tasks else 0
        id = last_id + 1
        task = Task(
                id=id,
                title=title,
                status=status
            )

        self.tasks[id] = task
        print(f"\n[{id}] Task created successfuly....")

    def update(self, id:int, **kwargs):
        if(self._task_exists(id=id)):
            print("\nInvaild Task ID\n")
            return

        if(not kwargs):
            print("\nNothing to update...\n")
            return
        
        task = self.tasks[id]
        updated = False
        for field, value in kwargs.items():
            if(field not in Task._allowed_fields()):
                continue

            setattr(task, field, value)
            updated = True

        if(updated):
            print(f"\n[{id}] Task updated successfuly....")
        else:
            print("\nNothing to update...\n")

    def delete(self, id: int):
        if(self._task_exists(id=id)):
            print("\nInvaild Task ID\n")
            return

        self.tasks.pop(id)
        print(f"\n[{id}] Task deleted successfuly....")

    def get(self, id: int):
        if(self._task_exists(id=id)):
            print("\nInvaild Task ID\n")
            return

        task = self.tasks[id]
        print(f"\nID : {task.id}")
        print(f"Title : {task.title}")
        print(f"Status : {task.status}")
        print(f"Created At : {task.created_at}")
        print(f"Updated At : {task.update_at}")
        print()

    @staticmethod
    def input_task_details():
        data = {}
        fields = vars(Task()).keys()
        for field in fields:
            if field not in Task._allowed_fields():
                continue
            
            data[field] = input(f"Enter the {field} of the Task : ")

        return data

    def start(self):
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
                    self.get_all()
                case 2:
                    id = int(input("Enter the Task ID : "))
                    self.get(id)
                case 3:
                    data = self.input_task_details()
                    self.create(**data)
                case 4:
                    id = int(input("Enter the ID of the Task : "))
                    data = self.input_task_details()
                    self.update(id=id, **data)
                case 5:
                    id = int(input("Enter the ID of the Task : "))
                    self.delete(id=id)
                case 6:
                    print("\n Thank You for Visiting... \n")
                    break
                    
if __name__ == "__main__":
    todo = Todo()
    todo.start()