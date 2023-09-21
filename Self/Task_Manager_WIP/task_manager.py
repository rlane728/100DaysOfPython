# Define a list or dictionary to store tasks
task_text = []
task_status = []
task_num = []

# Define functions for each operation (add_task, list_tasks, mark_task_complete, delete_task, etc.)

def addTask():
    new_task = input("Please describe the task you would like to add to the list: \n")
    if len(task_num) == 0:
        task_num.append(1)
    else:
        task_num.append(task_num[-1] + 1)
    task_text.append(new_task)
    task_status.append("Incomplete")

def listTasks():
    count = 0
    max_count = (len(task_num))
    while count != max_count:
        print(f"{task_num[count]}: {task_status[count]}: {task_text[count]}")
        count += 1

def completeTask():
    complete = (int(input("Enter the task number that you would like to mark complete: \n")) - 1)
    task_status[complete] = "Complete"

def deleteTask():
    delete = (int(input("Enter the task number that you would like to delete: \n")) - 1)
    task_num.pop(delete)
    count_min = 1
    count_max = len(task_num)
    # print(count_max)
    while count_min <= count_max:
        count_step = (count_min - 1)
        task_num[count_step] = count_min
        count_min += 1


# Implement a loop to display the menu and handle user input
while True:
    print("Task Manager Menu:")
    print("1. Add a Task")
    print("2. List Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Quit")

    choice = input("Enter your choice: ")

    # Implement logic to perform the selected operation based on the user's choice

    if choice == '1':
        addTask()
        print(f"Your new task has been added to the list.")
    elif choice == '2':
        listTasks()
    elif choice == '3':
        completeTask()
    elif choice == '4':
        deleteTask()
    elif choice == '5':
        break  # Exit the loop and quit the program

