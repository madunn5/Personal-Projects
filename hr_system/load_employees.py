import csv


def load_employees(filename='employee_data.csv'):
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []  # return an empty list if the file doesn't exist


if __name__ == '__main__':
    print('Do not run this code from main. Only use as an import.')
