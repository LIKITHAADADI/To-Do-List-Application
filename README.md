# 📝 To-Do List Application

A simple command-line based To-Do List application written in Python that allows users to manage their daily tasks with options to view, add, and remove tasks. All tasks are stored in a text file (`tasks.txt`) so that data persists between sessions.

---

## 📂 Features

- ✅ View existing tasks  
- ➕ Add new tasks  
- ❌ Remove completed/unwanted tasks  
- 💾 Automatically saves tasks to `tasks.txt` on exit  
- ⚠️ Handles missing task file and invalid inputs gracefully  

---

## 🛠️ Requirements

- Python 3.x

---

## ▶️ How to Run

1. Save the code in a Python file, for example: `todo.py`
2. Run it using Python:

```bash
python todo.py
```

---

## 📋 Usage Instructions

Once you run the application, you'll see a menu like this:

* 1 - View Tasks: Displays all current tasks from tasks.txt.
* 2 - Add Task: Prompts the user to input a new task, which is then added to the list.
* 3 - Remove Task: Shows the task list with index numbers. You can enter a number to remove the corresponding task.
* 4 - Exit: Saves all tasks to tasks.txt and exits the program.

---

## 🧾 File Format
* Tasks are saved in a simple text format.
* Each task is stored on a new line in the tasks.txt file.

---

## 💡 Example
```bash
Enter task: Complete Python assignment
Task added.

--- TO-DO LIST ---
1. View Tasks
2. Add Task
3. Remove Task
4. Exit

Choose an option (1-4): 1

Your todo-task list:
0 - Complete Python assignment
```

---

## 📁 tasks.txt Sample
```bash
Buy groceries
Finish project report
Call John
```

---

## 📌 Notes
* The program creates tasks.txt automatically if it doesn’t exist.
* Handles incorrect menu choices and invalid inputs while removing tasks.

---
