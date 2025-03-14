def add(m, n):
    return m + n

def modulo(m, n):
    return m % n
def subtract(m, n):
    return m - n

def multiply(m, n):
    return m * n

def divide(m, n):
    if n == 0:
        return "Error! Division by zero."
    return m / n

def get_operation_result(op, num1, num2):
    if op == '+':
        return add(num1, num2)
    elif op == '-':
        return subtract(num1, num2)
    elif op == '*':
        return multiply(num1, num2)
    elif op == '/':
        return divide(num1, num2)
    elif op == '%':
        return modulo(num1, num2)
    else:
        return "Invalid operation"

def calculator():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /, %): ")
        
        result = get_operation_result(operation, num1, num2)
        
        if result == "Invalid operation":
            print(result)
        else:
            print(f"The result is: {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

calculator()
 