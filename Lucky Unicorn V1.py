"""
Lucky Unicorn Version 1
Yes/No Checker
By Daniel Wu
"""
global question
# Add constants
ZEBRA_TOKEN = 0.5
HORSE_TOKEN = 0.5
UNICORN_TOKEN = 5
DONKEY_TOKEN = 0


# Yes/No Checker
def yes_no():
    answer = input(question)
    if answer.upper() == "YES" or answer.upper() == "Y":
        return True
    elif answer.upper() == "NO" or answer.upper() == "N":
        return False
    else:
        print("Please enter (Yes/No)")
        return None


# Ask user if they have played before: if yes, program continue, if no, show instruction screen
question = "Have you played before? \n"
if yes_no():
    print("Continue")
elif not yes_no():
    print("Show instructions")
else:
    print("Error")
    yes_no()

# Error checking
