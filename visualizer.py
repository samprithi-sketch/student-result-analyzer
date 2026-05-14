import sqlite3
import matplotlib.pyplot as plt

def show_charts():
    conn = sqlite3.connect('student_results.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("No students found.")
        return

    # collect data
    names = []
    totals = []
    grades = []

    for row in rows:
        names.append(row[1])
        totals.append(row[6])
        grades.append(row[8])

    # Chart 1 - Bar chart (total marks of each student)
    plt.figure(figsize=(8, 5))
    plt.bar(names, totals, color='blue')
    plt.title("Total Marks of Each Student")
    plt.xlabel("Student Name")
    plt.ylabel("Total Marks")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Chart 2 - Pie chart (grade distribution)
    grade_counts = {}
    for grade in grades:
        if grade in grade_counts:
            grade_counts[grade] = grade_counts[grade] + 1
        else:
            grade_counts[grade] = 1

    plt.figure(figsize=(6, 6))
    plt.pie(grade_counts.values(), labels=grade_counts.keys(), autopct='%1.1f%%')
    plt.title("Grade Distribution")
    plt.show()

