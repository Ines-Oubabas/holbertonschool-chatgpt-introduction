#!/usr/bin/python3
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Vérification des lignes et des colonnes
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True

    # Vérification des diagonales
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    players = ["X", "O"]
    current_player = players[0]

    while not check_winner(board):
        print_board(board)
        row = int(input("Enter row (0, 1, or 2) for player " + current_player + ": "))
        col = int(input("Enter column (0, 1, or 2) for player " + current_player + ": "))

        if 0 <= row < 3 and 0 <= col < 3:
            if board[row][col] == " ":
                board[row][col] = current_player
                current_player = players[(players.index(current_player) + 1) % 2]
            else:
                print("That spot is already taken! Try again.")
        else:
            print("Invalid input. Please enter row and column indices between 0 and 2.")

    print_board(board)
    print("Player " + current_player + " wins!")

tic_tac_toe()
