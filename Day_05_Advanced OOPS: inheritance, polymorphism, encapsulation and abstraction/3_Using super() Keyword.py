# Using super() to call parent class constructor

class Employee:
    def __init__(self, name):
        self.name = name


class Tester(Employee):
    def __init__(self, name, tool):
        super().__init__(name)
        self.tool = tool


t = Tester("Sahil", "Selenium")
print(t.name)
print(t.tool)

# Output:
# Sahil
# Selenium

