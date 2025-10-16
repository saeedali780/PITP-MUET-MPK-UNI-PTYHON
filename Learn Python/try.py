# def hello():
#     return "Hello, World!"

# sayHello = hello()
# print(sayHello)

# def calculate():
#     return 2+3

# printResult = calculate()
# print(printResult)

# if 5> 4:
#     print("Hey Jerry")
    
# myName = "Saeed"
# myName = 2
# print(myName)
# myname = "Saeed"
# myName = "Jerry"
# my_name = "Cute"
# print(myname, my_name, myName)

# num = 2

# for num in range(1, 10):
#     print("2" )

# userName:str = input("Enter Your FullName: ")
# # userAge:int = int(input("Enter Your Age: "))
# # userFavColor:str = input("Enter your Fav Color: ")
# # currentYear:int = int(input("Enter Current Year: "))

# #print("Hey!",userName, "your age is", userAge, "and your Fav Color is",userFavColor,"finally the current year is",currentYear)

# if userName == "Saeed Ali":
#     sayHello = "Hello" + userName + "Welcome Back!"
#     print(sayHello)
#     print("Your Are Allowed to Login")
# else:
#     print("Sorry user doesn't exists!") 




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
# else:
#     print("Invalid Operator!")


# def isPositive(num):
#     if num > 0:
#         return f"This Number {num} is Positive"
#     elif num < 0:
#         return f"This Number {num} is Negative"
#     else:
#         return f"This Number is {num}"

# result = isPositive(-1)

# print(result)


# x = 10  # Global variable

# def my_func():
#   y = 5  # Local variable 
#   print("Inside function:", y)
# #   print("Hey this is x from function", x)
  

# my_func()
# print("Outside function:", y)

mylist = ["Saeed","Ali","Jerry"]

print(f"List before remove {mylist}")

for user in mylist:
  if user == "Jerry":
    print(user)    
    mylist.remove(user)

print(f"List after remove {mylist}")