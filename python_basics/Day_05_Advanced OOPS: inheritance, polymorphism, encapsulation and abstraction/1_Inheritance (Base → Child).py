# Base class

class User:
    def __init__(self, name):
        self.name = name

    def get_role(self):
        return "Generic User"


# Child class
class Admin(User):
    def get_role(self):
        return "Admin User"


user = User("Sahil")
admin = Admin("Rahul")

print(user.get_role())
print(admin.get_role())

# Output:
# Generic User
# Admin User

