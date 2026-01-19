# Demonstrating polymorphism via method overriding

class Login:
    def authenticate(self):
        print("Basic authentication")


class OAuthLogin(Login):
    def authenticate(self):
        print("OAuth based authentication")


login1 = Login()
login2 = OAuthLogin()

login1.authenticate()
login2.authenticate()

# Output:
# Basic authentication
# OAuth based authentication

