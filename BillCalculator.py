# Author: Joshua Wiley
# Title:  Electric Bill Calculator

# Check if the beginning of the month reading is
# greater then the second reading


def valid_reading(first_reading, second_reading):
    while first_reading >= second_reading:
        print("First input cannot be the same as the second!\n")
        first_reading = float(input("Enter Your Beginning of Month KwH Used: "))
        second_reading = float(input("Enter Your End of Month KwH Used: "))

    return True, first_reading, second_reading


# Calculate the Monthly bill
def calculate_bill(firstReading, secondReading):
    # RATE1, RATE2, RATE3 = 0.08, 0.11, 0.15

    kwh = float(secondReading - firstReading)

    if kwh < 500:
        rate = 0.08
    elif kwh <= 500 or kwh < 1500:
        rate = 0.11
    elif kwh >= 1500:
        kwh = 0.15
    else:
        rate = 0.20

    bill = rate * kwh

    return bill

with open('commands.txt', 'r') as f:
    LINES = f.read().splitlines()


def get_info(oneline, line_num):
    line = oneline[line_num]
    return line.split(' | ')

# Main
LIST_CUSTOMERS = {}
while True:
    print("\nN/n = New User")
    print("L/l = Lookup User")
    print("D/d = Delete User")
    print("U/u = Update User")
    print("A/a = Add New Bill")
    print("E/e = Exit\n")


    for x in range(0, len(LINES)):
        COMMANDINPUT, ID, VALUE1, VALUE2 = get_info(LINES, x)

        print(COMMANDINPUT)

        if COMMANDINPUT in 'n' or COMMANDINPUT in 'N':
            customerID = ID
            fRead = float(VALUE1)
            sRead = float(VALUE2)

            # Return values
            valid, fRead, sRead = valid_reading(fRead, sRead)

            if valid is True:
                balance = float(calculate_bill(fRead, sRead))
                print("Your user %s balance is $%.2f." % (ID, balance))
            LIST_CUSTOMERS[customerID] = balance
        elif COMMANDINPUT in 'l' or COMMANDINPUT in 'L':
            customerID = ID
            if customerID not in LIST_CUSTOMERS:
                print("\nThe Customer ID %s is not in the database."
                      % customerID)
            else:
                print('%s your balance is %.2f' % (ID, LIST_CUSTOMERS[customerID]))
        elif COMMANDINPUT in 'd' or COMMANDINPUT in 'D':
            customerID = ID
            del LIST_CUSTOMERS[customerID]
            print("Customer %s has been removed from the database."
                  % customerID)
        elif COMMANDINPUT in 'u' or COMMANDINPUT in 'U':
            # Enter current
            customerID = ID
            # Create a temp ID to store original ID
            temp = customerID
            # Get new ID
            customerID = VALUE1
            # Set the new ID with the old ID's value
            LIST_CUSTOMERS[customerID] = LIST_CUSTOMERS[temp]
            # Delete the old ID
            del LIST_CUSTOMERS[temp]
            print("Customer ID %s has been updated to %s."
                  % (temp, customerID))
        elif COMMANDINPUT in 'a' or COMMANDINPUT in 'A':
            fRead = float(VALUE1)
            sRead = float(VALUE2)

            # Return values
            if valid is True:
                balance = calculate_bill(fRead, sRead)
                print("Your user %s balance is $%.2f." % (ID, balance))
            LIST_CUSTOMERS[ID] = balance
        elif COMMANDINPUT in 'e' or COMMANDINPUT in 'E':
            f.close()
            exit()
