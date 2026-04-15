board = [[0,0,0], [0,0,0], [0,0,0]]
player_no = "1"

def move(player_no):
    print(f"Player {player_no} turn:")
    while True:
        down_input = input("enter down position (0-2): ")
        if down_input.isdigit() and int(down_input) in (0, 1, 2):
            down = int(down_input)
            break
        else:
            print("Please choose a valid coordinate on the board")
            continue
    
    while True:
        across_input = input("enter across position (0-2): ")
        if across_input.isdigit() and int(across_input) in (0, 1, 2):
            across = int(across_input)
            break
        else:
            print("Please choose a valid coordinate on the board")
            continue
    return down, across

def is_draw():
    for row in board:
        if 0 in row:
            return False
    return True

def print_board():
    print("Current Board: \n-----------------")
    for i in range(3):
        for j in range(3):
            print("|", board[i][j], end=" | ")
        print("\n-----------------")

def has_won():
    # Check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != 0:
            return True
        
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != 0:
            return True
        
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return True
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return True
    
    return False

def player_turn(player_no):
    down, across = move(player_no)
    while board[down][across] != 0:
        print("Space is taken, please choose a different space.")
        down, across = move(player_no)
    if player_no == "1":
        board[down][across] = "X"
    if player_no == "2":
        board[down][across] = "O"
    print_board()

# Start Gameplay loop

print_board()
while True:
    player_turn("1")
    if has_won():
        print("Player 1 wins!")
        break
    
    # Check if its a draw (only have to after player 1 turn because theres odd spaces to play on)
    if is_draw():
        print("It's a draw!")
        break

    player_turn("2")
    if has_won():
        print("Player 2 wins!")
        break