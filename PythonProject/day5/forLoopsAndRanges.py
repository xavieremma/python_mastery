# Use a loop completely independent of a list using the range function
# range generators a range of numbers to loop through
# Syntax:
#for number in range(a, b):
    #print(number)
for number in range(1, 10): # 10 isnt included so set range to 11
    print(number)

for number in range(1, 11, 3): # the last argument in range sets the step on how much it should count by
    print(number)

# <--- Gauss Challenge --->
sum = 0
for number in range(1, 101):
    sum += number

print(sum)