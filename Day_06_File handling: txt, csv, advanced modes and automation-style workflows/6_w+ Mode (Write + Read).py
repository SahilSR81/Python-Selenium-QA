# w+ truncates file before writing

with open("report.txt", "w+") as file:
    file.write("Execution Report\n")
    file.seek(0)
    print(file.read())

# Output:
# Execution Report

