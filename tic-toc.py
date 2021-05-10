import sys
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


def print_game(yourlist):
    print(*yourlist[0], sep=' | ')
    print("__________")
    print(*yourlist[1], sep=' | ')
    print("----------")
    print(*yourlist[2], sep=' | ')


def check_win(A):
    for i in range(len(A)):
        if A[i][0] == A[i][1] == A[i][2] \
                or A[0][i] == A[1][i] == A[2][i] \
                or A[0][0] == A[1][1] == A[2][2] \
                or A[0][2] == A[1][1] == A[2][0]:
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
3.quit
"""
while True:
    print(menu)
    choice = int(input("Please, choose from the menu 1,2 or 0 to quit:  "))
    if choice == 1:
        print("YOU CHOSE PLAYER X VS PLAYER O ")
        print("player X plays first")
        roundX = getX(list_default)
        print_game(roundX)
        print("Player O, it's your turn now ")
        roundO = getO(roundX)
        print_game(roundO)
        print("Player X, it's your turn now ")
        roundX = getX(roundO)
        print_game(roundX)
        print("Player O, it's your turn now :) ")
        roundO = getO(roundX)
        print_game(roundO)
        print("Player X, it's your turn now :) ")
        roundX = getX(roundO)
        print_game(roundX)
        winner = check_win(roundX)
        if winner == 1:
            print("The winner is player X")

        else:
            print("Player O, it's your turn now :) ")
            roundO = getO(roundX)
            print_game(roundO)
            winner = check_win(roundO)
            if winner == 1:
                print("The winner is player O")
                sys.exit()
            else:
                print("Player X, it's your turn")
                roundX = getX(roundO)
                print_game(roundX)
                winner = check_win(roundX)
                if winner == 1:
                    print("The winner is player X")
                    sys.exit()
                else:
                    print("Player O, it's your turn now :) ")
                    roundO = getO(roundX)
                    print_game(roundO)
                    winner = check_win(roundO)
                    if winner == 1:
                        print("The winner is player O")
                        sys.exit()
                    else:
                        print("Player X, it's your turn")
                        roundX = getX(roundO)
                        print_game(roundX)
                        winner = check_win(roundX)
                        if winner == 1:
                            print("The winner is player X")
                            sys.exit()
                        else:
                            print("it is a tie")
    elif choice == 2:
        print("you chose to play with the computer")
        print("player X, you play first")
        roundX = getX(list_default)
        print_game(roundX)
        print("AU , This is my play ")
        roundO = AU_getO(roundX)
        print_game(roundO)
        print("Player X, it's your turn now ")
        roundX = getX(roundO)
        print_game(roundX)
        print("AU , This is my play")
        roundO = AU_getO(roundX)
        print_game(roundO)
        print("Player X, it's your turn now :) ")
        roundX = getX(roundO)
        print_game(roundX)
        winner = check_win(roundX)
        if winner == 1:
            print("The winner is player X")

        else:
            print("AU , it's your turn now :) ")
            roundO = AU_getO(roundX)
            print_game(roundO)
            winner = check_win(roundO)
            if winner == 1:
                print("The winner is player O")
                sys.exit()
            else:
                print("Player X, it's your turn")
                roundX = getX(roundO)
                print_game(roundX)
                winner = check_win(roundX)
                if winner == 1:
                    print("The winner is player X")
                    sys.exit()
                else:
                    print("AU , This is my play: ")
                    roundO = AU_getO(roundX)
                    print_game(roundO)
                    winner = check_win(roundO)
                    if winner == 1:
                        print("The winner is player O")
                        sys.exit()
                    else:
                        print("Player X, it's your turn")
                        roundX = getX(roundO)
                        print_game(roundX)
                        winner = check_win(roundX)
                        if winner == 1:
                            print("The winner is player X")
                            sys.exit()
                        else:
                            print("it is a tie")
    elif choice == 0:
        print("BYe BYE !")
        break
    else:
        print("Please, choose from the menu 1, 2, or 0 to quit")
