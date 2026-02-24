from datetime import datetime
# Import validation functions from the validation module
from .validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list to store task dictionaries
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    # Validate all inputs before creating the task
    try:
        validate_task_title(title)
        validate_task_description(description)
        validate_due_date(due_date)
    except ValueError as e:
        print(f"Failed to add task: {e}")
        return

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")

# Implement mark_task_as_complete function
def mark_task_as_complete(index):
    try:
        # Convert 1-based user input to 0-based index
        if index < 1 or index > len(tasks):
            raise ValueError("Task number out of range.")
        tasks[index - 1]["completed"] = True
        print("Task marked as complete!")
    except (IndexError, ValueError):
        print("Invalid task number.")

# Implement view_pending_tasks function
def view_pending_tasks():
    pending = [t for t in tasks if not t["completed"]]
    if len(pending) == 0:
        print("No pending tasks.")
    else:
        for i, task in enumerate(tasks, 1):
            if not task["completed"]:
                print(f"{i}. {task['title']} - Due: {task['due_date']}")

# Implement calculate_progress function
def calculate_progress(tasks=None):
    import task_manager.task_utils as _mod
    target = tasks if tasks is not None else _mod.tasks
    if len(target) == 0:
        return 0.0
    completed = sum(1 for t in target if t["completed"])
    progress = (completed / len(target)) * 100
    return progress
