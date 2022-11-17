import random

compNumber = random.randint(1, 1000)
userNumber = 1001
userPrevious = []

while userNumber != compNumber:
    userNumber = int(input("Pick a number 1-1000\n"))
    userPrevious.append(userNumber)
    if userNumber > compNumber:
        userPrevious.append("L")
    if userNumber < compNumber:
        userPrevious.append("H")
    for x in range(len(userPrevious)):
        if type(userPrevious[x]) is int:
            userPrevious[x] = " \033[37m " + str(userPrevious[x])
        elif userPrevious[x] == "H":
            userPrevious[x] = " \033[32m " + userPrevious[x]
        else:
            userPrevious[x] = " \033[31m " + userPrevious[x]
    userPreviousstr = "".join(userPrevious)
    print(f"{''.join(userPrevious[-2:])}\nPrevious guesses: {userPreviousstr}")
