from random import *
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

print("Welcome to the generator of the secure passwords!")


def validate_number():
    while True:
        num = input()
        if num.isdigit():
            return int(num)
        else:
            print("This is not a number. Try again")


def password_number():
    print("How many passwords do you want to generate?")
    return validate_number()


def password_length():
    print("What is the length of one password?")
    return validate_number()


def validate_answer():
    while True:
        answer = input()
        if answer.upper() == 'Y':
            return True
        elif answer.upper() == 'N':
            return False
        else:
            print("The answer is not valid. Please try again")


def chars_setup(chars_available):
    print("Do you want to include numbers? Y / N")
    if validate_answer():
        chars_available += digits

    print("Do you want to include lowercase letters? Y / N")
    if validate_answer():
        chars_available += lowercase_letters

    print("Do you want to include uppercase letters? Y / N")
    if validate_answer():
        chars_available += uppercase_letters

    print("Do you want to include punctuation symbols? Y / N")
    if validate_answer():
        chars_available += punctuation

    return chars_available


def chars_check():
    while True:
        characters = chars_setup(chars)
        if characters != "":
            return characters
        else:
            print("You should choose at least one range of symbols. Please try again")


def generate_password(pass_len, chars_available):
    password = ''
    for i in range(pass_len):
        password += choice(chars_available)
    print(password)


number = password_number()
length = password_length()
characters_available = chars_check()
for j in range(number):
    generate_password(length, characters_available)
