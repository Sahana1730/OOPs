class Bank:
    def __init__(self):
        self.__balance = 1000   # private variable

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

b = Bank()
b.deposit(500)
print("Balance:", b.get_balance())
