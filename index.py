 # problem 1

userIn = input("Enter something or press q to quit.  ")
while userIn != "q":
    print(userIn)
    userIn = input("Enter something or press q to quit.  ")

    # skip problem 2

#  problem 3

userInput = input("Enter 1, 2, 3, or q to quit.  ")
while userInput != "q":
    if userInput == "1":
        print("1!")
        userInput = input("Enter 1, 2, 3, or q to quit.  ")
    elif userInput == "2":
        print("2!")
        userInput = input("Enter 1, 2, 3, or q to quit.  ")
    elif userInput == "3":
        print("3")
        userInput = input("Enter 1, 2, 3, or q to quit.  ")
    else:
        print("ERROR")
        userInput = input("Enter 1, 2, 3, or q to quit.  ")

# problem 4:

userInput1 = input("Enter elements or press q to quit  ")
userList =""
while  userInput1 != "q":
    userList = userList + ', ' + userInput1
    userInput1 = input("enter more or press q to quit  ")
print(userList)