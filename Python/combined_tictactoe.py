# Stylistic choices taken from: NOTcheatingat-tictactoe-Chris.py (class structure, game selection) 
# and NOTcheatingat-tictactoe_Daniil.py (terminal management, advanced win checking)
import os

# VARIABLE LIST:
# scores: Dictionary to track scores for X and O
# board_size: Variable for the size of the board (default 3x3)
# board: 2D array representing the current state of the board
# players: List to switch between who is X and who is O
# gameID: Selected game ID from the menu
# games: Number of games to play in the current match
# games_played: How many games have been played so far in the current match
# winner: Match winner once the majority is reached

ttt_scores = {"X": 0, "O": 0}
ttt_board_size = 3
ttt_board = [[0 for _ in range(ttt_board_size)] for _ in range(ttt_board_size)]
ttt_players = ["X", "O"]

def clear_board():
    """Call to wipe the user's terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def reset_board():
    """Call to reset all player's moves."""
    global ttt_board
    ttt_board = [[0 for _ in range(ttt_board_size)] for _ in range(ttt_board_size)]

def print_board():
    """Function to print the current state of the board in a nice format."""
    clear_board()
    print("Current Board:\n" + "-" * 13)
    for i in range(ttt_board_size):
        for j in range(ttt_board_size):
            symbol = ttt_board[i][j] if ttt_board[i][j] != 0 else " "
            print("|", symbol, end=" ")
        print("|")
        print("-" * 13)

def display_scores():
    """Call to print the current score to the terminal."""
    print("\n" + "="*30)
    print(f"Score: X: {ttt_scores['X']}, O: {ttt_scores['O']}")
    print("="*30 + "\n")

def check_valid(value, board_size):
    """Call to see if the player inputs are numbers and within valid range."""
    while True:
        if value.isdigit() and 0 <= int(value) <= board_size:
            return int(value)
        else:
            value = input(f"Please choose a valid coordinate on the board (1-{board_size}): ")

def move(player):
    """Call to receive inputs from players."""
    while True:
        down = check_valid(input(f"Player {player}, enter row position (1-{ttt_board_size}): "), ttt_board_size)
        across = check_valid(input(f"Player {player}, enter column position (1-{ttt_board_size}): "), ttt_board_size)
        down = down - 1
        across = across - 1
        
        if ttt_board[down][across] != 0:
            print("Space is taken, please choose a different space.")
            continue
        ttt_board[down][across] = player
        break

def check_win(player):
    """Call to scan the board for a winning condition."""
    # Check rows
    for row in range(ttt_board_size):
        if all(ttt_board[row][col] == player for col in range(ttt_board_size)):
            return True
    
    # Check columns
    for col in range(ttt_board_size):
        if all(ttt_board[row][col] == player for row in range(ttt_board_size)):
            return True
    
    # Check diagonals
    if all(ttt_board[i][i] == player for i in range(ttt_board_size)):
        return True
    if all(ttt_board[i][ttt_board_size - 1 - i] == player for i in range(ttt_board_size)):
        return True
    
    return False

def check_draw():
    """Call to see if all positions are filled."""
    for row in ttt_board:
        if 0 in row:
            return False
    return True

def tictactoe():
    """Main game loop: Shows board, takes player inputs, checks for winner or draw."""
    global ttt_board
    reset_board()
    print_board()
    
    while True:
        for player in ttt_players:
            print_board()
            move(player)
            
            if check_win(player):
                print_board()
                print(f"Player {player} wins!")
                ttt_scores[player] += 1
                return player
            
            if check_draw():
                print_board()
                print("It's a draw!")
                return None

class GameSelection:
    """Class for game selection and management."""
    def __init__(self):
        self.gameID = None
        self.games = 0
        self.games_played = 0
        self.winner = ""
        self.games_list = {1: "Tic Tac Toe", 2: "Example 2", 3: "Example 3"}
        self.launch_list = {1: tictactoe, 2: None, 3: None}
    
    def game_selection(self):
        """Method to handle game selection."""
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
        return self.gameID
    
    def game_count(self):
        """Method to ask user how many games they want to play"""
        # Choose how many times you want to play, call game
        games = input("How many games would you like to play: ")
        while not games.isdigit() or int(games) % 2 == 0: # Check to see if the input is a number, then check to see if that number is odd
            print("Invalid input, please enter an odd number")
            games = input("How many games would you like to play: ")
        games = int(games)
        return games
    
    def majority(self):
            majority = self.games // 2 + 1
            if ttt_scores["X"] >= majority or ttt_scores["O"] >= majority:
                winner = max(ttt_scores, key=ttt_scores.get)
                print(f"Best of {self.games}, {winner} wins!")
                return winner
            elif self.games_played != self.games - 1:
                display_scores()
                input("Press 'enter' to continue: ")
            return None
    
    def launch(self):
        """Method to launch the selected game."""
        if self.gameID in self.launch_list and self.launch_list[self.gameID]:
            print(f"Starting {self.games_list[self.gameID]}, best of {self.games}")
            for i in range(self.games):
                self.launch_list[self.gameID]()
                self.games_played += 1
                match_winner = self.majority()
                if match_winner:
                    self.winner = match_winner
                    break
    
    def run(self):
        """Method to run the game selector and launch the game."""
        ttt_scores["X"] = 0
        ttt_scores["O"] = 0
        self.game_selection()
        self.games = self.game_count()
        self.launch()

# Create an instance of the GameSelection class
selector = GameSelection()

# Code to run the game selector
while True:
    selector.run()
    display_scores()
    play_again = input("Thanks for playing!\nPlay again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing! Goodbye!")
        break
    reset_board()