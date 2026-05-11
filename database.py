import sqlite3
def initialize_db():
    conn=sqlite3.connect('student_results.db')
    cursor=conn.cursor()
    cursor.execute('''create table if not exists students(
                    student_id INTEGER PRIMARY KEY,
                    student_name TEXT NOT NULL,
                    class_name TEXT NOT NULL,
                    subject1 INTEGER NOT NULL,
                    subject2 INTEGER NOT NULL,
                    subject3 INTEGER NOT NULL,
                    total INTEGER NOT NULL,
                    average REAL NOT NULL,
                    grade TEXT NOT NULL
                )''')
    conn.commit()
    conn.close()