### Task Manager
This was a super fun exercise that I asked chatGPT to give me.  I had a lot of fun learning how to manipulate lists.

It's shy on comments and has no input error handling, but it works.

### From chatGPT...
Of course! Here's a Python challenge to help you exercise your skills:

**Challenge: Build a Simple Task Manager**

Create a Python program that acts as a simple task manager. Your program should allow the user to perform the following operations:

1. **Add a Task**: Allow the user to add a task to the task list. Each task should have a title and a description.

2. **List Tasks**: Display a list of all tasks with their titles and descriptions.

3. **Mark Task as Complete**: Allow the user to mark a task as completed.

4. **Delete Task**: Allow the user to delete a task from the list.

5. **Quit**: Exit the program.

Here are some additional guidelines:

- Use dictionaries or lists to store tasks, and use functions to encapsulate the logic for each operation.
- You can use the `input()` function to take user input for task titles, descriptions, and menu choices.
- Create a simple menu system that allows the user to choose which operation they want to perform.
- Implement error handling to handle cases where the user provides invalid input, such as trying to mark a task as complete when it doesn't exist.

Here's a basic outline to get you started:

```python
# Define a list or dictionary to store tasks
tasks = []

# Define functions for each operation (add_task, list_tasks, mark_task_complete, delete_task, etc.)

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

    if choice == '5':
        break  # Exit the loop and quit the program
```

Feel free to expand upon this basic outline and add more features as you become more comfortable with Python. Good luck, and have fun coding! If you have any questions or need further assistance, feel free to ask.