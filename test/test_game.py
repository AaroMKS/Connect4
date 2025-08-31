import unittest
from game.game import Board
from ai.ai import pieces_in_row
class TestGame(unittest.TestCase):
    def test_place_piece(self):
        board = Board()
        row = board.place_piece(3, 2)
        self.assertEqual(row, 5)
        self.assertEqual(board.grid[-1][3], 2)
    def test_winner(self):
        board=Board()
        # Luodaan pelitilanne jossa pelaajalla neljän rivi horisontaalisesti
        board.place_piece(0, 1)
        board.place_piece(0, 1)
        board.place_piece(0, 1)
        board.place_piece(0, 1)
        self.assertTrue(pieces_in_row(board.grid,1,4, 0, 3))

    def test_winner_diagonal(self):
        board=Board()
        # Luodaan pelitilanne jossa pelaajalla neljän rivi diagonaalisesti
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
        # Täytetaan yksi sarake kokonaan
        for _ in range(6):
            board.place_piece(0, 1)
        # Kuuluisi palauttaa "error" jos yritetäänm laittaa vielä yksi nappula
        result = board.place_piece(0, 2)
        self.assertEqual(result, "error")

