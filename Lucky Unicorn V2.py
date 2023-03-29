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


# Ask user if they have played before
played_before = input("Have you played before? (Y/N) \n")

# If yes, program continues
if played_before.upper() == "YES" or played_before.upper() == "Y":
    print("Continue")
# If no, show instruction screen
elif played_before.upper() == "NO" or played_before.upper() == "N":
    print("Show instructions")

# Error checking
else:
    print("Please enter (Y/N)")

