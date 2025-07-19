from game.game import Board
from game.rules import winner
def test_place_piece():
    board = Board()
    row = board.place_piece(3, 2)
    assert row == 5
    assert board.grid[-1][3] == 2
    
def test_winner():
    board=Board()
    board.place_piece(0, 1)
    board.place_piece(0, 1)
    board.place_piece(0, 1)
    board.place_piece(0, 1)
    assert winner(board.grid, 0, 1, 3) == True