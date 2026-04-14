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
        if player == 1:
            board[down][across] = "X"
        else:
            board[down][across] = "O"
        break

#Win Condition
def check_win():
    for i in range (2):
        #Row Check
        for j in range(3):
            if board[i][j] == board[i+1][j] and board[i][j] != "□":
                win = True
                return win
        #Column Check
        for j in range(3):
            if board[j][i] == board[j][i+1] and board[j][i] != "□":
                win = True
                return win


#Game Loop
while win == False:
    display_board()
    action(1)
    check_win()
    display_board()
    action(2)
    check_win()

print("End")
