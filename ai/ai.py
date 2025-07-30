import copy
from game import rules
def minimax(board, depth, current_player, alpha, beta, last_column=None, last_row=None):
    # Minimax-algoritmi, joka määrittää parhaan siirron
    if depth==0 or rules.full_board(board.grid):
        # Kutsutaan heuristiikkafunktiota
        return heuristic_function(board, last_column, last_row, depth)
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

def heuristic_function(board, last_column, last_row, depth):
    # Palauta pelitilanteen hyvyyttä kuvaava pistemäärä
    if rules.winner(board.grid, last_column, 2, last_row):
        return (100-depth*5, None)
    if rules.winner(board.grid, last_column, 1, last_row):
        return (-100+depth*5, None)
    if three_row(board.grid, last_column, 2, last_row):
        return (10-depth*2, None)
    if three_row(board.grid, last_column, 1, last_row):
        return (-10+depth*2, None)
    return (0, None)

def three_row(board, column, player, row):
    count=0
    for i in board[row]:     # Tarkastetaan onko rivillä neljä vierekkäistä saman pelaajan nappulaa
        if i==player:
            count+=1
        else:
            count=0
        if count==3:
            return True
    count=0
    for i in board:  # Tarkastetaan onko sarakkeella neljä päällekkäistä saman pelaajan nappulaa
        if i[column]==player:
            count+=1
        else:
            count=0
        if count==3:
            return True
    count=0
    placer=-min(3,column, row)
    for i in range(column+placer,min(column+4,7)):
        # Tarkastetaan onko diagonaalisesti alhaalta ylös neljä peräkkäistä saman pelaajan nappulaa
        if row+(i-column) >= 6 or row+(i-column)<0:
            continue
        if board[row+(i-column)][i]==player:
            count+=1
        else:
            count=0
        if count==3:
            return True
    count=0
    placer=-min(3,column,5-row)
    for i in range(column+placer,min(column+4,7)):
        # Tarkastetaan onko diagonaalisesti ylhäältä alas neljä peräkkäistä saman pelaajan nappulaa
        if row-(i-column) >= 7 or row-(i-column)<0:
            continue
        if board[row-(i-column)][i]==player:
            count+=1
        else:
            count=0
        if count==3:
            return True
    return False
    pass
