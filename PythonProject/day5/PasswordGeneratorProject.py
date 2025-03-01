import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
numLetters = int(input("How many letters would you like in your password?\n"))
numSymbols = int(input(f"How many symbols would you like?\n"))
numNumbers = int(input(f"How many numbers would you like?\n"))

# letters ---> numbers ---> symbols
password = ""

for char in range(1, numLetters + 1):
    password += random.choice(letters)

for char in range(1, numSymbols +1):
    password += random.choice(symbols)

for char in range(1, numNumbers + 1):
    password += random.choice(numbers)

print(password)

# more randomized

passwordList = []

for char in range(1, numLetters + 1):
    passwordList.append(random.choice(letters))

for char in range(1, numSymbols +1):
    passwordList.append(random.choice(symbols))

for char in range(1, numNumbers + 1):
    passwordList.append(random.choice(numbers))

random.shuffle(passwordList)
print(passwordList)

password = ""
for char in passwordList:
    password += char
print(f"Your password is: {password}")
