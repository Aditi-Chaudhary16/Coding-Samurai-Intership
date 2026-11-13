
# Coding Samurai Internship
# Project 2: To-Do List Application

tasks = []
completed_tasks = []

# Load tasks from file
try:
    with open("tasks.txt", "r") as file:
        for line in file:
            line = line.strip()

            if "|" in line:
                task, status = line.split("|", 1)
            else:
                task = line
                status = "Pending"

            if task:
                tasks.append(task)

                if status == "Completed":
                    completed_tasks.append(task)

except FileNotFoundError:
    pass


# Save tasks to file
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            status = "Completed" if task in completed_tasks else "Pending"
            file.write(task + "|" + status + "\n")


# Main program
while True:

    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Task
    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        save_tasks()
        print("Task added successfully!")

    # View Tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")

            for i, task in enumerate(tasks, start=1):
                status = "Completed" if task in completed_tasks else "Pending"
                print(i, ".", task, "-", status)

    # Delete Task
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(i, ".", task)

            task_number = int(input("Enter task number to delete: "))

            if 1 <= task_number <= len(tasks):
                task = tasks.pop(task_number - 1)

                if task in completed_tasks:
                    completed_tasks.remove(task)

                save_tasks()
                print("Task deleted successfully!")
            else:
                print("Invalid task number!")

    # Mark Task as Completed
    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                status = "Completed" if task in completed_tasks else "Pending"
                print(i, ".", task, "-", status)

            task_number = int(input("Enter task number to mark completed: "))

            if 1 <= task_number <= len(tasks):
                task = tasks[task_number - 1]

                if task not in completed_tasks:
                    completed_tasks.append(task)
                    save_tasks()
                    print("Task marked as completed!")
                else:
                    print("Task is already completed!")
            else:
                print("Invalid task number!")

    # Exit
    elif choice == "5":
        print("Thank you for using To-Do List!")
        break

    else:
        print("Invalid choice!")
