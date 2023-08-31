class bank_account:
    def __init__(self):
        self.balance=0
        print("Congratulations! your account has been created")

    def deposit(self):
        amount=float(input("enter the amount to deposited = "))
        self.balance += amount
        print("Amount deposited:",amount)
        print("Your balance is ",self.balance)

    def withdraw(self):
        amount = float(input("enter the amount to be withdrawn = "))
        if self.balance >= amount:
            self.balance -= amount
            print("You withdrawn",amount)
        else:
            print("Insufficient balance")
        print("Your balance is ",self.balance)

s=bank_account()
s.deposit()
s.withdraw()
