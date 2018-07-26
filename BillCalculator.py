# Author: Joshua Wiley
# Title:  Electric Bill Calculator

# Check if the beginning of the month reading is
# greater then the second reading


def validReading(FirstReading, SecondReading):
    while FirstReading >= SecondReading:
        print("First input cannot be the same as the second!\n")
        FirstReading = float(input("Enter Your Beginning of Month KwH Used: "))
        SecondReading = float(input("Enter Your End of Month KwH Used: "))

    return True, FirstReading, SecondReading


# Calculate the Monthly bill
def calculateBill(firstReading, secondReading):
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
    lines = f.read().splitlines()


def get_info(lines, line_num):
    line = lines[line_num]
    return line.split(' | ')

# Main
list_customers = {}
while True:
    print("\nN/n = New User")
    print("L/l = Lookup User")
    print("D/d = Delete User")
    print("U/u = Update User")
    print("A/a = Add New Bill")
    print("E/e = Exit\n")

    x = len(lines)
    for x in range(0, x):
        COMMANDINPUT, ID, VALUE1, VALUE2 = get_info(lines, x)

        print(COMMANDINPUT)
        print(list_customers)

        if COMMANDINPUT in 'n' or COMMANDINPUT in 'N':
            customerID = ID
            fRead = float(VALUE1)
            sRead = float(VALUE2)

            # Return values
            valid, fRead, sRead = validReading(fRead, sRead)

            if valid is True:
                balance = float(calculateBill(fRead, sRead))
                print("Your user %s balance is $%.2f." % (ID, balance))
            list_customers[customerID] = balance
        elif COMMANDINPUT in 'l' or COMMANDINPUT in 'L':
            customerID = ID
            if customerID not in list_customers:
                print("\nThe Customer ID %s is not in the database."
                      % customerID)
            else:
                for customerID in list_customers:
                    print(list_customers[customerID])
        elif COMMANDINPUT in 'd' or COMMANDINPUT in 'D':
            print(list_customers[ID])
            customerID = ID
            del list_customers[customerID]
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
            list_customers[customerID] = list_customers[temp]
            # Delete the old ID
            del list_customers[temp]
            print("Customer ID %s has been updated to %s."
                  % (temp, customerID))
        elif COMMANDINPUT in 'a' or COMMANDINPUT in 'A':
            fRead = float(VALUE1)
            sRead = float(VALUE2)

            # Return values
            if valid is True:
                balance = calculateBill(fRead, sRead)
                print("Your user %s balance is $%.2f." % (ID, balance))
            list_customers[ID] = balance
        elif COMMANDINPUT in 'e' or COMMANDINPUT in 'E':
            f.close()
            exit()
