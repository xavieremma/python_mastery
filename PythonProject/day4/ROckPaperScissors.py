import random
choice = input("What do you choose? 0 = Rock | 1 = Paper | 2 = Scissors: \n")
if choice == "0":
    print("You choose Rock")
elif choice == "1":
    print("You choose Paper")
elif choice == "2":
    print("You choose Scissors")
else:
    print("Invalid choice")
computerChoice = random.randint(0,2)
if(computerChoice == 0):
    print("Computer chose Rock")
    if(choice == "1"):
        print("You win!")
    elif(choice == "2"):
        print("You lose!")
    else:
        print("Draw!")
elif(computerChoice == 1):
    print("Computer chose Paper")
    if(choice == "0"):
        print("You lose!")
    elif(choice == "2"):
        print("You win!")
    else:
        print("Draw!")
else:
    print("Computer chose Scissors")
    if(choice == "0"):
        print("You win!")
    elif(choice == "1"):
        print("You lose!")
    else:
        print("Draw!")