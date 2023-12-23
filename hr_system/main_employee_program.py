import sys

from load_employees import load_employees
from save_to_csv import save_to_csv
from add_new_employee import add_new_employee
from current_employees_report import current_employees_report
from recently_left_employee_report import recently_left_employee_report
from annual_review_reminder_report import annual_review_reminder_report
from future_employees_report import future_employees_report

menu_options = """
    Welcome! Please select one of the options below.
    
    A. Load employees in from a csv 
    B. Save the current data into a csv with a unique filename 
    C. Add a new employee 
    D. Generate a report of current employees 
    E. Generate a report of employees who have recently left
    F. Generate a report of annual review reminder
    G. Generate a report future employees whose start dates haven't happened yet
    Q. Quit Program

    Your choice is: """


def quit():
    print('Goodbye!')
    sys.exit()


menu_functions = {
    "a": load_employees,
    "b": save_to_csv,
    "c": add_new_employee,
    "d": current_employees_report,
    "e": recently_left_employee_report,
    "f": annual_review_reminder_report,
    "g": future_employees_report,
    "q": quit
}

if __name__ == '__main__':
    while True:
        menu_selection = input(menu_options).strip().lower()
        if menu_selection in menu_functions.keys():
            menu_functions[menu_selection]()
        else:
            print("Please select a valid option.")
