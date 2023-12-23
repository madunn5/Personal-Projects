from datetime import datetime, timedelta


def calculate_quote(quote_data):
    weight_limit = 10  # in kilograms
    volume_limit = 125  # in cubic meters

    if quote_data['weight'] < weight_limit and quote_data['volume'] < volume_limit:
        route_options = []

        if quote_data['dangerous_contents']:
            route_options.append({'route': 'Truck' if not quote_data['international_destination'] else 'Ocean'})
        else:
            route_options.append({'route': 'Air'})

        route_options.append({'route': 'Truck' if not quote_data['international_destination'] else 'Ocean'})

        if (weight_limit - 2 <= quote_data['weight'] <= weight_limit) or (
                volume_limit - 5 <= quote_data['volume'] <= volume_limit):
            route_options.append({'route': 'Truck' if not quote_data['international_destination'] else 'Ocean'})

        if not route_options:
            print("No suitable shipping options found for this package.")
            route = 'Not Able to Be Shipped'
            cost = 0
            return [{'route': route, 'cost': cost}]
        else:
            # Calculate cost for each option
            for option in route_options:
                option['cost'] = calculate_cost(option['route'], quote_data)

            print(f"\nShipping Options for {quote_data['package_description']}:")

            unique_quotes = set()

            for option in route_options:
                route_cost_tuple = (option['route'], option['cost'])
                if route_cost_tuple not in unique_quotes:
                    unique_quotes.add(route_cost_tuple)
                    print(f"Route: {option['route']}, Cost: ${option['cost']}")

            return route_options
    else:
        print("This package cannot be shipped due to size or weight constraints.")
        route = 'Not Able to Be Shipped'
        cost = 0
        return [{'route': route, 'cost': cost}]


def calculate_cost(route, quote_data):
    if route == 'Air':  # Air shipments cost $10 per kilogram or $20 per cubic meter, whichever is larger
        return max(10 * quote_data['weight'], 20 * quote_data['volume'])
    elif route == 'Truck':  # Truck shipments cost a flat rate of $25, or $45 if urgent.
        return 45 if (datetime.now() + timedelta(days=3)) >= quote_data['delivery_date'] else 25
    elif route == 'Ocean':  # Ocean shipments costs a flat rate of $30
        return 30
    else:
        return 0


if __name__ == '__main__':
    print('Do not run this code from main. Only use as an import.')
