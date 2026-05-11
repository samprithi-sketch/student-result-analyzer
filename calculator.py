subject_names = ["Mathematics", "Physics", "English"]
def calculate_total(marks):
    return sum(marks)
def calculate_average(marks):
    return round(sum(marks) / len(marks))
def assign_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    elif average >= 40:
        return 'E'
    else:
        return 'F'