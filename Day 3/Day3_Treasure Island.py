print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
ch1 = input('You\'re at a crossroad, where do you want to go? '
                'Type "left" or "right".\n').lower()
if ch1 == "left":
   ch2 = input("Do you want to swim or wait").lower()
   if ch2 == "wait":
     ch3 = input("Which door colour do you want ").lower()
     if ch3 == "yellow":
           print("You Win")
     elif ch3 == "red":
           print("You Win")
     elif ch3 == "blue":
           print("Game Over")
     else: print("Game Over")
   else: print("Game Over")
else: print("Game Over")

