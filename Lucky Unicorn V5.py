"""
Lucky Unicorn Version 5
Token Generator
By Daniel Wu
"""
import random
import time

# Add constants
ZEBRA_TOKEN = 0.5
HORSE_TOKEN = 0.5
UNICORN_TOKEN = 5
DONKEY_TOKEN = 0
U = "Unicorn Token"
Z = "Zebra Token"
H = "Horse Token"
D = "Donkey Token"


# Instructions
def instructions():
    print("============ Welcome to Lucky Unicorn ============= \n"
          "\t Payout Rewards: \n"
          "\t Unicorn: 3x Payment \n"
          "\t Zebra: 1/2 of Payment \n"
          "\t Horse: 1/2 of Payment \n"
          "\t Donkey: Nothing \n"
          "===================================================")


# Number Checker
def is_number(num, min, max):
    while min > num > max:
        num = input(int(f"Please enter a number between {min} and {max} \n"))
    return num


# Token Generator
def generate():
    tokens = [[U, 5], [Z, 0.5], [H, 0.5], [D, 0]]
    number = random.randint(0, 3)
    token = tokens[number]
    print("Generating Token")
    for i in range(3):
        print(".")
        time.sleep(0.3)
    print(f"You got a {token[0]} \n"
          f"${token[1]:.2f} has been added to your balance")
    return



# Yes/No Checker
def yes_no(question_):
    while True:
        answer = input(question_).strip().lower()
        if answer in ["yes", "y"]:
            return True
        elif answer in ["no", "n"]:
            return False
        else:
            print("Please enter (Yes/No)")


# def payment(amount):
#    amount *


# Ask user if they have played before: if yes, program continues, if no, show instruction screen
question = "Have you played before? \n"
if yes_no(question):
    generate()
else:
    instructions()
    question = "Do you want to continue? \n"
    if yes_no(question):
        generate()
    else:
        print("Exit")
