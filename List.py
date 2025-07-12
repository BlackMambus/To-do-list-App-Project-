def display_menu():
    """Displays the to-do list menu."""
    print("\nTo-Do List Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as completed")
    print("4. Remove a task")
    print("5. Exit")


def add_task(todo_list):
    """Adds a task to the to-do list."""
    task = input("Enter the task to add: ")
    todo_list.append({"task": task, "completed": False})
    print("Task added!")


def view_tasks(todo_list):
    """Views the tasks in the to-do list."""
    if not todo_list:
        print("No tasks in the to-do list.")
        return

    print("\nTasks:")
    for index, task_data in enumerate(todo_list):
        status = "✓" if task_data["completed"] else " "  # Use checkmark if completed
        print(f"{index + 1}. [{status}] {task_data['task']}")


def mark_completed(todo_list):
    """Marks a task as completed."""
    view_tasks(todo_list)  # Show tasks with indices
    try:
        task_number = int(input("Enter the number of the task to mark as completed: "))
        if 1 <= task_number <= len(todo_list):
            todo_list[task_number - 1]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def remove_task(todo_list):
    """Removes a task from the to-do list."""
    view_tasks(todo_list)  # Show tasks with indices
    try:
        task_number = int(input("Enter the number of the task to remove: "))
        if 1 <= task_number <= len(todo_list):
            removed_task = todo_list.pop(task_number - 1)
            print(f"Task '{removed_task['task']}' removed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    except IndexError:
        print("Invalid task number.")


def main():
    """Main function to run the to-do list application."""
    todo_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(todo_list)
        elif choice == "2":
            view_tasks(todo_list)
        elif choice == "3":
            mark_completed(todo_list)
        elif choice == "4":
            remove_task(todo_list)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
