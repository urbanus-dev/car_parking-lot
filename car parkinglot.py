# SIMULATE A CAR PARKING LOT IN PHYTHON
# REQUIREMENTS
# ->spots available=20
# ->5 dollars to park per hour
# ->parking for more than 20 hours attracts 100dollars penalty
total_spots = 20
hourly_rate = 5
penalty = 100
max_parking_hours = 20
occupied_spots = 0
revenue = 0
while True:
    print("Welcome to the parking lot")
    print("1. Park a car")
    print("2. Remove a car")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        if occupied_spots < total_spots:
            car_number = input("Enter your car number: ")
            hours = int(input("Enter the number of hours: "))
            if hours > max_parking_hours:
                print("You have exceeded the maximum parking hours")
                print("You have to pay a penalty of 100 dollars")
                amount = (hours * hourly_rate) + penalty
            else:
                amount = hours * hourly_rate
            print("You have to pay", amount, "dollars")
            revenue += amount
            occupied_spots += 1
        else:
            print("Sorry, parking lot is full")
    elif choice == 2:
        if occupied_spots > 0:
            car_number = input("Enter your car number: ")
            hours = int(input("Enter the number of hours: "))
            if hours > max_parking_hours:
                print("You have exceeded the maximum parking hours")
                print("You have to pay a penalty of 100 dollars")
                amount = (hours * hourly_rate) + penalty
            else:
                amount = hours * hourly_rate
            print("You have to pay", amount, "dollars")
            revenue += amount
            occupied_spots -= 1
        else:
            print("Sorry, parking lot is empty")
    elif choice == 3:
        print("Total revenue:", revenue)
        break
    else:
        print("Invalid choice")
    print()

