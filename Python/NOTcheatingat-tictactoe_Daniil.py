import os

#BOARD CODE 
#Create Board
board = [['□','□','□'], ['□','□','□'], ['□','□','□']]
def display_board():
    clear_board()
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=" ")
        print()

#Clear Board
def clear_board():
    os.system('cls' if os.name == 'nt' else 'clear')

#Reset Board
def reset_board():
    global board
    board = [['□','□','□'], ['□','□','□'], ['□','□','□']]


#PLAYER CODE
players = ["X", "O"]
#Player moves
def move(player):
    while True:
        row = check_valid(input(f"Player {player}, Enter Row (1-3): "))
        column = check_valid(input(f"Player {player}, Enter Column (1-3): "))
        row_index = row - 1 #Convert input to from 1-3 to 0-2 for indexing
        column_index = column - 1 #Convert input to from 1-3 to 0-2 for indexing
        if not check_vacancy(row_index, column_index):
            print("This spot is taken. Try again.")
            continue
        board[row_index][column_index] = player
        break

#GAME CODE
#Is the input a number between 1 and 3?
def check_valid(value):
    while True:
        if value.isdigit() and 1 <= int(value) <= 3:
            return int(value)
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

#Main Game Loop
def game():
    for i in range(len(players)):
        display_board()
        move(players[i])
        if check_win(players[i]):
            display_board()
            print(f"Player {players[i]} wins!")
            return
        if check_draw():
            display_board()
            print("It's a draw!")
            return

#Choose how many times you want to play, call game
games = input("How many games would you like to play: ")
while not games.isdigit() or int(games) % 2 == 0: #Check to see if the input is a number, then check to see if that number is odd 
    print("Invalid input, please enter an odd number")
    games = input("How many games would you like to play: ")
games = int(games)
for i in range (games):
    game()
    if games > 1 and i < games:
        input("Press 'enter' to continue: ")
    reset_board()
