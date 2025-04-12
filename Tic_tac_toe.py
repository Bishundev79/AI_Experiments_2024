# pylint: disable=all
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all([spot == player for spot in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False


def check_draw(board):
    return all([spot != " " for row in board for spot in row])


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        move = input(f"Player {current_player}, enter your move (row,col): ")
        try:
            row, col = map(int, move.split(','))
            row -= 1
            col -= 1

            if row not in range(3) or col not in range(3):
                print("Invalid move. Row and column must be between 1 and 3.")
                continue

            if board[row][col] != " ":
                print("Spot already taken, try again.")
                continue

            board[row][col] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break

            if check_draw(board):
                print_board(board)
                print("It's a draw!")
                break

            current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("Invalid input. Please enter the move as 'row,col'.")


if __name__ == "__main__":
    tic_tac_toe()