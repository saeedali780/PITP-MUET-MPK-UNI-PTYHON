#   Write a program that takes numbers from the user until the user enters a number greater than 100.
total = 0
while True:
    num = int(input("Enter a number: "))
    if num >= 100:
        total += num
        break
    else:
        print("Number is less, please try again.")
print(f"The user Entered: {total}")