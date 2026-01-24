# Handling division by zero

try:
    a = int(input("Enter number: "))
    result = 10 / a
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero")

# Output:
# Enter number: 0
# Cannot divide by zero

