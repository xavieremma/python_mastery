print("Welcome to the Secret Auction!")

def UserandBid():
    user = input("What is your name:")
    bid = input("What is your bid:")
    addUserAndBid(user, bid)

def addUserAndBid(user, bid):
    username [user] = bid
    choice = input("Are there any other users? (y/n): ")

    if choice == "y":
        UserandBid()
    else:
        Winner()

def Winner():
    maxBid = 0
    for user in username:
        maxbid = username[user]
        if maxbid > username[user]:
            maxbid = username[user]
    print(f"The winner is {user} with a bid of ${maxbid}")



username = {}

UserandBid()




