
task = [] 

while True:
      
    print("ENTER YOUR CHOICE")
    print("1 Add Task")
    print("2 View Task")
    print("3 Delete Task")
    print("4 Exit")

    choice = int(input("Enter Your Choice (1-4) :"))

    if choice == 1:
        task_1 = input("Enter your task :")
        task.append(task_1)
        
        print("task added succesfully.......")
        print(task)

        f = open("store.txt", "a")
        f.append(task_1)

    
    

    elif choice == 2:
        if len(task) == 0:
            print("No task available ")
        else:
            print("\n your task ")

            for i, task in enumerate(task, start=1):
                    print(f"{i}. {task}")

    elif choice == 3:
        if len(task) == 0:
            print("No Task available...")

        else: 
            print("\n your task.")

            for i, task in enumerate(task, start=1):
                            print(f"{i}. {task}")

        task_number = int(input("enter a task number to delete :"))

        remove_task = task.pop(task_number - 1)

        print(f"{remove_task} deleted..")


    elif choice == 4:
        print("goodbyeee")
    

    else:
        print("invalidd")