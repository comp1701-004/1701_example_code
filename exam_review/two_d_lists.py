
# a tick-tac-toe board
# represent the board with a 2d list (3x3)
# uses 0s to indicate empty squares
# 1s to indicate Xs
# -1s to indicate Os
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

def check_for_win(board: list) -> int:
    """returns +1 if X has won, -1 if O has won, 0 otherwise"""

    # validate the board
    # number of Xs must be 0 or 1 more than # of Os
    board_total = 0
    for row in board:
        for item in row:
            board_total += item
    # make the program break if board is invalid
    # NOTE EXCEPTIONS AREN'T ON THE EXAM
    if board_total > 1 or board_total < 0:
        raise Exception("invalid board")

    all_sums = []

    # compute the size of the board
    n_rows = len(board)
    n_columns = len(board[0])

    # check the rows
    for row in board:
        all_sums.append(sum(row))
    
    # check the columns
    for column_index in range(n_columns):
        column_sum = 0
        for row_index in range(n_rows):
            value = board[row_index][column_index]
            column_sum += value
        all_sums.append(column_sum)

    # check the downward diagonal
    diag_sum = 0
    for index in range(n_rows):
        diag_sum += board[index][index]
    all_sums.append(diag_sum)

    # check the upward diagonal
    diag_sum = 0
    for index in range(n_rows):
        diag_sum += board[2-index][index]
    all_sums.append(diag_sum)
    
    # check if any of the sums represents a win
    if 3 in all_sums:
        return 1
    elif -3 in all_sums:
        return -1
    else:
        return 0


# here's another board
board = [
    [0, 0, -1],
    [-1, -1, -1],
    [-1, 0, 1],
]
print(check_for_win(board))