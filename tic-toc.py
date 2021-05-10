import sys


def getX(list_game):
    while True:
        try:
            row = int(input("Enter the row:  "))
            col = int(input("Enter the column:  "))
            if row in [0, 1, 2] and col in [0, 1, 2]:
                if list_game[row][col] == 0:
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
                if list_game[row][col] == 0:
                    list_game[row][col] = "O"
                    return list_game
                else:
                    print("Cannot play there!")
            else:
                print("Not in range, try again")
        except ValueError:
            print("Not an integer. Try again")


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


list_default = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]
                ]
print("Hello to this simple version of tic-toc game :) ")
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


