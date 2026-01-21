# Demonstrating full exception flow

try:
    num = int(input("Enter number: "))
    result = 100 / num
except ZeroDivisionError:
    print("Zero is not allowed")
else:
    print("Result:", result)
finally:
    print("Execution completed")

# Output:
# Enter number: 10
# Result: 10.0
# Execution completed

