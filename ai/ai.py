import copy
import time
from game import rules


def iterative(board, current_player, max_depth, time_limit):
    """
    Suorittaa iteratiivisen syvenevän haun minimaxin avulla anetulla aikarajalla.
    Funktio kokeilee hakusyvyyksiä max_depth asti ja kutsuu aina minimaxia.

    Parametrit: 
        board: Pelilauta-luokka, jossa nykyinen pelitilanne
        current_player: Pelaaja, jonka vuoro (1 tai 2)
        max_depth: Suurin mahdollinen hakusyvyys
        time_limit: Aikaraja sekunteinta, jolloin haku keskeytetään
    Palauttaa tuplen, jossa:
        best_value: Paras löydetty heuristinen pistemäärä
        best_column: Paras löydetty sarake, johon kannattaa tehdä siirto
    """
    board.dictionary = {}
    start = time.time()
    best_column = None
    for depth in range(1, max_depth+1):
        if time.time() - start > time_limit:
            break
        value,column = minimax(board, depth, current_player, start, time_limit, alpha=-99999, beta=99999)
        if column is None:
            break
        best_value = value
        best_column = column
    return best_value, best_column

def minimax(board, depth, current_player, start, time_limit, alpha, beta, last_column=None, last_row=None):
    """ 
    Suorittaa Minimax-algoritmin

    Parametrit:
        board: Pelilauta-luokka, jossa nykyinen pelitilanne
        depth: Kuinka paljon siirtoyvyyttä jäljellä
        current_player: Pelaaja, jonka vuoro (1 tai 2)
        start: Iteratiivisen haun aloitusaika
        time_limit: Aikaraja sekunteinta, jolloin haku keskeytetään
        alpha: Alfa-arvo alfa-beeta-karsinnassa (maksimoija)
        beta: Beta-arvo alfa-beeta-karsinnassa (minimoija)
        last_column: Viimeksi pelatun siirron sarake
        last_row: Viimeksi pelatun siirron rivi
    Palauttaa tuplen jossa: 
            best_value: Paras löydetty heuristinen pistemäärä
            best_column: Paras löydetty sarake, johon kannattaa tehdä siirto
      
        """
    best_column = None
    # Tarkastetaan johtiko viimeisin siirto voittoon
    if last_column is not None and last_row is not None:
        if pieces_in_row(board.grid, 3-current_player, 4, last_column, last_row):
            if current_player == 1:
                return (100000 - depth*1000, last_column)
            else:
                return (-100000 + depth*1000, last_column)
    # Tasapeli, jos lauta täynnä
    if rules.full_board(board.grid):
        return (0, None)
    # Maksimisyvyys saavutettu
    if depth == 0:
        return heuristic_function(board, last_column, last_row, depth)

    # Tutkitaan siirrot keskeltä ulospäin
    column_order = [3, 2, 4, 1, 5, 0, 6]

    # Jos tästä tilanteesta on jo löydetty paras siirto, aloitetaan siitä
    board_str = ",".join(",".join(str(number) for number in row) for row in board.grid)
    if board_str in board.dictionary:
        column_order.remove(board.dictionary[board_str])
        column_order.insert(0, board.dictionary[board_str])
    # Maksimoija
    if current_player == 2:
        value = -99999
        for column in column_order:
            # Tarkistetaan aikaraja
            if time.time() - start > time_limit:
                return value, None
            # Kokeillaan siirtoa
            board_copy = copy.deepcopy(board)
            row = board_copy.place_piece(column, current_player)
            if row == "error":   # Ohitetaan, jos sarake täynnä
                continue
            # Jos siirto johtaa suoraan voittoon
            if pieces_in_row(board_copy.grid, current_player, 4, column, row):
                return (100000 - depth*1000, column)

            # Kutsutaan minimaxia rekursiivisesti
            new_score = minimax(board_copy, depth-1, 1, start, time_limit, alpha, beta, column, row)[0]

            # Saadaan uusi paras arvo ja siirto
            if new_score > value:
                value = new_score
                best_column = column

            # Alfa-beeta karsinta
            alpha = max(alpha, value)
            if alpha >= beta:
                break
    # Minimoija
    else:
        value = 99999
        for column in column_order:
            if time.time() - start > time_limit:
                return value, None
            board_copy = copy.deepcopy(board)
            row = board_copy.place_piece(column, current_player)
            if row == "error":
                continue
            if pieces_in_row(board_copy.grid, current_player, 4, column, row):
                
                return (-100000 + depth*1000, column)
            new_score=minimax(board_copy, depth-1, 2, start, time_limit, alpha, beta, column, row)[0]
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
    """
    Arvioi pelilaudan tilanteen heuristiikan avulla. 
    Lasketaan neljän suorat, kolmen suorat ja kahden suorat.
    Syvyys vaikuttaa pistemäärään, niin että nopeat voitot antavat enemmän pisteitä

    Parametrit:
        board: Pelilauta-luokka, jossa nykyinen pelitilanne
        last_column: Viimeksi pelatun siirron sarake
        last_row: Viimeksi pelatun siirron rivi
        depth: Kuinka paljon siirtoyvyyttä jäljellä (jotta nopeammat voitot saa paremmat arvot)

    Palauttaa:
        tuplen jossa on heuristinen pistearvo ja sarake jonka arvo laskettiin
    
    """
    if pieces_in_row(board.grid, 2, 4, last_column, last_row):
        return (100000 - depth*10000, last_column)
    if pieces_in_row(board.grid, 1, 4, last_column, last_row):
        return (-100000 + depth*10000, last_column)
    if pieces_in_row(board.grid, 2, 3, last_column, last_row):
        return (5000 - depth*50, last_column)
    if pieces_in_row(board.grid, 1, 3, last_column, last_row):
        return (-5000 + depth*50, last_column)
    if pieces_in_row(board.grid, 2, 2, last_column, last_row):
        return (100 - depth*2, last_column)
    if pieces_in_row(board.grid, 1, 2, last_column, last_row):
        return (-100 + depth*2, last_column)
    return (0, None)

def pieces_in_row(board, player, size, column, row):
    """
    Etsii muodostaako annettu nappula annetun koon pituisen suoran

    Parametrit:
        board: Pelilauta-luokka, jossa nykyinen pelitilanne
        player: Pelaaja, jonka suoria etsitään
        size: Koko, jonka pituista suoraa etsitään
        column: Viimeksi pelatun siirron sarake
        row: Viimeksi pelatun siirron rivi
    Palauttaa True tai False, riippuen siitä löytyikö suoraa

    """
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
