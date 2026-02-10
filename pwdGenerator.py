import random

print("Benvenuto al Generatore di Password")

chars = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890!£$%&/()=?*-+.,_;:@"

number = input("Quante psw vuoi?")
number = int(number)

lenght = input("Quanto devono essere lunghe?")
lenght = int(lenght)

print("\nEcco le tue psw:")

for pwd in range(number):
    passwords = ""
    for c in range(lenght):
        passwords += random.choice(chars)
    print(passwords)
