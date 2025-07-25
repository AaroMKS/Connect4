from game import rules, game
from game.game import Board
import copy
def minimax(board, depth, current_player, last_column=None, last_row=None): 
    # Määritetään minimax-algoritmillä paras mahdollinen siirto
    if depth==0 or rules.full_board(board.grid):    # Palauta tekoälyn tai vastustajan voittoa kuvaava arvo jos algoritmin syvyys on 0
        if rules.winner(board.grid, last_column, 2, last_row):
            return (100, None)
        elif rules.winner(board.grid, last_column, 1, last_row):
            return (-100, None)
        else:
            return (0, None)
    best_column=None
    if current_player==2:    
        value=-99999
        for column in range(7):
            board_copy=copy.deepcopy(board)  # Tehdään kopio Board-luokasta
            row=board_copy.place_piece(column, current_player)   # Asetetaan jokaiseen kolumniin nappula
            
            if row=="error":   # Jos kolumni on täynnä palataan loopin alkuun
                continue
            new_score=minimax(board_copy,depth-1,1, column, row)[0]   # Funktio kutsuu itseään rekursiivisesti
            
            if new_score>value:   # Jos tällä siirrolla saatu uusi arvo on parempi kuin aikaisemmin saatu, valitaan se parhaaksi siirroksi
                value=new_score
                best_column=column
        return value, best_column
    else:   # Vähennetään arvoa perustuen kuinka hyviä vastustajan siirrot ovat
        value=99999
        for column in range(7):
            board_copy=copy.deepcopy(board)
            row=board_copy.place_piece(column, current_player)
            if row=="error":
                continue
            new_score=minimax(board_copy,depth-1,2, column, row)[0] 
            if new_score<value:
                value=new_score
                best_column=column
        return value, best_column

