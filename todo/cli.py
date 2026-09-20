import base
import sys
from main import Todo

class Cli:
    def __init__(self):
        super().__init__()
        
    def create(self):
        return super().create()

    def get(self):
        return super().get()
    
    def get_all(self):
        return super().get_all()

    def update(self):
        return super().update()

    def delete(self):
        return super().delete()

if __name__ == "__main__":
    sys_args = sys.argv
    length = len(sys_args)
    if(length < 2):
        print("Invalid Command")

    todo = Todo() 
    todo.create(title="demo")
    action = sys_args[1]
    
    match(action):
        case 'add':
            if length < 3:
                print("Must provide the title")
            else:
                title = sys_args[2]
                todo.create(title=title)    
        case 'update':
            print("update")

        case "list":
            if length == 3:
                pass
            else:
                todo.get_all()
            

        case "delete":
            if length < 3:
                print("Must provide the ID")
            else:
                id = int(sys_args[2])
                todo.delete(id=id)

        case _:
            print("Invaild Command")