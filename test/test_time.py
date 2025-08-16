import time
from game.game import Board 
from ai.ai import iterative  

def test_depths():
    board = Board()
    board.place_piece(1, 1)
    board.place_piece(3, 2)
    board.place_piece(1, 1)
    board.place_piece(3, 2)
    board.place_piece(0, 1)
    board.place_piece(0, 2)
    for depth in range(1, 10):   
        start = time.time()
        value, column = iterative(board, 2, max_depth=depth, time_limit=10.0)
        length= time.time()-start
        print(depth, column, value,length)

def test_time_limits():
    board = Board()
    board.place_piece(1, 1)
    board.place_piece(3, 2)
    board.place_piece(1, 1)
    board.place_piece(3, 2)
    board.place_piece(0, 1)
    board.place_piece(0, 2)
    for t in [0.5, 1.0, 2.0, 3.0]:
        start = time.time()
        value, column = iterative(board,2, max_depth=20, time_limit=t)
        duration = time.time() - start
        print(f"Aikaraja {t:.1f}s: paras siirto = {column}, arvo = {value}, kesti = {duration:.3f} s")


if __name__ == "__main__":
    test_depths()
    test_time_limits()