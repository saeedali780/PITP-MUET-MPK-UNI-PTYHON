# Print each user from the list
users = ["Saeed","Ali","Jerry","Khan"]

for user in users:
    print(user)

# Print numbers from 1 to 10
for i in range(1, 11):
    print(i)
 
# Continuously ask for a number until 0 is entered    
while True:
    num = int(input("Enter a number (0 to exit): "))
    if num == 0:
        break
    print(f"You entered: {num}")

# Ask for developer name until "Saeed" is entered
while True:
    devName = input("Enter your Developer Name: ")
    if devName == "Saeed":
        print("Welcome Saeed!")
        break
    else:
        print("You are not Saeed! Try again.")
