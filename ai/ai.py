import copy
from game import rules
def minimax(board, depth, current_player, alpha, beta, last_column=None, last_row=None):
    # Minimax-algoritmi, joka määrittää parhaan siirron
    if depth==0 or rules.full_board(board.grid):
        # Kutsutaan heuristiikkafunktiota
        return heuristic_function(board, last_column, last_row)
    best_column=None
    column_order =[3, 2, 4, 1, 5, 0, 6]  # Tutkitaan siirrot keskeltä ulospäin
    if current_player==2:
        value=-99999
        for column in column_order:
            board_copy=copy.deepcopy(board)  # Kopioidaan pelilaudan luokka
            row=board_copy.place_piece(column, current_player)  # Kokeillaan siirtoa
            if row=="error":   # Ohitetaan, jos sarake täynnä
                continue
            new_score=minimax(board_copy,depth-1,1, alpha, beta, column, row)[0]
            # Saadaan uusi paras arvo ja siirto
            if new_score>value:
                value=new_score
                best_column=column
            alpha = max(alpha, value)
            if alpha >= beta:   #Alfa-beeta karsinta
                break
        return value, best_column
    else:
        value=99999
        for column in column_order:
            board_copy=copy.deepcopy(board)
            row=board_copy.place_piece(column, current_player)
            if row=="error":
                continue
            new_score=minimax(board_copy,depth-1,2, alpha, beta, column, row)[0]
            if new_score<value:
                value=new_score
                best_column=column
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value, best_column

def heuristic_function(board, last_column, last_row):
    # Palauta pelitilanteen hyvyyttä kuvaava pistemäärä
    if rules.winner(board.grid, last_column, 2, last_row):
        return (100, None)
    if rules.winner(board.grid, last_column, 1, last_row):
        return (-100, None)
    return (0, None)