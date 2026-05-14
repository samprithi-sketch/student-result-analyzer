import sqlite3
def show_class_summary():
    conn=sqlite3.connect('student_results.db')
    cursor=conn.cursor()
    cursor.execute('select * from students')
    rows=cursor.fetchall()
    conn.close()
    if not rows:
        print("No student records found.")
        return
    total_students=len(rows)
    passed = 0
    failed = 0
    total_average = 0

    for row in rows:
        total_average += row[7]
        if row[8] == 'F':
            failed += 1
        else:
            passed += 1

    student_average = round(total_average / total_students)

    print(f"  Total Students : {total_students}")
    print(f"  Passed         : {passed}")
    print(f"  Failed         : {failed}")
    print(f"  Student Average  : {student_average}%")

def show_topper_list():
    print("\n--- Topper List ---")

    conn = sqlite3.connect('student_results.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students ORDER BY total DESC LIMIT 5")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("  No students found.")
        return

    rank = 1
    for row in rows:
        print(f"  #{rank} {row[1]} | Class: {row[2]} | Total: {row[6]} | Grade: {row[8]}")
        rank = rank + 1


def show_failed_students():
    print("\n--- Failed Students ---")

    conn = sqlite3.connect('student_results.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE grade = 'F'")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("  No students have failed!")
        return

    for row in rows:
        print(f"  {row[0]} | {row[1]} | Class: {row[2]} | Average: {row[7]}%")


def show_full_report():
    print("\n---------- FULL REPORT ----------")
    show_class_summary()
    print()
    show_topper_list()
    print()
    show_failed_students()
    print("\n---------------------------------")