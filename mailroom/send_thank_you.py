def read_donor_data(filename='list_of_donors.csv'):
    list_of_donors = []  # initialize an empty list to store the data
    try:
        with open(filename, 'r') as file:
            header = next(file)  # this skips the first line of the file since that is the header
            for line in file:
                parts = line.strip().split(",")
                donor_name = parts[0]
                total_given = parts[1:]
                total_given_float = [float(string) for string in total_given]
                row = {"donor_name": donor_name.strip(),
                       "total_given": total_given_float}
                list_of_donors.append(row)
    except FileNotFoundError:
        print(f"File '{filename}' not found. A new file will be created once donor data has been added.")
    except Exception as e:
        print(f'ERROR: {e}')
    return list_of_donors


def choose_donor(filename='list_of_donors.csv'):
    list_of_donors = read_donor_data()
    donor_found = False  # setting a flag for when we find if the donor exists or not. Setting to False by default
    while True:
        menu_options = input("""
Please input the name of the donor you'd like to send the thank you to. 
If you'd like to see a list of donors, please type list. 
If the donor is not already in the list please type their name here. """)
        if menu_options.strip():
            if menu_options.lower() == 'list':
                print('*' * 40)
                print(f"Donor Name, Total Given in $, Number of Gifts")
                for item in list_of_donors:
                    print(f"{item['donor_name']}, {sum(item['total_given']):,.2f}, {len(item['total_given']):,}")
                print('*' * 40)
                donor_selection = input(f"What is the name of the donor you'd like to thank? ").title()
                while not donor_selection.strip():
                    print('Please provide a valid response.')
                    donor_selection = input(f"What is the name of the donor you'd like to thank? ").title()
                break
            elif menu_options.lower() != 'list':
                donor_selection = menu_options.title()
                break
        else:
            print('\nPlease answer the question. Your last response was blank.')

    for item in list_of_donors:
        if item['donor_name'] == donor_selection:
            donor_found = True
            num_of_gifts = len(item['total_given'])
            total_given = sum(item['total_given'])
            # ask if an additional donation was made
            while True:
                additional_donation = input(f"Has {donor_selection} made an additional donation? (Y/N) ")
                if additional_donation.lower() == 'y':
                    while True:
                        try:
                            additional_amount_str = input(f"How much was the additional donation? ")
                            if additional_amount_str:  # check if the input is not empty
                                additional_amount = float(additional_amount_str)
                                item['total_given'].append(additional_amount)
                                total_given += additional_amount
                                num_of_gifts += 1
                                # update the CSV file with the new donation information
                                with open(filename, 'w', newline='') as file:
                                    file.write('donor_name,total_given\n')
                                    for row in list_of_donors:
                                        # removes brackets
                                        total_given_str = str(row['total_given']).replace('[', '').replace(']', '')
                                        file.write(f"{row['donor_name']},{total_given_str}\n")
                                break
                            else:
                                print("Please provide a valid amount.")
                        except ValueError:
                            print('Please enter a valid numerical input.')
                    break
                elif additional_donation.lower() == 'n':
                    break
                else:
                    print('Please respond with Y or N.')

    if donor_found:
        print(f"\n{donor_selection} has contributed {num_of_gifts:,} gifts for a total of ${total_given:,.2f}.")
        print()
        print('*' * 11, 'Generating email thank you', '*' * 11)
        print(f"""
Dear {donor_selection},
    On behalf of the Ballard Foundation I'd like to sincerely thank you for generous donation of ${total_given:,.2f}. We
greatly appreciate your generosity, and a tax receipt will be sent to you at the end of the year for your {num_of_gifts:,}
gifts given to the Foundation. We thank you again for your generosity.
Sincerely,
Matt Dunn, CEO
Ballard Foundation""")
        print()
        print('*' * 50)
    else:
        while True:
            answer = input(f'This donor is not in the current data. Would you like to add them to the list? (Y/N) ')
            if answer.lower() == 'y':
                while True:
                    total_given_str = input(f"How much money did {donor_selection} contribute? ").strip()
                    if total_given_str:
                        try:
                            total_given = float(total_given_str)
                            if total_given >= 0:  # Ensure that the input is a non-negative number
                                print(
                                    f'Ok, {donor_selection} will be added to the data. They have contributed {total_given:,.2f} on '
                                    f'a total of 1 gifts.')
                                row = {"donor_name": str(donor_selection).strip(),
                                       "total_given": total_given}
                                list_of_donors.append(row)
                                with open(filename, 'w', newline='') as file:
                                    file.write('donor_name,total_given\n')
                                    for row in list_of_donors:
                                        # removes brackets
                                        total_given_str = str(row['total_given']).replace('[', '').replace(']', '')
                                        file.write(f"{row['donor_name']},{total_given_str}\n")
                                print()  # add an extra line for looks
                                print(f"Donation data for {donor_selection} has been saved to the file '{filename}'!\n")
                                print('*' * 11, 'Generating email thank you', '*' * 11)
                                print(f"""
Dear {donor_selection},
    On behalf of the Ballard Foundation I'd like to sincerely thank you for generous donation of ${total_given:,.2f}. 
We greatly appreciate your generosity, and a tax receipt will be sent to you at the end of the year for your 1 gift 
given to the Foundation. We thank you again for your generosity. 
Sincerely, 
Matt Dunn, 
CEO Ballard Foundation""")
                                print()
                                print('*' * 50)
                                break
                            else:
                                print('Please enter a valid non-negative amount.')
                        except ValueError:
                            print('Please enter a valid numerical input.')
                    else:
                        print('Please enter a valid input.')
                break
            elif answer.lower() == 'n':
                print(f'OK, {donor_selection} will not be added to the data.')
                break
            else:
                print('Please answer Y or N.')


def send_thank_you():
    choose_donor()


if __name__ == '__main__':
    print('Do not run this code from main. Only use as an import.')
