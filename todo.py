"""
    todo.py Gabriel Edwards
    This is a simple To-Do List application in python
    
    """
    
menu = """
    ToDO List - Choose an Option: 
    1. View Tasks 
    2. Add a Task 
    3. Exit
    """
    
while True: 
        print(menu)
        user_input = input(">").strip()
        # This handles menu choices
        
        todo_items = {}
        
        
        #this allows us to add tasks at will
        task_name = input("Enter a task Description: ")
        todo_items[task_name] = False
        print(f"Task '{task_name}' added.")
        
        
        if not todo_items:
            print("No tasks available. ")
        else: 
            for idx, (task, done) in enumerate(todo_items.items(), start=1):
                status = "(DONE)" if done else ""
                print(f"{idx}. {task} {status}")
                
                
        task_index = int(input("select the task number: ")) - 1
        task_name = list(todo_items.keys())[task_index]
        
        print("1. Mark as Done \n2. Delete Task")
        action = input(">").strip()
        
        if action == '1':
            todo_items[task_name] = True
            print(f"Task '{task_name}' mark as done. ")
        elif action == '2':
            del todo_items[task_name]
            print(f"Task '{task_name}' deleted. ")
        
        
        
        
        