class Calculator:
    def __init__(self):
        pass
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Cannot divide by zero!"
        return x / y


calculator = Calculator()

print(calculator.add(1, 2))  # 3
print(calculator.subtract(3, 2))  # 1
print(calculator.multiply(2, 5))  # 6
print(calculator.divide(9, 3))  # 3
print(calculator.divide(9, 0))
