def to_do_list():
    tasks = []
    print("----- My To-Do App -----")

    total_tasks = int(input("Number of tasks you want to enter = "))
    for i in range(1, total_tasks + 1):
        task = input(f"Enter task {i} = ")
        tasks.append(task)

    print(f"Added tasks:\n{tasks}")

    while True:
        menu = int(input(
            "\nEnter:\n"
            "1 - Add\n"
            "2 - Update\n"
            "3 - Delete\n"
            "4 - View\n"
            "5 - Quit / Exit\n"
        ))

# Logic of - to-do-app 

        if menu == 1:
            add = input("Enter task you want to add = ")
            tasks.append(add)
            print(f"Task {add} added successfully :)")

        elif menu == 2:
            update_val = input("Enter the task name you want to update = ")
            if update_val in tasks:
                updated_task = input("Enter new task = ")
                ind = tasks.index(update_val)
                tasks[ind] = updated_task
                print(f"Task updated to {updated_task}")
            else:
                print("Task not found!")

        elif menu == 3:
            del_val = input("Enter task you want to delete = ")
            if del_val in tasks:
                tasks.remove(del_val)
                print(f"Task {del_val} deleted...")
            else:
                print("Task not found!")

        elif menu == 4:
            print("Your tasks;")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

        elif menu == 5:
            print("Goodbye... :)")
            break

        else:
            print("Invalid input! Please choose 1-5")

to_do_list()
