def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def player_input(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("Cell already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Enter a number between 1 and 9.")

def check_win(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def main():
    while True:
        board = [[" "] * 3 for _ in range(3)]
        for turn in range(9):
            display_board(board)
            player = "X" if turn % 2 == 0 else "O"
            player_input(board, player)
            if check_win(board, player):
                display_board(board)
                print(f"Player {player} wins!")
                break
        else:
            display_board(board)
            print("It's a draw!")
        
        if input("Play again? (y/n): ").lower() != "y":
            break

if __name__ == "__main__":
    main()
