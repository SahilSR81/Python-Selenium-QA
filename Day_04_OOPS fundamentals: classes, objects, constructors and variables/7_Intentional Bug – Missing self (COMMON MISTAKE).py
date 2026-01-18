# Buggy code: missing self keyword

class User:
    def __init__(name, age):   # ❌ self missing
        name = name
        age = age


# This will cause error when object is created


# FIXED VERSION

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("Sahil", 22)
print(user.name)

# Output:
# Sahil
