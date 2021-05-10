import random
import sys


def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            return x
        except ValueError:
            print("Oh Sorry, please enter a valid number!")


# Part 1

def find_max():
    mylist = []
    while True:
        try:
            x = int(input("Please, enter a number that is greater than 0:  "))
            if x > 0:
                mylist.append(x)
                if len(mylist) >= 2:
                    if mylist[0] > mylist[1] or mylist[0] == mylist[1]:
                        mylist.pop(1)
                    else:
                        mylist.pop(0)
                    print(f" The greater number for now is {mylist}")
            elif x == 0 or x < 0:
                if len(mylist) > 0:
                    break
                elif len(mylist) == 0:
                    print("Cannot find the largest value because no integers greater than 0 have been input")

        except ValueError:
            pass       # pass here to ensure the function won't crush if the user entered str


# Part Two:

def length(s):
    x = 0
    for i in s:
        x = x + 1
    return x


# Part Three:
def roll_dice(n_sides):
    x = random.randint(1, n_sides)
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
    choice = int(input("Please make your choice, and enter an option:  "))
    if choice == 1:
        print("You choose to find the max among a group of numbers you enter :)")
        find_max()
    elif choice == 2:
        print("you choose to calculate the length of a word :)")
        s = input("Please enter the word/sentence that you want to calculate its length:  ")
        result = length(s)
        print(f"The length of {s} is {result} ")

    elif choice == 3:
        print("you choose to roll a dice :)")
        n_sides = get_int("please enter the number of the sides:  ")
        default = 6
        if n_sides > 1 :
            result = roll_dice(n_sides)
            print(f"The dice says {result}")
        elif n_sides <= 1 :
            result = roll_dice(default)
            print(f"The dice says {result}")

    elif choice == 0:
        print("you choose to quit, Good Bye !")
        sys.exit()
    else:
        print("invalid number, Please choose from the menu")

