from datetime import datetime
from load_employees import load_employees


def annual_review_reminder_report():
    list_of_employees = load_employees()
    current_date = datetime.now().date()
    print('*' * 100)
    print(f"Creating Report for Employees Who Have 90 Days Til Their Work Anniversary: Today's Date is {current_date}")
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
        start_date_str = item['start_date']
        end_date_str = item['end_date']

        # skip employees that are no longer employee
        if end_date_str != '':
            continue

        # convert the end_date string to a datetime object
        start_date = datetime.strptime(start_date_str, '%m/%d/%Y').date()

        # calculate the difference in days between the current date and the employee's next work anniversary
        anniversary_this_year = datetime(current_date.year, start_date.month, start_date.day).date()
        anniversary_next_year = datetime(current_date.year + 1, start_date.month, start_date.day).date()

        # if the anniversary for the current year has already passed, use the anniversary for the next year
        # if the start date hasn't happened then they will be left off this report
        if start_date > current_date:
            continue
        elif current_date > anniversary_this_year:
            days_til_work_anniversary = (anniversary_next_year - current_date).days
        else:
            days_til_work_anniversary = (anniversary_this_year - current_date).days

        # check if the employee left within the last 31 days
        if 0 <= days_til_work_anniversary <= 90:
            employee_id = str(item['employee_id'])
            employee_name = str(item['name'])
            address = str(item['address'])
            social_security_number = str(item['ssn'])
            date_of_birth = str(item['date_of_birth'])
            job_title = str(item['job_title'])
            start_date = str(item['start_date'])
            end_date = str(item['end_date'])

            print("{:<11} | {:<25} | {:<50} | {:<10} | {:<15} | {:<25} | {:<15} | {:<15}".format(
                employee_id, employee_name, address, social_security_number, date_of_birth, job_title, start_date,
                end_date))

    print()
    print('*' * 50)
    print("Report has been created!")
    print('*' * 50)


if __name__ == '__main__':
    print('Do not run this code from main. Only use as an import.')
