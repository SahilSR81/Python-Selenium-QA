# List CRUD operations

languages = ["Java", "Python", "C++"]

# Create (Add)
languages.append("JavaScript")

# Read
print("Languages:", languages)

# Update
languages[1] = "Python 3"

# Delete
languages.remove("C++")

print("Updated List:", languages)

# Output:
# Languages: ['Java', 'Python', 'C++', 'JavaScript']
# Updated List: ['Java', 'Python 3', 'JavaScript']

