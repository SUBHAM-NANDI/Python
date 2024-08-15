import random

random_integer = random.randint(1,10)
print(random_integer)

random_0to1 = random.random()
random_float = random_0to1*10
print(random_float)

random_float1 = random.uniform(1,10)
print(random_float1)

randomHeadsOrTails = random.randint(0,1)
if randomHeadsOrTails == 0:
    print("Heads")
else: print("Tails")