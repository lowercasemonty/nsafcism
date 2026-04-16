# Constants
tictactoe_board = [[0,0,0], [0,0,0], [0,0,0]]

# Functions

# Function to print the current state of the board in a nice format

def print_tictactoe_board():
    print("Current Board: \n-----------------")
    for i in range(3):
        for j in range(3):
            print("|", tictactoe_board[i][j], end=" | ")
        print("\n-----------------")
        

# Function to handle a player's turn by getting their move, validating that the space is not already taken, 
# and updating the board with their symbol (X for player 1 and O for player 2)

def player_turn(player_no):
    down, across = move(player_no)
    while tictactoe_board[down][across] != 0:
        print("Space is taken, please choose a different space.")
        down, across = move(player_no)
    if player_no == "1":
        tictactoe_board[down][across] = "X"
    elif player_no == "2":
        tictactoe_board[down][across] = "O"
    print_tictactoe_board()

# Function to get player move and validate input
# This function will loop until the player inputs a valid coordinate on the board (0-2 for both down and across)

def move(player_no):
    print(f"Player {player_no} turn:")
    
    def get_coordinate(coordinate_name):
        while True:
            input_val = input(f"enter {coordinate_name} position (0-2): ")
            if input_val.isdigit() and int(input_val) in (0, 1, 2):
                return int(input_val)
            else:
                print("Please choose a valid coordinate on the board")
    down = get_coordinate("down")
    across = get_coordinate("across")
    return down, across

# Function to check if a player has won by checking all rows, columns, and diagonals for three of the same non-zero symbol (X or O)

def has_won():
    # Check rows
    for row in range(3):
        if tictactoe_board[row][0] == tictactoe_board[row][1] == tictactoe_board[row][2] != 0:
            return True
        
    # Check columns
    for col in range(3):
        if tictactoe_board[0][col] == tictactoe_board[1][col] == tictactoe_board[2][col] != 0:
            return True
        
    # Check diagonals
    if tictactoe_board[0][0] == tictactoe_board[1][1] == tictactoe_board[2][2] != 0:
        return True
    if tictactoe_board[0][2] == tictactoe_board[1][1] == tictactoe_board[2][0] != 0:
        return True
    
    return False

# Function to check if the game is a draw (no more spaces to play on)

def is_draw():
    for row in tictactoe_board:
        if 0 in row:
            return False
    return True

# Start TicTacToe Gameplay loop
# The game will continue until either player 1 wins, player 2 wins, or the game is a draw.
# Game will only check if its a draw after player 1 turn because theres odd spaces to play on.

def tictactoe():
    global tictactoe_board
    tictactoe_board = reset_tictactoe_board()
    winner = None
    print_tictactoe_board()
    while True:
        player_turn("1")
        if has_won():
            print("Player 1 wins!")
            winner = "1"
            break
        
        if is_draw():
            print("It's a draw!")
            winner = None
            break

        player_turn("2")
        if has_won():
            print("Player 2 wins!")
            winner = "2"
            break
    return winner

# Reset board in between games

def reset_tictactoe_board():
    global tictactoe_board
    tictactoe_board = [[0,0,0], [0,0,0], [0,0,0]]

# Classes (oho fancy fancy)

# Class for game selection
class GameSelection:
    def __init__(self):
        self.gameID = None
        self.games_list = {1: "Tic Tac Toe", 2: "Example 2", 3: "Example 3"} # List of Available Games
        self.launch_list = {1: tictactoe, 2: None, 3: None} # Functions to launch said games
        self.scores = {"1": 0, "2": 0} # Dictionary to keep track of total player wins across games for a leaderboard
    
    def game_selection(self):
        while True:
            print("\nWhat game would you like to play?")
            for game_id, game_name in self.games_list.items():
                print(f"{game_id} = {game_name}")
            game_choice = input("Enter game id: ")
            if game_choice.isdigit() and int(game_choice) in self.games_list:
                    self.gameID = int(game_choice)
                    break
            else:
                    print("That's not a valid game ID, please try again.")
                    continue
        return self.gameID
    
    def launch(self):
        if self.gameID in self.launch_list:
            print(f"Starting {self.games_list[self.gameID]}")
            self.launch_list[self.gameID]()
    
    def run(self):
        self.game_selection()
        self.launch()
    
    def update_scores(self, winner):
        if winner and winner in self.scores:
            self.scores[winner] += 1

# Create an instance of the GameSelection class to run the game selector 
selector = GameSelection()


# Code to run the game selector and then print a thank you message after the game is done
while True:
    selector.run()
    play_again = input("Thanks for playing!\nPlay again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing! Goodbye!")
        break
    reset_tictactoe_board()