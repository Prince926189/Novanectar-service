def printBoard(xState, zState):
    # Create the board for printing
    board = [
        'X' if xState[i] else ('O' if zState[i] else str(i)) for i in range(9)
    ]
    
    # Print the board
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print(f"---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print(f"---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]}")

def checkWin(xState, zState):
    # Define all winning combinations
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    
    # Check if any winning combination for 'X' or 'O' exists
    for win in wins:
        if sum(xState[i] for i in win) == 3:
            print("X Won the match!")
            return 1
        if sum(zState[i] for i in win) == 3:
            print("O Won the match!")
            return 0
    return -1

if __name__ == "__main__":
    # Initialize game states for both players
    xState = [0] * 9
    zState = [0] * 9
    
    # Start with player X's turn
    turn = 1
    
    print("Welcome to Tic Tac Toe!")
    
    # Main game loop
    while True:
        printBoard(xState, zState)
        
        if turn == 1:
            print("player 1's Chance")
            value = int(input("Please enter a value (0-8): "))
            if xState[value] == 0 and zState[value] == 0:
                xState[value] = 1
            else:
                print("Invalid move! Try again.")
                continue
        else:
            print("palyer 2's Chance")
            value = int(input("Please enter a value (0-8): "))
            if xState[value] == 0 and zState[value] == 0:
                zState[value] = 1
            else:
                print("Invalid move! Try again.")
                continue

        # Check for win condition after every move
        cwin = checkWin(xState, zState)
        if cwin != -1:
            print("Match over")
            break

        # Switch turn between X and O
        turn = 1 - turn
