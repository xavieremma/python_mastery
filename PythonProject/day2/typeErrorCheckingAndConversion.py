# <--- Type Error --->
#len(12345) will produce a type error
#the correct format is:
len("Hello")

print(type("Hello")) # this checks the data type of the
# prints <class, 'str'>

# <--- Type Conversion --->
int("123")
print(int("123") + int("456")) # you cannot convert "abc" into a number, this produces an error

# fixed the code
print("Number of letters in your name: " + str(len(input("What is your name? "))))

nameOfUser = input("Enter your name")
print(type("Number of letters in your name: "))
lengthOfName = len(nameOfUser)
print(type(lengthOfName))