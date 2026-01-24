# Custom exception example

class InvalidAgeError(Exception):
    pass


def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")
    return "Eligible to vote"


try:
    print(check_age(16))
except InvalidAgeError as e:
    print(e)

# Output:
# Age must be 18 or above

