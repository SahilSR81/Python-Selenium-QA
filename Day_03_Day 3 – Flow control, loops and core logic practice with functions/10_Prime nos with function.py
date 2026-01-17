# Prime number check using function

def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True


number = int(input("Enter number: "))

if is_prime(number):
    print("Prime number")
else:
    print("Not prime")

# Output:
# Enter number: 11
# Prime number

