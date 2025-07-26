import unittest
from game.game import Board
from game.rules import winner
class TestGame(unittest.TestCase):
    def test_place_piece(self):
        board = Board()
        row = board.place_piece(3, 2)
        self.assertEqual(row, 5)
        self.assertEqual(board.grid[-1][3], 2)
    def test_winner(self):
        board=Board()
        board.place_piece(0, 1)
        board.place_piece(0, 1)
        board.place_piece(0, 1)
        board.place_piece(0, 1)
        self.assertTrue(winner(board.grid, 0, 1, 3))
    def test_winner_diagonal(self):
        board=Board()
        board.place_piece(0,1)
        board.place_piece(1,2)
        board.place_piece(1,1)
        board.place_piece(2,1)
        board.place_piece(2,2)
        board.place_piece(2,1)
        board.place_piece(3,1)
        board.place_piece(3,2)
        board.place_piece(3,2)
        board.place_piece(3,1)
        self.assertTrue(winner(board.grid, 3, 1, 2))
