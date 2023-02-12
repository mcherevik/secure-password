from random import *
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''


def password_number():
    print("How many passwords do you want to generate?")
    while True:
        num = input()
        if num.isdigit():
            return int(num)
        else:
            print("This is not a number. Try again")


def password_length():
    print("What is the length of one password?")
    while True:
        num = input()
        if num.isdigit():
            return int(num)
        else:
            print("This is not a number. Try again")


print("Do you want to include numbers? Y / N")
answer = input()
if answer == 'Y':
    chars += digits


print("Do you want to include lowercase letters? Y / N")
answer = input()
if answer == 'Y':
    chars += lowercase_letters


print("Do you want to include uppercase letters? Y / N")
answer = input()
if answer == 'Y':
    chars += uppercase_letters


print("Do you want to include punctuation symbols? Y / N")
answer = input()
if answer == 'Y':
    chars += punctuation


def generate_password(length, characters):
    password = ''
    for i in range(length):
        password += choice(characters)
    print(password)


length = password_length()
for j in range(password_number()):
    generate_password(length, chars)

