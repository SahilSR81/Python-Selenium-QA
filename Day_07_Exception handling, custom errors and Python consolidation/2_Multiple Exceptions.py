# Handling multiple exceptions

try:
    num = int(input("Enter number: "))
    print(10 / num)
except ValueError:
    print("Invalid input. Enter number only.")
except ZeroDivisionError:
    print("Division by zero not allowed.")

# Output:
# Enter number: abc
# Invalid input. Enter number only.

