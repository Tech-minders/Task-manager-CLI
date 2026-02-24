from datetime import datetime

def validate_task_title(title):
    # Check if title is a non-empty string using len()
    if not isinstance(title, str):
        raise ValueError("Title must be a string.")
    if len(title.strip()) == 0:
        raise ValueError("Title cannot be empty or whitespace.")
    return True

def validate_task_description(description):
    # Ensure description is a string and within length limits
    if not isinstance(description, str):
        raise ValueError("Description must be a string.")
    if len(description) > 500:
        raise ValueError("Description cannot exceed 500 characters.")
    return True

def validate_due_date(due_date):
    # Parse date string to ensure it matches YYYY-MM-DD format
    try:
        datetime.strptime(due_date, '%Y-%m-%d')
        return True
    except (ValueError, TypeError):
        raise ValueError("Due date must be in YYYY-MM-DD format.")
