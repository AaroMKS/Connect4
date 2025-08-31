import unittest
from game.game import Board
from ai.ai import pieces_in_row
from game.rules import full_board
class TestGame(unittest.TestCase):
    def test_place_piece(self):
        board = Board()
        row = board.place_piece(6, 2)
        self.assertEqual(row, 5)
        self.assertEqual(board.grid[-1][6], 2)
    def test_winner(self):
        board=Board()
        board.place_piece(6, 1)
        board.place_piece(6, 1)
        board.place_piece(6, 1)
        board.place_piece(6, 1)
        self.assertTrue(pieces_in_row(board.grid,1,4, 6, 3))

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
        self.assertTrue(pieces_in_row(board.grid,1, 4, 3, 2))

    def test_full_column(self):
        board = Board()
        for _ in range(6):
            board.place_piece(0, 1)
        result = board.place_piece(0, 2)
        self.assertEqual(result, "error")

    def test_full_board(self):
        board = Board()
        for i in range(7):
            for _ in range(6):
                board.place_piece(i, 1)
        self.assertTrue(full_board(board.grid))

    def test_print_board(self):
        board = Board()
        board.place_piece(0, 1)
        try:
            board.print_board()
        except ValueError:
            print("Oops")
