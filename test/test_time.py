import time
from game.game import Board 
from ai.ai import iterative  

def test_depths():
    board = Board()
    board.place_piece(3, 1)
    board.place_piece(2, 2)
    board.place_piece(3, 1)
    board.place_piece(4, 2)

    print("Syvyystestit (ilman aikarajaa):")
    for depth in range(1, 8):   
        start = time.time()
        value, column = iterative(board, max_depth=depth, time_limit=10.0)
        duration = time.time() - start
        print(f"Syvyys {depth}: paras siirto = {column}, arvo = {value}, aika = {duration:.3f} s")
