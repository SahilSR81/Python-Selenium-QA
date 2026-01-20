# Reading data from text file

file = open("testdata.txt", "r")
content = file.read()
file.close()

print(content)

# Output:
# username=admin
# password=admin123

