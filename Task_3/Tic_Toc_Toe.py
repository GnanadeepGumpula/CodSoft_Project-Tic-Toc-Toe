def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def is_winner(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]]
    ]
    return [player, player, player] in win_conditions

def get_empty_cells(board):
    return [(x, y) for x in range(3) for y in range(3) if board[x][y] == " "]

def minimax(board, depth, is_maximizing, alpha, beta):
    if is_winner(board, "X"):
        return -1
    elif is_winner(board, "O"):
        return 1
    elif not get_empty_cells(board):
        return 0

    if is_maximizing:
        max_eval = float('-inf')
        for (x, y) in get_empty_cells(board):
            board[x][y] = "O"
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[x][y] = " "
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for (x, y) in get_empty_cells(board):
            board[x][y] = "X"
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[x][y] = " "
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def best_move(board):
    best_val = float('-inf')
    move = (-1, -1)
    for (x, y) in get_empty_cells(board):
        board[x][y] = "O"
        move_val = minimax(board, 0, False, float('-inf'), float('inf'))
        board[x][y] = " "
        if move_val > best_val:
            move = (x, y)
            best_val = move_val
    return move

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    human_turn = True

    while True:
        try:
            print_board(board)
            if is_winner(board, "X"):
                print("Human wins!")
                break
            if is_winner(board, "O"):
                print("AI wins!")
                break
            if not get_empty_cells(board):
                print("It's a draw!")
                break

            if human_turn:
                move = input("Enter your move (row and column): ").split()
                x, y = int(move[0]), int(move[1])
                if board[x][y] == " ":
                    board[x][y] = "X"
                    human_turn = False
                else:
                    print("Invalid move. Try again.")
            else:
                x, y = best_move(board)
                board[x][y] = "O"
                human_turn = True
        except (ValueError, IndexError):
            print("Invalid input. Please enter valid row and column numbers.")

if __name__ == "__main__":
    main()
