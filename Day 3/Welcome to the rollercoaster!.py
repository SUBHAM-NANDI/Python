print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    elif age >= 45 and age <= 55:

        print("No bill required")
    else:
        bill = 12
        print("Please pay $12.")

    take_photograph = input("Do you want a photograph? y or n")
    if take_photograph == "y":
        bill += 3

    print(f"Final bill:{bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
