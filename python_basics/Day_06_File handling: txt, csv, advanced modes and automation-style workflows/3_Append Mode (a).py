# Append new content without deleting old data

file = open("output.txt", "a")
file.write("Execution time: 12s\n")
file.close()

print("Data appended")

# Output:
# Data appended

