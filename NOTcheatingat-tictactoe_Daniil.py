import os

#BOARD CODE 
#Create Board
board = [['□','□','□'], ['□','□','□'], ['□','□','□']]
draw = False

def display_board():
    clear_board()
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=" ")
        print()

#Clear Board
def clear_board():
    os.system('cls' if os.name == 'nt' else 'clear')


#PLAYER CODE
#Player moves
def move(player):
    while True:
        row = check_valid(input(f"Player {player}, Enter Row (1-3): "))
        column = check_valid(input(f"Player {player}, Enter Column (1-3): "))
        row_index = int(row) - 1 #Convert input to from 1-3 to 0-2 for indexing
        column_index = int(column) - 1 #Convert input to from 1-3 to 0-2 for indexing
        if not check_vacancy(row_index, column_index):
            print("This spot is taken. Try again.`")
            continue
        board[row_index][column_index] = player
        break

#GAME CODE
#Is the input a number between 1 and 3?
def check_valid(value):
    while True:
        if value.isdigit() and 1 <= int(value) <= 3:
            return value
        display_board()
        value = input("Invalid input. Please enter a number between 1 and 3: ")
#Is this available?
def check_vacancy(row, column):
    return board[row][column] == "□"
#Check if the player has won
def check_win(player):
    for i in range(3):
        #Did a player win horizontally?
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        #Did a player win vertically?
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    #Did a player win diagonally?
    if board[0][0] == board[1][1] == board[2][2] == player: 
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

#Check if the board is full
def check_draw():
    for row in board:
        if "□" in row:
            return False
    return True

#Reset the board
def reset_board():
    global board
    board = [['□','□','□'], ['□','□','□'], ['□','□','□']]

#Score
def score(player):
    if check_win(player):
        return 1
    elif check_draw():
        return 0.5
    else:
        return 0

#Main Game Loop
def game():
    games = int(input("How many games would you like to play?: "))
    while games % 2 != 1:
        games = int(input("Number cannot be even, please input an Odd Number: "))
    if games > 1:
        print(f"Current Score: Player X: {score('X')} | Player O: {score('O')}")
    for i in range (games):
        while True:
            players = ["X", "O"]
            for i in range(len(players)):
                display_board()
                move(players[i])
                if check_win(players[i]):
                    display_board()
                    print(f"Player {players[i]} wins!")
                    break
                if check_draw():
                    display_board()
                    print("It's a draw!")
                    break
    reset_board()

#Call Game
game()
