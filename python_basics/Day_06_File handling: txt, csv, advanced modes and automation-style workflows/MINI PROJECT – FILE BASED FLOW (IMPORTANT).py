# Read test data → validate → write result

with open("users.csv", "r") as infile, open("result.txt", "w+") as outfile:
    for line in infile:
        if "admin" in line:
            outfile.write("Admin user found - PASS\n")
        else:
            outfile.write("Normal user\n")

    outfile.seek(0)
    print(outfile.read())

# Output:
# Admin user found - PASS
# Normal user

