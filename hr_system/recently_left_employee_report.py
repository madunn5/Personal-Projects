from datetime import datetime
from load_employees import load_employees


def recently_left_employee_report():
    list_of_employees = load_employees()
    current_date = datetime.now().date()
    print('*' * 100)
    print(f"Creating Report for Employees Who Have Left Within the Last 31 Days: Today's Date is {current_date}")
    print('*' * 100)
    print()
    print("{:<11} | {:<25} | {:<50} | {:<10} | {:<15} | {:<25} | {:<15} | {:<15}".format("Employee ID",
                                                                                         "Employee Name",
                                                                                         "Address", "SSN",
                                                                                         "Date of Birth",
                                                                                         "Job Title", "Start Date",
                                                                                         "End Date"))
    print("-" * 175)

    # sort the employees by employee id in ascending order
    sorted_employees = sorted(list_of_employees, key=lambda x: int(x.get('employee_id', 0)))

    for item in sorted_employees:
        end_date_str = item['end_date']

        # skip employees with no end date
        if end_date_str is None or end_date_str == '':
            continue

        # convert the end_date string to a datetime object
        end_date = datetime.strptime(end_date_str, '%m/%d/%Y').date()

        # calculate the difference in days between the current date and the employee's end_date
        days_since_departure = (current_date - end_date).days

        # check if the employee left within the last 31 days
        if 0 <= days_since_departure <= 31:
            employee_id = str(item['employee_id'])
            employee_name = str(item['name'])
            address = str(item['address'])
            social_security_number = str(item['ssn'])
            date_of_birth = str(item['date_of_birth'])
            job_title = str(item['job_title'])
            start_date = str(item['start_date'])
            end_date = str(end_date_str)

            print("{:<11} | {:<25} | {:<50} | {:<10} | {:<15} | {:<25} | {:<15} | {:<15}".format(
                employee_id, employee_name, address, social_security_number, date_of_birth, job_title, start_date,
                end_date))

    print()
    print('*' * 50)
    print("Report has been created!")
    print('*' * 50)


if __name__ == '__main__':
    print('Do not run this code from main. Only use as an import.')
