from datetime import datetime


def validate_not_blank(response):
    if response.strip() == '':
        print('Please answer the question.')
        return False
    return True


def validate_number(response):
    try:
        int_value = float(response)
        return True
    except ValueError:
        print('Please enter a numeric amount.')
        return False


def validate_yes_or_no(response):
    if response.lower() not in {'y', 'n'}:
        print('Please enter Y or N.')
        return False
    return True


def validate_date(response):
    try:
        date_object = datetime.strptime(response, '%m/%d/%Y')
        return True
    except ValueError:
        print('Please enter a valid date in MM/DD/YYYY format.')
        return False


if __name__ == '__main__':
    print('Do not run this code from main. Only use as an import.')