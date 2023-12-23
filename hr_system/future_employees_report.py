from datetime import datetime
from load_employees import load_employees


def future_employees_report():
    list_of_employees = load_employees()
    current_date = datetime.now().date()
    print('*' * 50)
    print("Creating Future Employee Report:")
    print('*' * 50)
    print()
    print("{:<11} | {:<25} | {:<50} | {:<10} | {:<15} | {:<25} | {:<15} | {:<15}".format("Employee ID", "Employee Name",
                                                                                         "Address", "SSN",
                                                                                         "Date of Birth",
                                                                                         "Job Title", "Start Date",
                                                                                         "End Date"))
    print("-" * 175)

    # sort the employees by employee id in ascending order
    sorted_employees = sorted(list_of_employees, key=lambda x: int(x.get('employee_id', 0)))

    for item in sorted_employees:
        end_date_str = item['end_date']
        start_date_str = item['start_date']

        # skip employees with no end date
        if end_date_str != '':
            continue

        # convert the start_date string to a datetime object
        start_date = datetime.strptime(start_date_str, '%m/%d/%Y').date()

        # only include future employees with start dates that haven't happened
        if start_date > current_date:
            employee_id = item['employee_id']
            employee_name = item['name']
            address = item['address']
            social_security_number = item['ssn']
            date_of_birth = item['date_of_birth']
            job_title = item['job_title']
            start_date = item['start_date']
            end_date = item['end_date']

            # handle None values
            employee_id = str(employee_id) if employee_id is not None else ''
            employee_name = str(employee_name) if employee_name is not None else ''
            address = str(address) if address is not None else ''
            social_security_number = str(social_security_number) if social_security_number is not None else ''
            date_of_birth = str(date_of_birth) if date_of_birth is not None else ''
            job_title = str(job_title) if job_title is not None else ''
            start_date = str(start_date) if start_date is not None else ''
            end_date = str(end_date) if end_date is not None else ''

            print("{:<11} | {:<25} | {:<50} | {:<10} | {:<15} | {:<25} | {:<15} | {:<15}".format(
                employee_id, employee_name, address, social_security_number, date_of_birth, job_title, start_date,
                end_date))
    print()
    print('*' * 50)
    print("Employee Report has been created!")
    print('*' * 50)


if __name__ == '__main__':
    print('Do not run this code from main. Only use as an import.')
