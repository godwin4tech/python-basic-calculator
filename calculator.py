# Basic Calculator Program
# Author: Godwin Kipkoech
# Objective: Practice variables, user input, arithmetic operations, and strings.

# Ask the user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask the user to choose a mathematical operation
operation = input("Choose an operation (+, -, *, /): ")

# Perform the calculation based on the chosen operation
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

elif operation == "/":
    if num2 != 0:  # Prevent division by zero
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Invalid operation! Please choose +, -, * or /.")
