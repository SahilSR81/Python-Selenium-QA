# Real-world login model

class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def validate_login(self):
        if self.username == "admin" and self.password == "admin123":
            print("Login successful")
        else:
            print("Invalid credentials")


user = Login("admin", "admin123")
user.validate_login()

# Output:
# Login successful

