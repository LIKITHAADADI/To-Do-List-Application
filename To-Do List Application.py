filename = "tasks.txt"

def load_tasks():
    try:
        with open(filename, 'r') as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(filename, 'w') as f:
        for task in tasks:
            f.write(task + "\n")

def view_tasks(tasks):
    if not tasks:
        print("Empty Task List")
    else:
        print("Your todo-task list:")
        for i, task in enumerate(tasks):
            print(f"{i} - {task}")

def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added.")

def remove_task(tasks):
    view_tasks(tasks)
    try:
        n = int(input("Enter the task number to remove: "))
        if 0 <= n < len(tasks):
            r = tasks.pop(n)
            print(f"Removed Task: {r}")
        else:
            print("Invalid number")
    except ValueError:
        print("Enter a valid number")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- TO-DO LIST ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
