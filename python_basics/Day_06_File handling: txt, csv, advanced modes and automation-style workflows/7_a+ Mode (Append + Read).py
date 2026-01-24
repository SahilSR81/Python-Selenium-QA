# a+ appends data and allows reading

with open("report.txt", "a+") as file:
    file.write("\nTotal Tests: 10")
    file.seek(0)
    print(file.read())

# Output:
# Execution Report
# Total Tests: 10

