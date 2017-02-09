import random

gameOver = False
round = 1
winner = ""
draw = False
count = 0
list = ["__1__|__2__|__3__", "__4__|__5__|__6__", "  7  |  8  |  9  "]

def check_board():
    global winner
    global gameOver
    global draw
    i = 2
    count = 0

    #check lines
    for line in list:
        if line[2] == "X":
            if line[8] == "X":
                if line[14] == "X":
                    winner = "Player X"
                    gameOver = True
                    return
        elif line[2] == "O":
            if line[8] == "O":
                if line[14] == "O":
                    winner = "Player O"
                    gameOver = True
                    return
        else:
            pass

    #check columns
    for line in list:
        if list[0][i] == "X":
            if list[1][i] == "X":
                if list[2][i] == "X":
                    winner = "Player X"
                    gameOver = True
                    return
        elif list[0][i] == "O":
            if list[1][i] == "O":
                if list[2][i] == "O":
                    winner = "Player O"
                    gameOver = True
                    return
        else:
            pass
        i += 6

    #check diagonal lines
    if list[0][2] == "X":
        if list[1][8] == "X":
            if list[2][14] == "X":
                winner = "Player X"
                gameOver = True
                return
    elif list[0][2] == "O":
        if list[1][8] == "O":
            if list[2][14] == "O":
                winner = "Player O"
                gameOver = True
                return
    else:
        pass
    if list[0][14] == "X":
        if list[1][8] == "X":
            if list[2][2] == "X":
                winner = "Player X"
                gameOver = True
                return
    elif list[0][14] == "O":
        if list[1][8] == "O":
            if list[2][2] == "O":
                winner = "Player O"
                gameOver = True
                return
    else:
        pass

    #check draw
    for line in list:
        if (line[2] == "X" or line[2] == "O") and (line[8] == "X" or line[8] == "O") and (line[14] == "X" or line[14] == "O"):
            count += 1
        if count == 3:
            draw = True
            gameOver = True
            return

    return


def print_board():
    for line in list:
        print line
    return


while not gameOver:
    if round == 1:
        print "Game Start!"
        print "******** Round: 1 ********"
        print_board()
        if random.randint(0, 1) == 0:
            print "Player X goes first. Please enter a number: "
        else:
            print "Player O goes first. Please enter a number: "
    else:
        print "******** Round: %d ********" % round
        print_board()
        if count % 2 == 0:
            print "Player X's turn. Please enter a number: "
        else:
            print "Player O's turn. Please enter a number: "

    input = raw_input()

    for line in list:
        for num in line:
            if num == input:
                if count % 2 == 0:
                    list[list.index(line)] = line.replace(num, "X")
                else:
                    list[list.index(line)] = line.replace(num, "O")


    check_board()
    round += 1
    count += 1

if draw == True:
    print_board()
    print "The game is a draw!!!"
else:
    print_board()
    print winner + " is the winner of the game!!! :D"

