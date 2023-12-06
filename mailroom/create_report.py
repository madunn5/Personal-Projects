from send_thank_you import read_donor_data


def create_report():
    list_of_donors = read_donor_data()
    print('*' * 50)
    print("Creating Donor Report:")
    print('*' * 50)
    print()
    print("{:<25} | {:<15} | {:<10} | {:<15}".format("Donor Name", "Total Given", "# of Gifts", "Average Gift Amount"))
    print("-" * 80)

    # sort the list_of_donors by total_given in descending order
    sorted_donors = sorted(list_of_donors, key=lambda x: sum(x['total_given']), reverse=True)

    for item in sorted_donors:
        donor_name = item['donor_name']
        num_of_gifts = len(item['total_given'])
        total_given = sum(item['total_given'])
        average_gift = total_given / num_of_gifts
        print("{:<25} | ${:<14,.2f} | {:<10,} | ${:<14,.2f}".format(donor_name, total_given, num_of_gifts,
                                                                    average_gift))
    print()
    print('*' * 50)
    print("Donor Report has been created!")
    print('*' * 50)


if __name__ == '__main__':
    print('Do not run this code from main. Only use as an import.')
