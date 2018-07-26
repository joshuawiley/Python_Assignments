# Author: Joshua Wiley
# Title:  Electric Bill Calculator

# Check if the beginning of the month reading is
# greater then the second reading


def valid_reading(first_reading, second_reading):
    while first_reading >= second_reading:
        print("First input cannot be the same as the second!\n")
        first_reading = float(input("Enter Your Beginning of Month KwH Used: "))
        print(first_reading)
        second_reading = float(input("Enter Your End of Month KwH Used: "))
        print(second_reading)

    return True, first_reading, second_reading


# Calculate the Monthly bill
def calculate_bill(reading_one, reading_two):
    # RATE1, RATE2, RATE3 = 0.08, 0.11, 0.15
    kwh = float(reading_two - reading_one)

    if kwh < 500:
        rate = 0.08
    elif kwh <= 500 or kwh < 1500:
        rate = 0.11
    elif kwh >= 1500:
        rate = 0.15
    else:
        rate = 0.20

    bill = rate * kwh

    return bill


# Main
LIST_CUSTOMERS = {}
while True:
    print("\nN/n = New User")
    print("L/l = Lookup User")
    print("D/d = Delete User")
    print("U/u = Update User")
    print("A/a = Add New Bill")
    print("E/e = Exit\n")

    COMMANDINPUT = input("\nEnter a command: ")
    print(COMMANDINPUT)
    if COMMANDINPUT in 'n' or COMMANDINPUT in 'N':
        CUSTOMER_ID = input("\nEnter your 4 digit customer ID: ")
        print(CUSTOMER_ID)
        F_READ = float(input("Enter Your Beginning of Month KwH Used: "))
        print(F_READ)
        S_READ = float(input("Enter Your End of Month KwH Used: "))
        print(S_READ)

        # Return values
        VALID, F_READ, S_READ = valid_reading(F_READ, S_READ)

        if VALID is True:
            BALANCE = float(calculate_bill(F_READ, S_READ))
            print("\nYour balance is $%.2f." % BALANCE)
        LIST_CUSTOMERS[CUSTOMER_ID] = BALANCE
    elif COMMANDINPUT in 'l' or COMMANDINPUT in 'L':
        CUSTOMER_ID = input("\nEnter your 4 digit customer ID: ")
        print(CUSTOMER_ID)
        if CUSTOMER_ID not in LIST_CUSTOMERS:
            print("\nThe Customer ID %s is not in the database." % CUSTOMER_ID)
        else:
            print(LIST_CUSTOMERS[CUSTOMER_ID])
    elif COMMANDINPUT in 'd' or COMMANDINPUT in 'D':
        CUSTOMER_ID = input("Enter your 4 digit customer ID: ")
        print(CUSTOMER_ID)
        del LIST_CUSTOMERS[CUSTOMER_ID]
        print("\nCustomer %s has been removed from the database." % CUSTOMER_ID)
    elif COMMANDINPUT in 'u' or COMMANDINPUT in 'U':
        # Enter current
        CUSTOMER_ID = input("Enter your current ID: ")
        print(CUSTOMER_ID)
        # Create a temp ID to store original ID
        TEMP = CUSTOMER_ID
        # Get new ID
        CUSTOMER_ID = input("Enter your new ID: ")
        print(CUSTOMER_ID)
        # Set the new ID with the old ID's value
        LIST_CUSTOMERS[CUSTOMER_ID] = LIST_CUSTOMERS[TEMP]
        # Delete the old ID
        del LIST_CUSTOMERS[TEMP]
        print("\nCustomer ID %s has been updated to %s." % (TEMP, CUSTOMER_ID))
    elif COMMANDINPUT in 'a' or COMMANDINPUT in 'A':
        CUSTOMER_ID = input("Enter your 4 digit customer ID: ")
        print(CUSTOMER_ID)
        F_READ = float(input("Enter Your New Beginning of Month KwH Used: "))
        print(F_READ)
        S_READ = float(input("Enter Your New End of Month KwH Used: "))
        print(S_READ)

        # Return values
        if VALID is True:
            BALANCE = calculate_bill(F_READ, S_READ)
            print("Your balance is $%.2f." % BALANCE)
        LIST_CUSTOMERS[CUSTOMER_ID] = BALANCE
    elif COMMANDINPUT in 'e' or COMMANDINPUT in 'E':
        exit()
