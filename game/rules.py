def full_board(board):
    '''
    Tarkastaa onko pelilauta täynnä

    Saa parametriksi peliladan.
    Palauttaa totuusarvon sen mukaan onko pelilauta täynnä
    '''
    for i in board[0]:
        if i==0:
            return False
    return True
