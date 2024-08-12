print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

if size == "S":
    bill = 15
    print("Bill is 15")
elif size == "M":
    bill = 20
    print("Bill is 20")
elif size == "L":
    bill = 25
    print("Bill is 25")
else: print("Invalid size")

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else: bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Final bill: {bill}")
