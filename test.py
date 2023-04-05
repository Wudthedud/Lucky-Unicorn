def payment():
    while True:
        try:
            amount = float(input("Please enter a number between 1 and 10\n"))
            if 1 <= amount <= 10 and amount.is_integer():
                print(f"You are playing with ${amount:.2f}")
                return amount
            else:
                print("Please enter an integer between 1 and 10\n")
        except ValueError:
            print("Please enter a number between 1 and 10\n")

