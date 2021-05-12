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


def getO(list_game):  # player O enter row & column valid values in empty places
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


def AI_getO(list_game):  # AI enter row & column random valid values in empty places
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if list_game[row][col] == " ":
            list_game[row][col] = "O"
            return list_game
        else:
            print("ops, it seems that I cannot play here!")


def print_game(yourlist):  # print the figure
    print(*yourlist[0], sep=' | ')
    print("__________")  # sep function learned from www.kite.com
    print(*yourlist[1], sep=' | ')
    print("----------")
    print(*yourlist[2], sep=' | ')


def gamex(list1, list2):
    print("PlayerX, it is your turn! ")
    list2 = getX(list1)
    print_game(list2)
    return list2


def gameO(list1, list2):
    print("PlayerO, it is your turn! ")
    list2 = getO(list1)
    print_game(list2)
    return list2


def gameAI(list1, list2):
    print("This is my play ! ")
    list2 = AI_getO(list1)
    print_game(list2)
    return list2


def check_winX(A):
    brek = 0
    for i in range(len(A)):
        if A[i][0] == A[i][1] == A[i][2] == "X" \
                or A[0][i] == A[1][i] == A[2][i] == "X" \
                or A[0][0] == A[1][1] == A[2][2] == "X" \
                or A[0][2] == A[1][1] == A[2][0] == "X":
            print("The winner is Player X")
            brek = 1
            break
    return brek


def check_winO(A):
    brek = 0
    for i in range(len(A)):
        if A[i][0] == A[i][1] == A[i][2] == "O" \
                or A[0][i] == A[1][i] == A[2][i] == "O" \
                or A[0][0] == A[1][1] == A[2][2] == "O" \
                or A[0][2] == A[1][1] == A[2][0] == "O":
            print("the winner is player O")
            brek = 1
            break
    return brek

    return


def play_again():
    while True:
        try:
            r = int(input("Do you want to play again enter 1 for yes, 0 for no:  "))
            if r == 1:
                return r
            elif r == 0:
                print("BYE BYE!")
                sys.exit()
            else:
                print("please enter 1 for yes, 0 for no:  ")
        except ValueError:
            print("please enter a valid choice 1 for yes, 0 for no")


def clear_board(yourlist):  # clear the board, it is not called successfully in the program
    yourlist = [[" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "]
                ]
    return yourlist


list_default = [[" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "]
                ]
roundX = [[" ", " ", " "],
          [" ", " ", " "],
          [" ", " ", " "]
          ]

roundO = [[" ", " ", " "],
          [" ", " ", " "],
          [" ", " ", " "]
          ]
menu = """
Hello, welcome to this simple version of Tic-Toc game.
Please, make your choice:
1.Player X VS player O
2.Player X VS AI 
"""
x = 0
o = 0
while True:
    print(menu)
    choice = int(input("Please, choose from the menu 1 or 2:  "))
    if choice == 1:
        again = 1
        # to be used when the user choose to play again
        while again == 1:
            win_countX = 0  # those parameters count the winning and losing
            win_countO = 0
            print("YOU CHOSE PLAYER X VS PLAYER O ")

            roundX = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]
                      ]
            roundO = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]
                      ]
            list_default = [[" ", " ", " "],
                            [" ", " ", " "],
                            [" ", " ", " "]
                            ]
            roundX = gamex(list_default, roundX)
            roundO = gameO(roundX, roundO)
            roundX = gamex(roundO, roundX)
            roundO = gameO(roundX, roundO)
            roundX = gamex(roundO, roundX)
            again = check_winX(roundX)
            if again == 1:
                win_countX = win_countX + 1
                print(f"Player X won {win_countX} times | Player O won {win_countO} times")
                again = play_again()
                continue
            roundO = gameO(roundX, roundO)
            again = check_winO(roundO)
            if again == 1:
                win_countO = win_countO + 1
                print(f"Player X won {win_countX} times | Player O {win_countO} times")
                again = play_again()
                continue
            roundX = gamex(roundO, roundX)
            again = check_winX(roundX)
            if again == 1:
                win_countX = win_countX + 1
                print(f"Player X won {win_countX} times | Player O won {win_countO} times")
                again = play_again()
                continue
            roundO = gameO(roundX, roundO)
            again = check_winO(roundO)
            if again == 1:
                win_countO = win_countO + 1
                print(f"Player X won {win_countX} times | Player 0 won {win_countO} times")
                again = play_again()
                continue
            roundX = gamex(roundO, roundX)
            again = check_winX(roundX)
            if again == 1:
                win_countX = win_countX + 1
                print(f"Player X won {win_countX} times | Player O won {win_countO} times")
                again = play_again()
                continue
            print("it is a tie")
            print(f"Player X won {win_countX} times | Player O won {win_countO} times")
            again = play_again()
    elif choice == 2:
        again = 1
        while again == 1:
            win_countX = 0
            win_countO = 0
            print("YOU CHOSE User VS AI ")

            roundX = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]
                      ]
            roundO = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]
                      ]
            list_default = [[" ", " ", " "],
                            [" ", " ", " "],
                            [" ", " ", " "]
                            ]
            roundX = gamex(list_default, roundX)
            roundO = gameAI(roundX, roundO)
            roundX = gamex(roundO, roundX)
            roundO = gameAI(roundX, roundO)
            roundX = gamex(roundO, roundX)
            again = check_winX(roundX)
            if again == 1:
                win_countX = win_countX + 1
                print(f"Player X won {win_countX} times | AI won {win_countO} times")
                again = play_again()
                continue
            roundO = gameAI(roundX, roundO)
            again = check_winO(roundO)
            if again == 1:
                win_countO = win_countO + 1
                print(f"Player X won {win_countX} times | AI won {win_countO} times")
                again = play_again()
                continue
            roundX = gamex(roundO, roundX)
            again = check_winX(roundX)
            if again == 1:
                win_countX = win_countX + 1
                print(f"User won {win_countX} times | AI won {win_countO} times")
                again = play_again()
                continue
            roundO = gameAI(roundX, roundO)
            again = check_winO(roundO)
            if again == 1:
                win_countO = win_countO + 1
                print(f"User won {win_countX} times | AI won {win_countO} times")
                again = play_again()
                continue
            roundX = gamex(roundO, roundX)
            again = check_winX(roundX)
            if again == 1:
                win_countX = win_countX + 1
                print(f"User won {win_countX} times | AI won {win_countO} times")
                again = play_again()
                continue
            print("it is a tie")
            print(f"User won {win_countX} times | AI won {win_countO} times")
            again = play_again()
    else:
        print("Please, choose from the menu 1, OR 2 ")
