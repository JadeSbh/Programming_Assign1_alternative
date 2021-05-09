import random


def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            return x
        except ValueError:
            print("Oh Sorry, please enter a valid number!")


# Part 1

def getint():
    mylist = []
    j = 0
    while True:
        try:
            x = int(input("Please, enter a number:  "))
            if x > 0:
                mylist.append(x)
                print(f" The list now is {mylist}")
                if len(mylist) >= 2:
                    for i in len(mylist):
                        if mylist[i] > mylist[i + 1]:
                            continue
                        elif mylist[i] < mylist[i + 1]:
                            j = mylist[i]
                            mylist[i] = mylist[i + 1]
                            mylist[i + 1] = j
            elif x == 0 or x < 0:
                if sum(mylist) == 0:
                    print('Cannot find the largest value because no integers greater than 0 have been input')
                else:
                    print(mylist[0])
                    break
        except ValueError:
            pass


# Part Two:

def length(s):
    x = 0
    for i in s:
        x = x + 1
    return x


# Part Three:

def roll_dice():
    start = 1
    end = 6
    x = random.randint(start, end)
    return x


# Part Four:


menu = """
Please, choose an option:
1. Find the max
2. Calculate the length
3.roll the dice
0.exit"""
while True:
    print(menu)
    choice = get_int("Please make your choice, and enter an option:  ")
    if choice == 1:
        print("You choose to find the max among a group of numbers you enter :)")
    # find_max()
    elif choice == 2:
        print("you choose to calculate the length of a word :)")
        s = input("Please enter the word that you want to calculate its length:  ")
        result = length(s)
        print(f"The length of {s} is {result} ")

    elif choice == 3:
        print("you choose to roll a dice :)")
        result = roll_dice()
        print(f"The dice says {result}")
    elif choice == 0:
        print("you choose to quit, Good Bye !")
        break
    else:
        print("invalid number, Please choose from the menu")
        print(menu)
