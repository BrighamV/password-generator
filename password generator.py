"""
Password Generator

Created by: Brigham Valentine

"""
import string
import random
string.ascii_letters

characters = '!@#$%^&*<>?/'

num = '123456789'


print("Passwords are very important in keeping our information safe\n")
print("This program is designed to make a good and safe password.\n")

password = []

long = int(input("How many characters long does your password need to be? 8, 12, or 16: "))
numbers = int(input("How many numbers do you want in your password? 1, or 2: "))
special = input("Do you want special characters in your password? y/n: ")

if long == 8:
    if numbers == 1:
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
        if special == "y" or special == "y":
            password.append(random.choice(characters))
        else:
            password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(num))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
    else:
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(num))
        if special == "y" or special == "y":
            password.append(random.choice(characters))
        else:
            password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(num))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
elif long == 12:
    if numbers == 1:
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
        if special == "y" or special == "y":
            password.append(random.choice(characters))
        else:
            password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(num))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
    else:
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(num))
        if special == "y" or special == "y":
            password.append(random.choice(characters))
        else:
            password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(num))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
else:
    if numbers == 1:
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
        if special == "y" or special == "y":
            password.append(random.choice(characters))
        else:
            password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(num))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
    else:
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(num))
        if special == "y" or special == "y":
            password.append(random.choice(characters))
        else:
            password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(num))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.ascii_letters))


for i in range(len(password)):
    print(password[i], end = '')
    
    
    