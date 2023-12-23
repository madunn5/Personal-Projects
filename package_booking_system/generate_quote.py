import csv
import uuid
from validation_functions import *
from calculation_functions import calculate_quote


class Questionnaire:
    def __init__(self, questions):
        self.questions = questions
        self.response_dictionary = {}

    def generate_quote(self):
        for question in self.questions:
            # setting unique ID and limiting to 6 characters
            self.response_dictionary['package_id'] = str(uuid.uuid4())[:6]
            while True:
                response = input(question['text'])
                valid_response = self.validate_response(response, question['validators'])

                if valid_response:
                    break

            self.response_dictionary[question['id']] = response.title()

        with open('booking_quotes.csv', 'a', newline='') as csvfile:
            fieldnames = ['package_id', 'customer', 'package_description', 'dangerous_contents',
                          'weight', 'volume', 'delivery_date', 'international_destination', 'route', 'cost']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            # calculate quote and append each quote to its own row
            quote_data = {
                'package_description': self.response_dictionary['package_description'],
                'weight': float(self.response_dictionary['weight']),
                'volume': float(self.response_dictionary['volume']),
                'dangerous_contents': self.response_dictionary['dangerous_contents'] == 'Y',
                'international_destination': self.response_dictionary['international_destination'] == 'Y',
                'delivery_date': datetime.strptime(self.response_dictionary['delivery_date'], '%m/%d/%Y'),
            }

            quote_results = calculate_quote(quote_data)

            # create a set to identify duplicate quotes
            unique_quotes = set()

            for quote_result in quote_results:
                quote_result['package_description'] = self.response_dictionary['package_description']
                quote_result['dangerous_contents'] = self.response_dictionary['dangerous_contents']
                quote_result['weight'] = self.response_dictionary['weight']
                quote_result['volume'] = self.response_dictionary['volume']
                quote_result['delivery_date'] = self.response_dictionary['delivery_date']
                quote_result['international_destination'] = self.response_dictionary['international_destination']
                quote_result['package_id'] = self.response_dictionary['package_id']
                quote_result['customer'] = self.response_dictionary['customer']

                # check for duplicates before appending to the CSV file
                route_cost_tuple = (quote_result['route'], quote_result['cost'])
                if route_cost_tuple not in unique_quotes:
                    unique_quotes.add(route_cost_tuple)
                    writer.writerow(quote_result)

    @staticmethod
    def validate_response(response, validators):
        for validator in validators:
            if not validator(response):
                return False
        return True


if __name__ == '__main__':
    print('Do not run this code from main. Only use as an import.')
