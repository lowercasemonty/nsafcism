win = False
draw = False

#Create Board
board = [['□','□','□'], ['□','□','□'], ['□','□','□']]
def display_board():
    for i in range(0,3):
        for j in range(0,3):
            print(board[i][j], end=" ")
        print()

#Action
def action(player):
    display_board()
    while True:
        #Get Inputs
        down = input(f"Player {player}, enter down position (0-2): ")
        check_valid(down)
        across = input("          enter across position (0-2): ")
        check_valid(across)
        down = int(down)
        across = int(across)
        #Check Vacancy
        if board[down][across] != "□":
            print("This spot is taken")
            continue
        if player == "X":
            board[down][across] = "X"
        else:
            board[down][across] = "O"
        break
    #Check Win/Draw
    check_win(player)

#Valid input
def check_valid(a):
    while a not in ["0", "1", "2"]:
        if not a.isdigit():
            display_board()
            a = input("Please enter a number between 0 and 2: ")
        else:
            return a

#Output
def output(player):
    global win
    global winner
    win = True
    winner = player

#Win Condition
def check_win(player):
    for i in range(3):
        #Row Check
        if board[i][0] == board[i][1] == board[i][2] == (player):
            output(player)
        #Column Check
        if board[0][i] == board[1][i] == board[2][i] == (player):
            output(player)
    #Diagonal Check
    if board[0][0] == board[1][1] == board[2][2] == (player):
        output(player)
    if board[0][2] == board[1][1] == board[2][0] == (player):
        output(player)
    if win == False:
        check_draw()

def check_draw():
    global draw
    for i in range(3):
        for j in range(3):
            if board[i][j] == "□":
                return
    draw = True

#Game Loop
while not win and not draw:
    if win == False:
        action("X")
    if win == False:
        action("O")

if win == True:
    display_board()
    print(f"Player {winner} wins!")
if draw == True:
    display_board()
    print("No spaces left, Draw!")