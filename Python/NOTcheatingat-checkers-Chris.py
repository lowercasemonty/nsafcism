import os

# VARIABLE LIST:
# scores: Dictionary to track scores for X and O
# board_size: Variable for the size of the board (default 3x3)
# board: 2D array representing the current state of the board
# players: List to switch between who is playing as B and W

scores = {"B": 0, "W": 0}
board_size = 8
board = [[0 for _ in range(board_size)] for _ in range(board_size)]
players = ["B","W"]

def clear_board():
    """Call to wipe the user's terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board():
    """Function to print the current state of the board in a nice format."""
    clear_board()
    print("Current Board:\n" + "-" * 33)
    for i in range(board_size):
        for j in range(board_size):
            symbol = board[i][j] if board[i][j] != 0 else " "
            print("|", symbol, end=" ")
        print("|")
        print("-" * 33)

def setup_board():
    global board
    for row in range(board_size):
        for col in range(board_size):
            if (row + col) % 2 != 0:
                if row < 3:
                    board[row][col] = "W"
                elif row > 4:
                    board[row][col] = "B"
                else:
                    continue

def select_piece(player):
    return

def move(player):
    return





setup_board()
print_board()