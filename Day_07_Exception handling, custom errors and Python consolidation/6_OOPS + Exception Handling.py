# Combining OOPS with exception handling

class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def validate(self):
        if self.username != "admin" or self.password != "admin123":
            raise Exception("Invalid credentials")
        return "Login successful"


try:
    user = Login("admin", "wrongpass")
    print(user.validate())
except Exception as e:
    print(e)

# Output:
# Invalid credentials

