# Mutable example (List)

a = [1, 2, 3]
b = a

b.append(4)
print("a:", a)
print("b:", b)

# Output:
# a: [1, 2, 3, 4]
# b: [1, 2, 3, 4]

# Immutable example (String)

x = "hello"
y = x

y = y.upper()

print("x:", x)
print("y:", y)

# Output:
# x: hello
# y: HELLO

