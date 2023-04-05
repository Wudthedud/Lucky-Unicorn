def initial_payment(amount):
    amount_ = amount
    num = isinstance(amount_, int)
    print(num)
    if 1 <= amount_ <= 10 and num is True:
        return amount_
    else:
        amount_ = float(input("Please enter a number between 1 and 10\n"))
        while 1 > amount_ > 10 and num is False:
            amount_ = float(input("Please enter a number between 1 and 10\n"))
            num = isinstance(amount_, int)
        return amount_


print(f"You are playing with ${initial_payment(6.5)}")
