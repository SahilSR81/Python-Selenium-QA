# Demonstrating instance vs class variables

class Account:
    bank_name = "State Bank"   # class variable

    def __init__(self, holder, balance):
        self.holder = holder   # instance variable
        self.balance = balance # instance variable


acc1 = Account("Sahil", 5000)
acc2 = Account("Rahul", 8000)

print(acc1.bank_name)
print(acc2.bank_name)

# Output:
# State Bank
# State Bank

