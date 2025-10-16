
# # Question 01
# name:str = "Ali"
# print(name)

# #Question 02
# age:int = 20
# print("Hey! My Name is:", name, "and i'm", age,"Year old" )

# #Question 03
# a:int = 5
# b:int = 10

# a,b = b,a
# print("a =",a)
# print("b =",b)

# #Question 04

# x = 10
# y = 12.5
# z = "Python"
# w = True

# print(type(x))
# print(type(w))
# print(type(y))
# print(type(z))

# #Question 05

# rollNo = 101
# percentage = 84.9
# studentName = "Saeed"
# isPresent = True

# print(rollNo,percentage,studentName,isPresent)

# #Question 06

# num = 5
# print(float(num))
# print(str(num))


# #Question 07

# num = "100"
# result = int(num) + 50
# print(result)


# #Question 08
# booleanValue = False
# print(int(booleanValue))


# # #Question 09
# num1 = int(input("Enter First Number: "))
# num2 = int(input("Enter Second Number: "))
# operator = input("Enter Operator: ")
# result = 0

# if operator == "+":
#     result = num1 + num2
#     print("The Result is: ", result)
# elif operator == "-":
#     result = num1 - num2
#     print("The Result is: ", result)
# elif operator == "*":
#     result = num1 * num2
#     print("The Result is: ", result);
# elif operator == "/":
#     result = num1 / num2
#     print("The Result is: ", result)
# elif operator == "%":
#     result = num1 % num2
#     print("The Result is: ", result)
# elif operator == "**":
#     result = num1 ** num2
#     print("The Result is: ", result)
# else:
#     print("Invalid Operator!")

# #Question 10
 
# users = ["Saeed","Ali","Jerry","Khan"]

# for user in users:
#     print(user)

# #Question 11

# length = float(input("Enter the Length of Reactangle: "))
# width = float(input("Enter the width of Reactangle: "))

# area = length * width
# perimeter = 2 *(length + width)

# print(f"Area: {area:.2f}")
# print(f"Perimeter: {perimeter:.2f}")

# #Question 12

# num = 6

# if num > 0:
#     print(f"This Number {num} is Positive")
# elif num < 0:
#     print(f"This Number {num} is Negative")
# else:
#     print(f"This Number is {num}")


# #Question 13

# def python_geet ():
#     print("Hello this is from python") 

# python_geet()
# #Question 14
# def printMyName():
#     myName = input("Enter your Name: ")
#     print(f"Hey🙋 Dear {myName} Welcome to the Python Hub 🤗")

# printMyName()

# #Question 15

# def greet(userName):
#     print(f"Hello Dear {userName}")
# greet("Jerry")

# #Question 16

# def sum(a,b):
#     return a+b
# result= sum(3,5)
# print(result)

#Question 17

# import math

# def square_root(num):
#     return math.sqrt(num)
# result = square_root(16)
# print(result)


#Question 18
# from math import factorial

# def fact(num):
#     return factorial(num)
# result = fact(5)
# print(result)


#Question 19

# import random

# def my_func():
#     y = random.randint(1,5)  # Local variable
#     print("Random:", y)
    
# my_func()
