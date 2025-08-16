import unittest
from game import Board
from ai.ai import minimax, heuristic_function


class MinimaxTest(unittest.TestCase):
    def test_avoiding_losing(self):
        board=Board()
        board.place_piece(1,1)
        board.place_piece(1,1)
        board.place_piece(1,1)
        move=minimax(board, depth=5, current_player=2, alpha=-99999, beta=99999)[1]
        self.assertEqual(move, 1)

    def test_certain_win(self):
        board=Board()
        board.place_piece(1,2)
        board.place_piece(0,1)
        board.place_piece(1,2)
        board.place_piece(0,1)
        board.place_piece(1,2)
        board.place_piece(0,1)
        move=minimax(board, depth=5, current_player=2, alpha=-99999, beta=99999)[1]
        self.assertEqual(move, 1)

    def test_heuristic(self):
        board=Board()
        board.place_piece(1,1)
        board.place_piece(2,2)
        board.place_piece(1,1)
        board.place_piece(2,2)
        board.place_piece(2,1)
        board.place_piece(1,2)
        board.place_piece(4,1)
        board.place_piece(1,2)
        board.place_piece(4,1)
        board.place_piece(2,2)
        board.place_piece(0,1)
        self.assertEqual(heuristic_function(board, 0,5,0), (-5000, None))





        

