win = False

#Create Board
board = [['□','□','□'], ['□','□','□'], ['□','□','□']]
def display_board():
    for i in range(0,3):
        for j in range(0,3):
            print(board[i][j], end=" ")
        print()

#Action
def action(player):
    while True:
        down = int(input(f"Player {player}, enter down position (0-2): "))
        across = int(input("          enter across position (0-2): "))
        if board[down][across] != "□":
            print("This spot is taken")
            continue
        if player == "X":
            board[down][across] = "X"
        else:
            board[down][across] = "O"
        break
    check_win(player)

#Win Condition
def check_win(player):
    global win
    global winner
    for i in range(3):
        #Row Check
        if board[i][0] == board[i][1] == board[i][2] == (player):
            win = True
            winner = player
        #Column Check
        if board[0][i] == board[1][i] == board[2][i] == (player):
            win = True
            winner = player 
    #Diagonal Check
    if board[0][0] == board[1][1] == board[2][2] == (player):
        win = True
        winner = player
    if board[0][2] == board[1][1] == board[2][0] == (player):
        win = True
        winner = player

#Game Loop
while win == False:
    display_board()
    action("X")
    display_board()
    action("O")

print(f"Player {winner} wins!")
