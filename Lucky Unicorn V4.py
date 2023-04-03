"""
Lucky Unicorn Version 4
Number Checker
By Daniel Wu
"""
import random

# Add constants
ZEBRA_TOKEN = 0.5
HORSE_TOKEN = 0.5
UNICORN_TOKEN = 5
DONKEY_TOKEN = 0


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
    tokens = [["U", 5], ["Z", 0.5], ["H", 0.5], ["D", 0]]
    number = random.randint(1, 4)
    return tokens[number]


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
#    generate()
    print("Continue")
else:
    instructions()
    question = "Do you want to continue? \n"
    if yes_no(question):
        print("Continue")
    else:
        print("Exit")
