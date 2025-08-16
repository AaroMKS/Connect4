import copy
from game import rules
import time

def iterative(board, current_player, max_depth, time_limit):
    board.dictionary = {}
    first=time.time()
    best_column= None
    for depth in range(1, max_depth+1):
        value,column =minimax(board, depth, current_player, first, time_limit, alpha=-99999, beta=99999)
        #if time.time()-first>time_limit:
            #break
        if column is None:
            break
        best_value=value
        best_column =column
    return best_value,best_column

def minimax(board, depth, current_player,first, time_limit, alpha, beta, last_column=None, last_row=None):
    best_column = None
    if current_player == 2:
        value = -99999 
    else:
        value = 99999
    
    # Minimax-algoritmi, joka määrittää parhaan siirron
    if last_column is not None and last_row is not None:
        if rules.winner(board.grid, last_column, 3-current_player, last_row):
            
            if current_player==1:
                return (100000 - depth*1000, last_column)
            else:
                return (-100000 + depth*1000, last_column)
            
    if rules.full_board(board.grid):
        return (0, None)
    if depth==0:
        # Kutsutaan heuristiikkafunktiota
        if last_column==None:
            last_column=-1
        if last_row==None:
            last_row=-1
        
        return heuristic_function(board, last_column, last_row, depth, current_player)

    column_order =[3, 2, 4, 1, 5, 0, 6]  # Tutkitaan siirrot keskeltä ulospäin
    board_str=",".join(",".join(str(number) for number in row) for row in board.grid)
    if board_str in board.dictionary:
        column_order.remove(board.dictionary[board_str])
        column_order.insert(0, board.dictionary[board_str])
    if current_player==2:
        value=-99999
        for column in column_order:
            if time.time()-first>time_limit:
                return value, best_column
            board_copy=copy.deepcopy(board)  # Kopioidaan pelilaudan luokka
            row=board_copy.place_piece(column, current_player)  # Kokeillaan siirtoa
            if row=="error":   # Ohitetaan, jos sarake täynnä
                continue
            
            new_score=minimax(board_copy,depth-1,1, first, time_limit, alpha, beta, column, row)[0]
            # Saadaan uusi paras arvo ja siirto
            if new_score>value:
                value=new_score
                best_column=column
            alpha = max(alpha, value)
            if alpha >= beta:   #Alfa-beeta karsinta
                break
        if best_column is not None: 
            board.dictionary[board_str]=best_column
        return value, best_column
    else:
        value=99999
        for column in column_order:
            if time.time()-first>time_limit:
                return value, best_column
            board_copy=copy.deepcopy(board)
            row=board_copy.place_piece(column, current_player)
            if row=="error":
                continue
            
            new_score=minimax(board_copy,depth-1,2,first, time_limit, alpha, beta, column, row)[0]
            if new_score<value:
                value=new_score
                best_column=column
            beta = min(beta, value)
            if alpha >= beta:
                break
        if best_column is not None:
            board.dictionary[board_str]=best_column
        return value, best_column

def heuristic_function(board, last_column, last_row, depth, current_player):
    # Palauta pelitilanteen hyvyyttä kuvaava pistemäärä
    if rules.winner(board.grid, last_column, current_player, last_row):
        return (100000-depth*1000, last_column)
    if rules.winner(board.grid, last_column, 3-current_player, last_row):
        return (-100000+depth*1000, last_column)
    if pieces_in_row(board.grid, current_player, 3, last_column, last_row):
        return (5000-depth*50, last_column)
    if pieces_in_row(board.grid, 3-current_player,3, last_column, last_row):
        return (-5000+depth*50, last_column)
    if pieces_in_row(board.grid, current_player, 2, last_column, last_row):
        return (100-depth*2, last_column)
    if pieces_in_row(board.grid, 3-current_player, 2, last_column, last_row):
        return (-100+depth*2, last_column)
    return (0, None)

def pieces_in_row(board, player, size, column, row):
    count=0
    for i in range(len(board[0])):     # Tarkastetaan onko rivillä neljä vierekkäistä saman pelaajan nappulaa
        if board[row][i]==player:
            count+=1
        else:
            count=0
        if count==size:
            if size==4:
                return True
            else:
                if (i-size>=0 and board[row][i-size]==0) or (i+1<len(board[0]) and board[row][i+1]==0):
                    return True
    
    count=0
    for i in range(len(board)):  # Tarkastetaan onko sarakkeella neljä päällekkäistä saman pelaajan nappulaa
        if board[i][column]==player:
            count+=1
        else:
            count=0
        if count==size:
            if size==4:
                return True
            else:
                if i<len(board)-1 and board[i+1][column]==0:
                    return True
    count=0
    placer=-min(3,column, row)
    for i in range(column+placer,min(column+4,len(board[0]))):
        # Tarkastetaan onko diagonaalisesti alhaalta ylös neljä peräkkäistä saman pelaajan nappulaa
        if row+(i-column) >= len(board) or row+(i-column)<0:
            continue
        if board[row+(i-column)][i]==player:
            count+=1
        else:
            count=0
        if count==size:
            if size==4:
                return True
            else:
                if (i-size>=0 and row+(i-column)-size>=0 and board[row+(i-column)-size][i-size]==0) or (i+1<len(board[0]) and row+(i-column)+1<len(board) and board[row+(i-column)+1][i+1]==0):
                    return True
    count=0
    placer=-min(3,column,len(board)-1-row)
    for i in range(column+placer,min(column+4,len(board[0]))):
        # Tarkastetaan onko diagonaalisesti ylhäältä alas neljä peräkkäistä saman pelaajan nappulaa
        if row-(i-column) >= len(board) or row-(i-column)<0:
            continue
        if board[row-(i-column)][i]==player:
            count+=1
        else:
            count=0
        if count==size:
            if size==4:
                return True
            else:
                if (i-size>=0 and row-(i-column)-size>=0 and board[row-(i-column)-size][i-size]==0) or (i+1<len(board[0]) and row-(i-column)<len(board)-1 and board[row-(i-column)+1][i+1]==0):
                    return True
    return False
