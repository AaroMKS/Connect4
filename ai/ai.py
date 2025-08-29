import copy
import time
from game import rules


def iterative(board, current_player, max_depth, time_limit):
    board.dictionary = {}
    first = time.time()
    best_column = None
    for depth in range(1, max_depth+1):
        if time.time()-first > time_limit:
            break
        value,column =minimax(board, depth, current_player, first, time_limit, alpha=-99999, beta=99999)
        if column is None:
            break
        best_value = value
        best_column = column
    return best_value, best_column

def minimax(board, depth, current_player, first, time_limit, alpha, beta, last_column=None, last_row=None):
    # Minimax-algoritmi, joka määrittää parhaan siirron
    best_column = None
    if current_player == 2:
        value = -9999
    else:
        value = 9999
    if last_column is not None and last_row is not None:
        if pieces_in_row(board.grid, 3-current_player, 4, last_column, last_row):
            #print("Detected win by", 3-current_player, "at column", last_column, "row", last_row)
            winner = current_player
            if winner == 1:
                return (100000 - depth*1000, last_column)
            else:
                return (-100000 + depth*1000, last_column)

    if rules.full_board(board.grid):
        return (0, None)
    if depth == 0:
        return heuristic_function(board, last_column, last_row, depth)

    column_order = [3, 2, 4, 1, 5, 0, 6]  # Tutkitaan siirrot keskeltä ulospäin
    board_str = ",".join(",".join(str(number) for number in row) for row in board.grid)
    if board_str in board.dictionary:
        column_order.remove(board.dictionary[board_str])
        column_order.insert(0, board.dictionary[board_str])
    if current_player == 2:
        value = -99999
        for column in column_order:
            if time.time()-first>time_limit:
                return value, None
            board_copy=copy.deepcopy(board)  # Kopioidaan pelilaudan luokka
            row=board_copy.place_piece(column, current_player)  # Kokeillaan siirtoa
            if row=="error":   # Ohitetaan, jos sarake täynnä
                continue
            if pieces_in_row(board_copy.grid, current_player, 4, column, row):
                
                return (100000 - depth*1000, column)
            new_score=minimax(board_copy, depth-1, 1, first, time_limit, alpha, beta, column, row)[0]
            # Saadaan uusi paras arvo ja siirto
            if new_score > value:
                value = new_score
                best_column = column
            alpha = max(alpha, value)
            if alpha >= beta:   #Alfa-beeta karsinta
                break
        if best_column is not None:
            board.dictionary[board_str] = best_column
        return value, best_column
    else:
        value = 99999
        for column in column_order:
            if time.time()-first>time_limit:
                return value, None
            board_copy=copy.deepcopy(board)
            row=board_copy.place_piece(column, current_player)
            if row=="error":
                continue
            if pieces_in_row(board_copy.grid, current_player, 4, column, row):
                
                return (-100000 + depth*1000, column)
            new_score=minimax(board_copy, depth-1, 2, first, time_limit, alpha, beta, column, row)[0]
            if new_score<value:
                value = new_score
                best_column = column
            beta = min(beta, value)
            if alpha >= beta:
                break
        if best_column is not None:
            board.dictionary[board_str] = best_column
        return value, best_column

def heuristic_function(board, last_column, last_row, depth):
    # Palauta pelitilanteen hyvyyttä kuvaava pistemäärä
    if pieces_in_row(board.grid, 2, 4, last_column, last_row):
        return (100000 - depth*10000, last_column)
    if pieces_in_row(board.grid, 1, 4, last_column, last_row):
        return (-100000 + depth*10000, last_column)
    if pieces_in_row(board.grid, 2, 3, last_column, last_row):
        return (5000 - depth*50, last_column)
    if pieces_in_row(board.grid, 1,3, last_column, last_row):
        return (-5000 + depth*50, last_column)
    if pieces_in_row(board.grid, 2, 2, last_column, last_row):
        return (100 - depth*2, last_column)
    if pieces_in_row(board.grid, 1, 2, last_column, last_row):
        return (-100 + depth*2, last_column)
    return (0, None)

def pieces_in_row(board, player, size, column, row):
    y = len(board)
    x = len(board[0])

    # Horisontaalinen
    count = 0
    for i in range(x):
        if board[row][i] == player:
            count += 1
        else:
            count = 0
        if count == size:
            if size == 4:
                return True
            elif (i - size >= 0 and board[row][i - size] == 0) or (i + 1 < x and board[row][i + 1] == 0):
                return True

    # Vertikaalinen
    count = 0
    for i in range(y):
        if board[i][column] == player:
            count += 1
        else:
            count = 0
        if count == size:
            if size == 4:
                return True
            elif (i - size >= 0 and board[i - size][column] == 0) or (i + 1 < y and board[i + 1][column] == 0):
                return True

    # Diagonalinen alhaalta ylös
    count = 0
    for i in range(-3, 4):
        r = row + i
        c = column + i
        if 0 <= r < y and 0 <= c < x:
            if board[r][c] == player:
                count += 1
            else:
                count = 0
            if count == size:
                if size == 4:
                    return True
                r_backward, c_backward = r - size, c - size
                r_forward, c_forward = r + 1, c + 1
                if (0 <= r_backward < y and 0 <= c_backward < x and board[r_backward][c_backward] == 0) or \
                   (0 <= r_forward < y and 0 <= c_forward < x and board[r_forward][c_forward] == 0):
                    return True

    # Diagonaalinen ylhäältä alas
    count = 0
    for i in range(-3, 4):
        r = row - i
        c = column + i
        if 0 <= r < y and 0 <= c < x:
            if board[r][c] == player:
                count += 1
            else:
                count = 0
            if count == size:
                if size == 4:
                    return True
                r_backward, c_backward = r - size, c - size
                r_forward, c_forward = r + 1, c + 1
                if (0 <= r_backward < y and 0 <= c_backward < x and board[r_backward][c_backward] == 0) or \
                   (0 <= r_forward < y and 0 <= c_forward < x and board[r_forward][c_forward] == 0):
                    return True

    return False
