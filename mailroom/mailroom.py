import sys

from create_report import create_report
from send_thank_you import send_thank_you

menu_options = """
    Welcome! Please select one of the options below.
    
    A. Send a Thank You
    B. Create Report
    Q. Quit Program

    Your choice is: """


def quit():
    print('Goodbye!')
    sys.exit()


menu_functions = {
    "a": send_thank_you,
    "b": create_report,
    "q": quit
}

if __name__ == '__main__':
    while True:
        menu_selection = input(menu_options).strip().lower()
        if menu_selection in menu_functions.keys():
            menu_functions[menu_selection]()
        else:
            print("Please select a valid option.")
