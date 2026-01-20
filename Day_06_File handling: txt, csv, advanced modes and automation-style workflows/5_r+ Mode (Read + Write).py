# r+ allows reading and writing without truncating file

with open("testdata.txt", "r+") as file:
    print(file.read())
    file.write("\nrole=admin")

# Output:
# username=admin
# password=admin123

