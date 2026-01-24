# Class with constructor

class User:
    def __init__(self, name, age):
        self.name = name        # instance variable
        self.age = age          # instance variable

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)


user1 = User("Sahil", 22)
user1.display_info()

# Output:
# Name: Sahil
# Age: 22

