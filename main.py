def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

a = int(input('Enter a number.'))
b = int(input('Enter another number.'))
c = input('Add, subtract, multiply, or divide?')
match c:
    case "add":
        print(str(add(a, b)))
    case "subtract":
        print(str(subtract(a, b)))
    case "multiply":
        print(str(multiply(a,b)))
    case "divide":
        print(str(divide(a,b)))
