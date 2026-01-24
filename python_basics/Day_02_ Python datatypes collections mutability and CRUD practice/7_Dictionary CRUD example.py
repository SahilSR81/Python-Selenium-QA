# Dictionary CRUD example

student = {
    "name": "Sahil",
    "age": 22,
    "course": "Automation"
}

# Read
print(student["name"])

# Update
student["age"] = 23

# Create
student["city"] = "Kolkata"

# Delete
del student["course"]

print(student)

# Output:
# Sahil
# {'name': 'Sahil', 'age': 23, 'city': 'Kolkata'}

