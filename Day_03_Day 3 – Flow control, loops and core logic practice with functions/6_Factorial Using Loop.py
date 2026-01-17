# Factorial of a number

num = int(input("Enter number: "))
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial:", fact)

# Output:
# Enter number: 5
# Factorial: 120

