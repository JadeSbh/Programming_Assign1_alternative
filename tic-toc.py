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
    print(yourlist[0])
    print("__________")
    print(yourlist[1])
    print("----------")
    print(yourlist[2])


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
roundO = getX(roundX)
print_game(roundO)
print("Player X, it's your turn now :) ")
roundX = getX(roundO)
print_game(roundX)


