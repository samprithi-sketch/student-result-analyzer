import sqlite3
from validator import *
from calculator import *
from database import *

def add_student():
    student_id = input("Enter Student ID: ")
    if not is_valid_id(student_id):
        return
    
    conn = sqlite3.connect('student_results.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        print("Student ID already exists! Please use a different ID.")
        return
    
    student_name = input("Enter Student Name: ")
    if not is_valid_name(student_name):
        return

    class_name = input("Enter Class Name: ")
    if not is_valid_class(class_name):
        return

    marks = []
    for subject in subject_names:
        mark = input(f"Enter {subject} Mark: ")
        if not is_valid_mark(mark, subject):
            return
        marks.append(int(mark.strip()))

    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = assign_grade(average)

    conn = sqlite3.connect('student_results.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO students (student_id, student_name, class_name, subject1, subject2, subject3, total, average, grade)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (int(student_id), student_name, class_name, marks[0], marks[1], marks[2], total, average, grade))
    conn.commit()
    conn.close()
    print("Student added successfully!")
    print(f"\nTotal: {total} \nAverage: {average} \nGrade: {grade}")

def view_all_students():
    conn = sqlite3.connect('student_results.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("No students found.")
        return

    print("\n")
    print("ID\tName\t\tClass\tMath\tPhysics\tEnglish\tTotal\tAverage\tGrade")
    print("-" * 75)
    for row in rows:
        print(f"{row[0]}\t{row[1]}\t\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\t{row[6]}\t{row[7]}\t{row[8]}")

def search_student(student_id):
    if not is_valid_id(student_id):
        return

    conn = sqlite3.connect('student_results.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students WHERE student_id = ?', (int(student_id),))
    row = cursor.fetchone()
    conn.close()

    if row:
        print("ID\tName\t\tClass\tMath\tPhysics\tEnglish\tTotal\tAverage\tGrade")
        print("-" * 75)
        print(f"{row[0]}\t{row[1]}\t\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\t{row[6]}\t{row[7]}\t{row[8]}")
    else:
        print("Student not found.")

def delete_student(student_id):
    if not is_valid_id(student_id):
        return

    conn = sqlite3.connect('student_results.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM students WHERE student_id = ?', (int(student_id),))
    deleted_rows = cursor.rowcount
    conn.commit()
    conn.close()
    if deleted_rows > 0:
        print("Student deleted successfully!")
    else:
        print("Student not found.")
