from student import add_student, view_all_students, search_student, delete_student
from reports import show_full_report

def show_menu():
    while True:
        print("\n--------------------------------")
        print("   STUDENT RESULT ANALYZER")
        print("----------------------------------")
        print("  1. Add New Student")
        print("  2. View Student Result")
        print("  3. Search Student")
        print("  ------------------------------")
        print("  4. Full Report")
        print("  ------------------------------")
        print("  5. Delete Student")
        print("  0. Exit")
        print("--------------------------------")

        choice = input("  Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_all_students()
        elif choice == "3":
            student_id = input("  Enter Student ID to search: ")
            search_student(student_id)
        elif choice == "4":
            show_full_report()
        elif choice == "5":
            student_id = input("  Enter Student ID to delete: ")
            delete_student(student_id)
        elif choice == "0":
            print("\n  Exiting...")
            break
        else:
            print("Invalid choice.")

        input("\n  Press Enter to continue...")