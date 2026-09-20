import base
import sys
from main import Todo

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
                try:
                    task = todo.create(title=title)
                    print(f"\n[{task.id}] Task created successfuly....")
                except Exception as e:
                    print("Something went Wrong...")  
                    
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