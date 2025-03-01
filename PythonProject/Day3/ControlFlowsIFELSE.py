print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
else:
    print("Sorry you can't ride the rollercoaster")
    # if there is not an indentation, you get an indentation error

#<--- Modulo Operator --->
# 10 % 5 = 0
# 10 % 3 = 1
# modulo gives the remainder of division
numToCheck = int(input("What is the number you want to check? "))
if(numToCheck % 2 == 0):
    print("The number is even")
else:
    print("The number is odd")

# <--- Multiple if statements in succession --->
#python pizza delivery program
print("Welcome to Python Pizza Deliveries!")
bill = 0
size = input("What size pizza would you want? S, M, or L ")

pepperoni = input("Would you like pepperoni on your pizza? Y or N ")
extraCheese = input("Would you like extra cheese on your pizza? Y or N ")
if(size == 'S'):
    bill += 15
    if(pepperoni == "Y"):
        bill += 2
    if(extraCheese == "Y"):
        bill += 1
elif(size == 'M'):
    bill += 20
    if (pepperoni == "Y"):
        bill += 3
    if (extraCheese == "Y"):
        bill += 1
elif size == 'L':
    bill += 25
    if (pepperoni == "Y"):
        bill += 3
    if (extraCheese == "Y"):
        bill += 1

print(f"Your final bill is ${bill}")
