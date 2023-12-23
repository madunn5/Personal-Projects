import csv


def view_ocean_routes():
    print('*' * 50)
    print("Creating Report of All Ocean Transport Routes:")
    print('*' * 50)
    print()
    print("{:<11} | {:<25} | {:<30} | {:<20} | {:<15} | {:<21} | {:<15} | {:<15} | {:<9}".format('Package ID',
                                                                                                 'Customer',
                                                                                                 'Package Description',
                                                                                                 'Dangerous Contents',
                                                                                                 'Weight (KGs)',
                                                                                                 'Volume (Cubic '
                                                                                                 'Meters)',
                                                                                                 'Delivery Date',
                                                                                                 'Route', 'Cost'))
    print("-" * 200)

    try:
        with open('booking_quotes.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                route = row['route']
                if route == 'Ocean':
                    package_id = row['package_id']
                    customer = row['customer']
                    package_description = row['package_description']
                    dangerous_contents = row['dangerous_contents']
                    weight = row['weight']
                    volume = row['volume']
                    delivery_date = row['delivery_date']
                    route = row['route']
                    cost = row['cost']

                    # handle None values
                    package_id = str(package_id) if package_id is not None else ''
                    customer = str(customer) if customer is not None else ''
                    package_description = str(package_description) if package_description is not None else ''
                    dangerous_contents = str(dangerous_contents) if dangerous_contents is not None else ''
                    weight = str(weight) if weight is not None else ''
                    volume = str(volume) if volume is not None else ''
                    delivery_date = str(delivery_date) if delivery_date is not None else ''
                    route = str(route) if route is not None else ''
                    cost = str(cost) if cost is not None else ''

                    print("{:<11} | {:<25} | {:<30} | {:<20} | {:<15} | {:<21} | {:<15} | {:<15} | {:<9}".format(
                        package_id, customer, package_description, dangerous_contents, weight, volume, delivery_date,
                        route, cost))

    except FileNotFoundError:
        print('No current file saved.')

    print()
    print('*' * 50)
    print("Ocean Transport Report has been created!")
    print('*' * 50)


if __name__ == '__main__':
    print('Do not run this code from main. Only use as an import.')
