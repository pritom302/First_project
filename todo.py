# todo.py
import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        file.write("\n".join(tasks))

def show_tasks(tasks):
    if not tasks:
        print("No tasks found!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    print()

def main():
    tasks = load_tasks()

    while True:
        print("=== TO-DO LIST MENU ===")
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            task = input("Enter a new task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Task added!\n")
        elif choice == "3":
            show_tasks(tasks)
            num = int(input("Enter task number to delete: ")) - 1
            if 0 <= num < len(tasks):
                removed = tasks.pop(num)
                save_tasks(tasks)
                print(f"Removed task: {removed}\n")
            else:
                print("Invalid task number!\n")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!\n")

if __name__ == "__main__":
    main()
