# Safe file reading with exception handling

try:
    with open("data.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found. Please check file name.")

# Output:
# File not found. Please check file name.

