# Encapsulation using naming convention

class Account:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount


acc = Account(5000)

print(acc.get_balance())
acc.set_balance(8000)
print(acc.get_balance())

# Output:
# 5000
# 8000

# This will cause error

print(acc.__balance)

# Output:
# AttributeError

