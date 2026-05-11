def is_valid_id(sid):
    if not sid.strip():
        print("Student ID cannot be empty.")
        return False
    if not sid.strip().isalnum():
        print("Student ID must be alphanumeric.")
        return False
    return True
def is_valid_name(name):
    if not name.strip():
        print("Student name cannot be empty.")
        return False
    if any(ch.isdigit() for ch in name):
        print("Name should not contain numbers.")
        return False
    return True
def is_valid_class(class_name):
    if not class_name.strip():
        print("Class name cannot be empty.")
        return False
    return True
def is_valid_mark(mark,subject):
    if not mark.strip():
        print(f"{subject} mark cannot be empty.")
        return False
    if not mark.strip().isdigit():
        print(f"{subject} mark must be a number.")
        return False
    mark_value = int(mark.strip())
    if mark_value < 0 or mark_value > 100:
        print(f"{subject} mark must be between 0 and 100.")
        return False
    return True