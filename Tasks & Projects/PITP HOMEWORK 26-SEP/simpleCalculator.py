# Simple Calculator in Python

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
operator = input("Enter Operator: ")
result = 0

if operator == "+":
    result = num1 + num2
    print("The Result is: ", result)
elif operator == "-":
    result = num1 - num2
    print("The Result is: ", result)
elif operator == "*":
    result = num1 * num2
    print("The Result is: ", result);
elif operator == "/":
    result = num1 / num2
    print("The Result is: ", result)
else:
    print("Invalid Operator!")