# Check palindrome string

text = input("Enter string: ")
reversed_text = ""

for char in text:
    reversed_text = char + reversed_text

if text == reversed_text:
    print("Palindrome")
else:
    print("Not Palindrome")

# Output:
# Enter string: madam
# Palindrome

