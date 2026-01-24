import csv

with open("results.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["TestCase", "Status"])
    writer.writerow(["LoginTest", "PASS"])
    writer.writerow(["SignupTest", "FAIL"])

print("CSV report generated")

# Output:
# CSV report generated

