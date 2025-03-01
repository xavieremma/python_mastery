#Python uses the mersene twister for psuedo random number generator

# the python documentation has a random module
import random

randomInteger = random.randint(1,10)
# generates random number greater than or equal to a, and less than or equal to b random.randint(a,b)

print(randomInteger)

# to add code from a different file:
# import filename.py or filename.txt
# to print it it would be print("filename.variable")

# generating random floating point numbers
#random.random(0.0 <= x < 1.0)

randomNum01 = random.random()
print(randomNum01)

#Heads or tails programs
coinFlip = random.randint(0,1)
if(coinFlip == 0):
    print("Heads")
else:
    print("Tails")