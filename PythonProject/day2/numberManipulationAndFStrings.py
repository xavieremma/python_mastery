bmi = 84 / 1.65 ** 2
print(bmi) # prints a massive decimal

print(int(bmi)) # prints interger

print(round(bmi)) # round function rounds up or down a whole number based on first decimal place

print(round(bmi, 2)) # rounds to two decimal places

# <--- Assignment Operator --->
# accumulates the results of a calculation
score = 0
score = score + 1
# we can use:
score += 1
print(score)

# <--- f Strings --->
# print("Your score is " + score) gives a type error
userScore = 0
height = 1.8
is_winning = True
print(f"Your score is = {score}, your height is {height}, You are winning is {is_winning}")
# f strings cuts down on the labor of inserting different things into strings



