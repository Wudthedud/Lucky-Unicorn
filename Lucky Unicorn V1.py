"""
Lucky Unicorn Version 1
Yes/No Checker
By Daniel Wu
"""

# Add constants
ZEBRA_TOKEN = 0.5
HORSE_TOKEN = 0.5
UNICORN_TOKEN = 5
DONKEY_TOKEN = 0


# Yes/No Checker
def yes_no(question):
    while True:
        answer = input(question).strip().lower()
        if answer in ["yes", "y"]:
            return True
        elif answer in ["no", "n"]:
            return False
        else:
            print("Please enter (Yes/No)")


# Ask user if they have played before: if yes, program continues, if no, show instruction screen
question = "Have you played before? \n"
if yes_no(question):
    print("Continue")
else:
    print("Show instructions")
