print("Welcome to the tip calculator")
billTotal = float(input("What was the total bill?\n"))
tip = int(input("How much would you like to tip (percentage)? 10, 12, 15, 20?\n"))
total = float(round(((tip / 100 + 1) * billTotal), 2))
print(f"Your total bill is ${total}")

splitNum = input("How many people to split the bill?\n")
splitTotal = float(round(total / int(splitNum), 2))
print(f"Each person should pay ${splitTotal}")