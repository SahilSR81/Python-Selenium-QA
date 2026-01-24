# Writing data to a file
# WARNING: 'w' overwrites existing content

file = open("output.txt", "w")
file.write("Test execution started\n")
file.write("Status: PASS\n")
file.close()

print("File written successfully")

# Output:
# File written successfully

