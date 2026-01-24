# with statement automatically closes file

with open("output.txt", "r") as file:
    data = file.read()

print(data)

# Output:
# Test execution started
# Status: PASS
# Execution time: 12s

