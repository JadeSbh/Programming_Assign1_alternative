import sys  #www.geeksforgeeks.com
import random


def getX(list_game):
    while True:
        try:
            row = int(input("Enter the row:  "))
            col = int(input("Enter the column:  "))
            if row in [0, 1, 2] and col in [0, 1, 2]:
                if list_game[row][col] == " ":
                    list_game[row][col] = "X"
                    return list_game
                else:
                    print("Cannot play there!")
            else:
                print("Not in range, try again")
        except ValueError:
            print("Not an integer. Try again")


def getO(list_game):
    while True:
        try:
            row = int(input("Enter the row:  "))
            col = int(input("Enter the column:  "))
            if row in [0, 1, 2] and col in [0, 1, 2]:
                if list_game[row][col] == " ":
                    list_game[row][col] = "O"
                    return list_game
                else:
                    print("Cannot play there!")
            else:
                print("Not in range, try again")
        except ValueError:
            print("Not an integer. Try again")


def AU_getO(list_game):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if list_game[row][col] == " ":
            list_game[row][col] = "O"
            return list_game
        else:
            print("opps, it seems that I cannot play here, I am not that smart yet!")


def print_game(yourlist):   #www.kite.com
    print(*yourlist[0], sep=' | ')
    print("__________")
    print(*yourlist[1], sep=' | ')
    print("----------")
    print(*yourlist[2], sep=' | ')


def check_winX(A):
    for i in range(len(A)):
        if A[i][0] == A[i][1] == A[i][2] == "X" \
                or A[0][i] == A[1][i] == A[2][i] == "X" \
                or A[0][0] == A[1][1] == A[2][2] == "X" \
                or A[0][2] == A[1][1] == A[2][0] == "X":
            return 1


def play_again():
    while True:
        try:
            x = int(input("Do you want to play again enter 1 for yes, 0 for no:  "))
            if x == 1:
                return x
            elif x==0:
               print("BYE BYE!")
               sys.exit()
            else:
                print("please enter 1 for yes, 0 for no:  ")
        except ValueError:
            print("please enter a valid choice 1 for yes, 0 for no")

def check_winO(A):
    for i in range(len(A)):
        if A[i][0] == A[i][1] == A[i][2] == "O" \
                or A[0][i] == A[1][i] == A[2][i] == "O" \
                or A[0][0] == A[1][1] == A[2][2] == "O" \
                or A[0][2] == A[1][1] == A[2][0] == "O":
            return 1


list_default = [[" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "]
                ]
menu = """
Hello, welcome to this simple version of Tic-Toc game.
Please, make your choice:
1.Player X VS player O
2.Player X VS AI 
"""
while True:
    print(menu)
    choice = int(input("Please, choose from the menu 1 or 2:  "))
    if choice == 1:
        again = 1
        while again == 1:
            win_countX = 0
            win_countO = 0
            print("YOU CHOSE PLAYER X VS PLAYER O ")
            print("player X plays first")
            roundX = getX(list_default)
            print_game(roundX)
            for i in range(0, 4):
                print("Player O, it's your turn now ")
                roundO = getO(roundX)
                print_game(roundO)
                winner = check_winO(roundX)
                if winner == 1:
                    print("The winner is player O")
                    win_countO = win_countO + 1
                    play_again()
                print("Player X, it's your turn now ")
                roundX = getX(roundO)
                print_game(roundX)
                winner = check_winX(roundX)
                if winner == 1:
                    print("The winner is player X")
                    win_countX = win_countX + 1
                    play_again()
            print("it is a tie")
            play_again()
    elif choice == 2:
        again = 1
        while again == 1:
            win_countX = 0
            win_countO = 0
            print("you chose to play with the computer")
            user = input("Please enter your name: ")
            print(f"{user}, you play first")
            roundX = getX(list_default)
            print_game(roundX)
            for i in range(0, 4):
                print("AU , This is my play ")
                roundO = AU_getO(roundX)
                print_game(roundO)
                winner = check_winO(roundX)
                if winner == 1:
                    print("The winner is player O")
                    win_countO = win_countO + 1
                    print(f"The AU won {win_countO} times | {user} won {win_countX} times")
                    play_again()
                    continue
                print(f"{user}, it's your turn now ")
                roundX = getX(roundO)
                print_game(roundX)
                winner = check_winX(roundX)
                if winner == 1:
                    print("The winner is player X")
                    win_countX = win_countX + 1
                    print(f"The AU won {win_countO} times | {user} won {win_countX} times")
                    play_again()
                    continue
            else:
                print("it is a tie")
                play_again()
    else:
        print("Please, choose from the menu 1, OR 2 ")
