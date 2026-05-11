print("Welcome to Student Result Analyzer")
print("This project is built by: SAMPRITHI")


from database import initialize_db
from menu import show_menu

initialize_db()
show_menu()

