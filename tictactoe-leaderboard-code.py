leaderboard = [[0],[0]]

def print_leaderboard():
    print("Current Leaderboard: Updated now \n Player 1 | Player 2 |")
    for i in range(2):
        for j in range(1):
            print("", leaderboard[i][j], end="        |")

