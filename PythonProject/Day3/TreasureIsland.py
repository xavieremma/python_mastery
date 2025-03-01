print("Welcome to Treasure Island!")
print("Your mission is to find the treasure!")
choice1 = input("You're at a cross road. Where do you want to go? (L or R)")
if(choice1 == "L"):
    choice2 = input("you have come across a lake, where will you go? (L or R)")
    if(choice2 == "L"):
        print("you drowned :(")
    if(choice2 == "R"):
        choice3 = input("you have come across a house, where will you go? (L or R)")
        if(choice3 == "L"):
            print("you found the treasure!")
        else:
            print("you wander aimlessly and succomb to the elements empty handed :(")
else:
    print("You fell into a snake pit, Game Over :(")
