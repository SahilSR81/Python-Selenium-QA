# Check if number is prime

num = int(input("Enter number: "))
is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print("Prime number")
else:
    print("Not a prime number")

# Output:
# Enter number: 7
# Prime number

