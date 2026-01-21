# Mini automation-style flow

class UserValidator:
    def validate_user(self, username):
        if username != "admin":
            raise Exception("Unauthorized user")
        return "Valid user"


validator = UserValidator()

try:
    with open("users.txt", "r") as infile, open("result.txt", "w+") as outfile:
        for user in infile:
            user = user.strip()
            try:
                result = validator.validate_user(user)
                outfile.write(f"{user}: PASS\n")
            except Exception as e:
                outfile.write(f"{user}: FAIL ({e})\n")

        outfile.seek(0)
        print(outfile.read())

except FileNotFoundError:
    print("Input file missing")

# Output:
# admin: PASS
# guest: FAIL (Unauthorized user)

