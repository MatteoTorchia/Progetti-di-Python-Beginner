import random

x = random.randint(1,6)

guess = int(input("Try to guess the number between 1 and 6: "))

if guess >=0 and guess <=6:
    if x==guess:
        print("You won, the number was: " + str(x))
    else:
        print("You lost, the correct answer was: " + str(x))
else:
    print("Please insert a nuber between 1 and 6.")
