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


# Main
list_customers = {}
while True:
    print("\nN/n = New User")
    print("L/l = Lookup User")
    print("D/d = Delete User")
    print("U/u = Update User")
    print("A/a = Add New Bill")
    print("E/e = Exit\n")

    
    commandInput = input("\nEnter a command: ")
    if commandInput in 'n' or commandInput in 'N':
        customerID = input("\nEnter your 4 digit customer ID: ")
        fRead = float(input("\nEnter Your Beginning of Month KwH Used: "))
        sRead = float(input("\nEnter Your End of Month KwH Used: "))

        # Return values
        valid, fRead, sRead = validReading(fRead, sRead)

        if valid is True:
            balance = float(calculateBill(fRead, sRead))
            print("\nYour balance is $%.2f." % balance)
        list_customers[customerID] = balance
    elif commandInput in 'l' or commandInput in 'L':
        customerID = input("\nEnter your 4 digit customer ID: ")
        if customerID not in list_customers:
            print("\nThe Customer ID %s is not in the database." % customerID)
        else:
            for customerID in list_customers:
                print(list_customers[customerID])
    elif commandInput in 'd' or commandInput in 'D':
        customerID = input("\nEnter your 4 digit customer ID: ")
        del list_customers[customerID]
        print("\nCustomer %s has been removed from the database." % customerID)
    elif commandInput in 'u' or commandInput in 'U':
        # Enter current
        customerID = input("\nEnter your current ID: ")
        # Create a temp ID to store original ID
        temp = customerID
        # Get new ID
        customerID = input("\nEnter your new ID: ")
        # Set the new ID with the old ID's value
        list_customers[customerID] = list_customers[temp]
        # Delete the old ID
        del list_customers[temp]
        print("\nCustomer ID %s has been updated to %s." % (temp, customerID))
    elif commandInput in 'a' or commandInput in 'A':
        customerID = input("\nEnter your 4 digit customer ID: ")
        fRead = float(input("\nEnter Your New Beginning of Month KwH Used: "))
        sRead = float(input("\nEnter Your New End of Month KwH Used: "))

        # Return values
        if valid is True:
            balance = calculateBill(fRead, sRead)
            print("\nYour balance is $%.2f." % balance)
        list_customers[customerID] = balance
    elif commandInput in 'e' or commandInput in 'E':
        exit()
