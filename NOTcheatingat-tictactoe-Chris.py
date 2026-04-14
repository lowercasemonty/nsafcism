board = [[0,0,0], [0,0,0], [0,0,0]]
player_no = "1"

def move(player_no):
    down = int(input(f"Player {player_no}, enter down position (0-2): "))
    while down != 0 and down != 1 and down != 2:
        print("Please choose a valid position on the board")
        down = int(input(f"Player {player_no}, enter down position (0-2): "))
    
    across = int(input("          enter across position (0-2): "))
    while across != 0 and across != 1 and across != 2:
        print("Please choose a valid position on the board")
        across = int(input(f"Player {player_no}, enter across position (0-2): "))
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
        # if, in a given list(row) within the list(board), all 3 values equal each other (and not 0), return True
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
<<<<<<< HEAD:NOTcheatingat-tictactoe

    player_turn("2")
    if has_won():
        print("Player 2 wins!")
        break
=======
>>>>>>> bf5b909d3114eb2d819ca84c8d698d7e2dc3fd52:NOTcheatingat-tictactoe-Chris.py
