# Wrong usage of class variable

class User:
    role = "Tester"

    def __init__(self, name):
        self.name = name
        self.role = "Admin"   # This creates instance variable


u1 = User("Sahil")
u2 = User("Rahul")

print(u1.role)
print(u2.role)

# Output:
# Admin
# Admin (unexpected if intention was class-level)


# FIX: Modify class variable correctly

User.role = "Admin"

print(u1.role)
print(u2.role)

# Output:
# Admin
# Admin

