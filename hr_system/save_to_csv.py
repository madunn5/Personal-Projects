import csv


def save_to_csv(old_filename='employee_data.csv'):
    try:
        while True:
            new_filename = str(input("What is the unique name of the file you would like to use? ") + '.csv')

            if new_filename == old_filename:
                print('Please choose a different name other than', old_filename)
            else:
                try:
                    with open(old_filename, 'r') as file:
                        reader = csv.DictReader(file)
                        data = list(reader)

                    with open(new_filename, 'w', newline='') as file:
                        fieldnames = ['employee_id', 'name', 'address', 'ssn', 'date_of_birth', 'job_title',
                                      'start_date', 'end_date']
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(data)

                    print(f'Data has been saved to {new_filename}')
                    break  # exit the loop if the data is successfully saved
                except FileNotFoundError:
                    print(f'Error: File {old_filename} not found.')
                    return []
    except Exception as e:
        print(f'Error: {e}')
        return []


if __name__ == '__main__':
    print('Do not run this code from main. Only use as an import.')
