#simple.calculater.py
print("Welcome to Simple Calculater")

num1 = float(input("Enter first number:"))
operator = input("Enter operator(+,-,*,/):")
num2 = float(input("Enter second number:"))

if operator == "+":
    print("Result:",num1 + num2)
elif operator == "-":
    print("Result:",num1  - num2)
elif operator == "*":
    print("Result:",num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result:",num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print("invalid operator")                            