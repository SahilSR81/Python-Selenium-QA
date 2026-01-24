import csv

with open("users.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Output:
# ['username', 'password']
# ['admin', 'admin123']
# ['user1', 'test123']

