from game.game import Board

def test_place_piece():
    board = Board()
    row = board.place_piece(1, 1)
    assert row == 1
    assert board.grid[-1][0] == 1