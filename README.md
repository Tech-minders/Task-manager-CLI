Task Management System

```
A lightweight command-line task manager built in Python. It lets you add tasks, mark them complete, view what's pending, and track your overall progress — all from an interactive menu.

Project Structure
Task Management System/
├── main.py                        # Entry point — runs the interactive menu
└── task_manager/
    ├── __init__.py                # Package exports
    ├── task_utils.py              # Core task logic (add, complete, view, progress)
    └── validation.py              # Input validation with error handling

Getting Started
Requirements: Python 3.7+, no external dependencies.
bashpython main.py
You'll be presented with a menu:
Task Management System
1. Add Task
2. Mark Task as Complete
3. View Pending Tasks
4. View Progress
5. Exit

Features
1. Add a Task
Enter a title, description, and due date (YYYY-MM-DD format). All inputs are validated before the task is saved.
2. Mark Task as Complete
Displays your pending tasks, then prompts for the task number to mark as done.
3. View Pending Tasks
Lists all tasks that have not yet been completed, showing their title and due date.
4. View Progress
Calculates and displays the percentage of tasks completed so far.
5. Exit
Exits the program.

Module Reference
task_manager/validation.py
FunctionDescriptionvalidate_task_title(title)Raises ValueError if title is empty or not a stringvalidate_task_description(description)Raises ValueError if not a string or exceeds 500 charactersvalidate_due_date(due_date)Raises ValueError if date is not in YYYY-MM-DD format
task_manager/task_utils.py
FunctionDescriptionadd_task(title, description, due_date)Validates inputs and appends a new task to the listmark_task_as_complete(index)Marks the task at the given 1-based index as completeview_pending_tasks()Prints all incomplete tasks with their due datescalculate_progress(tasks=None)Returns completion percentage; accepts an optional task list

Validation Rules

Title — must be a non-empty string (whitespace-only titles are rejected)
Description — must be a string, maximum 500 characters
Due Date — must follow YYYY-MM-DD format exactly

All validation failures raise a ValueError with a descriptive message.

Example Usage
pythonfrom task_manager.task_utils import add_task, mark_task_as_complete, calculate_progress

add_task("Buy groceries", "Milk and eggs", "2025-06-01")
add_task("Read book", "Finish chapter 3", "2025-06-10")

mark_task_as_complete(1)

progress = calculate_progress()
print(f"Progress: {progress:.2f}%")  # Progress: 50.00%
You can also pass a task list directly to calculate_progress:
pythontasks = [
    {"title": "Task 1", "description": "test", "due_date": "2024-05-26", "completed": True},
    {"title": "Task 2", "description": "test", "due_date": "2024-05-26", "completed": False},
]
calculate_progress(tasks)  # Returns 50.0

```
