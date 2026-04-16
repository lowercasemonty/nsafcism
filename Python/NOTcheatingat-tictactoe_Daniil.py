import os

# VARIABLE LIST:
# scores: List to track scores, index 0 = X, index 1 = O
# Board_size: Variable for the size of the board (e.g. Board_size = 3 makes a 3x3 game)
# board: 2D array representing the current state of the board
# players: List to switch between who is X and who is O

scores = [0, 0]
Board_size = 3
board = [['□'] * Board_size for _ in range(Board_size)]
players = ["X", "O"]

def display_board():
    clear_board()
    for i in range(Board_size):
        for j in range(Board_size):
            print(board[i][j], end=" ")
        print()

# Clear_Board: Call to wipe the users terminal.
def clear_board():
    os.system('cls' if os.name == 'nt' else 'clear')

# Reset_Board: Call to reset ALL players moves.
def reset_board():
    global board
    board = [['□'] * Board_size for _ in range(Board_size)]

# Display_Scores: Call to print the current score to the terminal.
def display_scores():
    print("\n" + "="*30)
    print(f"Score: X: {scores[0]}, O: {scores[1]}")
    print("="*30 + "\n")


# PLAYER CODE
# Check_Valid: Call to see if the player inputs are both numbers, and within index range.
def check_valid(value):
    while True:
        if value.isdigit() and 1 <= int(value) <= Board_size:
            return int(value)
        value = input(f"Invalid input. Please enter a number between 1 and {Board_size}: ")

# Move: Call to receive inputs from players.
def move(player):
    while True:
        row = check_valid(input(f"Player {player}, Enter Row (1-{Board_size}): "))
        column = check_valid(input(f"Player {player}, Enter Column (1-{Board_size}): "))
        row_index = row - 1       # Convert input from 1-3 to 0-2 for indexing
        column_index = column - 1 # Convert input from 1-3 to 0-2 for indexing
        if not check_vacancy(row_index, column_index):
            print("This spot is taken. Try again.")
            continue
        board[row_index][column_index] = player
        break


# GAME CODE
# Check_Vacancy: Call to see if the position players entered is free.
def check_vacancy(row, column):
    return board[row][column] == "□"

# Check_Win: Call to scan the board for a 3 in a row.
def check_win(player):
    for i in range(Board_size):
        # Did a player win horizontally?
        if all(board[i][j] == player for j in range(Board_size)):
            return True
        # Did a player win vertically?
        if all(board[j][i] == player for j in range(Board_size)):
            return True
    # Did a player win diagonally?
    if all(board[i][i] == player for i in range(Board_size)):
        return True
    if all(board[i][Board_size - 1 - i] == player for i in range(Board_size)):
        return True
    return False

# Check_Draw: Call to see if all positions are filled.
def check_draw():
    for row in board:
        if "□" in row:
            return False
    return True

# Game: Main game loop: Shows board, takes player inputs, checks to see if they win, if not switch to the next player and repeat.
def game():
    while True:
        for i in range(len(players)):
            display_board()
            move(players[i])
            if check_win(players[i]):
                display_board()
                print(f"Player {players[i]} wins!")
                scores[i] += 1
                return
            if check_draw():
                display_board()
                print("It's a draw!")
                scores[0] += 0.5
                scores[1] += 0.5
                return

# Choose how many times you want to play, call game
games = input("How many games would you like to play: ")
while not games.isdigit() or int(games) % 2 == 0: # Check to see if the input is a number, then check to see if that number is odd
    print("Invalid input, please enter an odd number")
    games = input("How many games would you like to play: ")
games = int(games)

for i in range(games):
    game()
    display_scores()
    # Check if a player has won the majority of games selected
    majority = games // 2 + 1
    if scores[0] >= majority or scores[1] >= majority:
        winner = players[scores.index(max(scores))]
        print(f"Best of {games}, {winner} wins!")
        reset_board()
        break
    elif games > 1 and i < games - 1:
        input("Press 'enter' to continue: ")
    reset_board()