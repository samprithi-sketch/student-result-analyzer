# Student-Result-Analyzer

## Description
A console-based student result management system built using Python and SQLite. The application manages student academic records, computes results, assigns grades and generates insightful reports and visual charts.

## Features
- Add new student with marks
- View individual student result
- Search student by ID or name
- Full report showing class summary, topper list and failed students
- Delete student record
- Visual charts showing total marks and grade distribution

## Tech
- Python 3
- SQLite (for database)
- Matplotlib (for charts)
- Git and GitHub (for version control)

## Installation

Step 1 - Make sure Python 3 is installed on your computer
         Download from: https://www.python.org/downloads/

Step 2 - Install required library:
         pip install matplotlib

Step 3 - Clone this repository:
         git clone https://github.com/samprithi-sketch/student-result-analyzer.git

Step 4 - Navigate to project folder:
         cd student-result-analyzer

Step 5 - Run the application:
         python main.py

## Project Structure
- main.py        - starts the application
- database.py    - creates and connects to database
- calculator.py  - calculates total, average and grade
- validator.py   - checks user input
- student.py     - add, view, search, delete student
- reports.py     - class summary, topper list, failed students
- visualizer.py  - shows bar chart and pie chart
- menu.py        - the main menu

## Dependencies
- matplotlib  (install using pip install matplotlib)
- sqlite3     (built into Python, no installation needed)
