#Create Board
board = [[0,0,0], [0,0,0], [0,0,0]]
for i in range(0,3):
    for j in range(0,3):
        print(board[i][j], end=" ")
    print()

#Player Turns
def player1():
    while True:
        down = int(input("Player 1, enter down position (0-2): "))
        across = int(input("          enter across position (0-2): "))
        if board[down][across] != 0:
            print("This spot is taken")
            continue
        board[down][across] = 1
        break

def player2():
    while True:
        down = int(input("Player 2, enter down position (0-2): "))
        across = int(input("          enter across position (0-2): "))
        if board[down][across] != 0:
            print("This spot is taken")
            continue
        board[down][across] = 1
        break

#Game Loop
while True:
    player1()
    player2()
