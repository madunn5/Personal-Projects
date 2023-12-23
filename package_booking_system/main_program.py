import sys

from generate_quote import Questionnaire
from validation_functions import *
from view_past_quotes import view_past_quotes
from view_current_quotes import view_active_quotes
from air_route_report import view_air_routes
from ocean_route_report import view_ocean_routes
from truck_route_report import view_truck_routes
from dangerous_contents_report import view_dangerous_contents
from unable_to_ship_report import view_unable_to_ship_routes

menu_options = """
    Welcome! Please select one of the options below.

    A. Add a new package quote
    B. View Report of Current Quotes 
    C. View Report of Past Quotes
    D. View Report of Dangerous Contents
    E. View Report of Truck Transports
    F. View Report of Ocean Transports
    G. View Report of Air Transports
    H. View Report of Transports Unable to be Shipped
    Q. Quit Program

    Your choice is: """


def quit():
    print('Goodbye!')
    sys.exit()


questions = [
    {'id': 'customer', 'text': 'Name of customer?: ', 'validators': [validate_not_blank]},
    {'id': 'package_description', 'text': 'What is the package?: ', 'validators': [validate_not_blank]},
    {'id': 'dangerous_contents', 'text': 'Are the content dangerous? [Y/N]: ', 'validators': [validate_yes_or_no]},
    {'id': 'weight', 'text': 'What is the weight of the package? (in KGs): ', 'validators': [validate_number]},
    {'id': 'volume', 'text': 'What is the volume of the package? (in cubic meters): ', 'validators': [validate_number]},
    {'id': 'delivery_date', 'text': 'Required delivery date? (MM/DD/YYYY): ', 'validators': [validate_date]},
    {'id': 'international_destination', 'text': 'Is this an international destination? [Y/N]: ',
     'validators': [validate_yes_or_no]}
]

menu_functions = {
    "a": Questionnaire(questions).generate_quote,
    "b": view_active_quotes,
    "c": view_past_quotes,
    "d": view_dangerous_contents,
    "e": view_truck_routes,
    "f": view_ocean_routes,
    "g": view_air_routes,
    "h": view_unable_to_ship_routes,
    "q": quit
}

if __name__ == '__main__':
    while True:
        menu_selection = input(menu_options).strip().lower()
        if menu_selection in menu_functions.keys():
            menu_functions[menu_selection]()
        else:
            print("Please select a valid option.")
