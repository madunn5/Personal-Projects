import csv
from datetime import datetime
from load_employees import load_employees


def add_new_employee(filename='employee_data.csv'):
    try:
        employee_data = load_employees(filename)
        unique_employee_ids = set()
        for row in employee_data:
            unique_employee_ids.add(int(row['employee_id']))
        new_employee_id = max(unique_employee_ids) + 1 if unique_employee_ids else 1

        while True:
            employee_name = input("What is the name of the employee you'd like to add? ").title()
            if not employee_name.strip():
                print('Employee name cannot be blank. Please provide a valid employee name.')
            elif all(x.isalpha() or x.isspace() for x in employee_name):
                break
            else:
                print('Please format the name correctly. Numbers or special characters are not allowed.')

        while True:
            address = input("What is the employee's address? ")
            if not address.strip():
                print('Address cannot be blank. Please provide a valid address.')
            elif all(x.isalnum() or x.isspace() or x in ('.', ',') for x in address):
                break
            else:
                print('Please input a properly formatted address.')

        while True:
            social_security_number = input("What is the employee's social security number? ")
            if not social_security_number.strip():
                print('Social security number cannot be blank. Please provide a valid social security number.')
            elif social_security_number.isnumeric() and len(social_security_number) == 9:
                break
            else:
                print('Please input a correctly formatted social security number.')

        while True:
            try:
                date_of_birth = input("What is the employee's date of birth? (MM/DD/YYYY) ")
                datetime.strptime(date_of_birth, '%m/%d/%Y')
                break  # Exit loop if the date format is valid
            except ValueError:
                print("Invalid date format. Please enter the date in the format MM/DD/YYYY.")

        while True:
            job_title = input("What is the employee's job title? ").title()
            if not job_title.strip():
                print('Job title cannot be blank. Please provide a valid job title.')
            elif all(x.isalpha() or x.isspace() for x in job_title):
                break
            else:
                print('Please format the job title correctly.')

        while True:
            try:
                start_date = input("What was the employee's start date? (MM/DD/YYYY) ")
                datetime.strptime(start_date, '%m/%d/%Y')
                break  # exit loop if the date format is valid
            except ValueError:
                print("Invalid date format. Please enter the date in the format MM/DD/YYYY.")

        while True:
            end_date_input = input("Enter the employee's termination date, or leave it blank if still employed ("
                                   "MM/DD/YYYY): ")
            if not end_date_input.strip():  # check if the input is blank
                break  # exit loop if the input is blank
            try:
                datetime.strptime(end_date_input, '%m/%d/%Y')
                break  # exit loop if the date format is valid
            except ValueError:
                print("Invalid date format. Please enter the date in the format MM/DD/YYYY.")

        row = {"employee_id": str(new_employee_id),
               "employee_name": employee_name.strip(),
               "address": address.strip(),
               "social_security_number": social_security_number.strip(),
               "date_of_birth": date_of_birth.strip(),
               "job_title": job_title.strip(),
               "start_date": start_date.strip(),
               "end_date": end_date_input}

        with open(filename, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=row.keys())
            if file.tell() == 0:  # check if the file is empty, write header if needed
                writer.writeheader()
            writer.writerow(row)

        print(f"{employee_name} has been added to the file.")
    except Exception as e:
        print(f'ERROR: {e}')


if __name__ == '__main__':
    print('Do not run this code from main. Only use as an import.')
