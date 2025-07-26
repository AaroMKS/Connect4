
import unittest
from game.game import Board
from ai.ai import minimax
class MinimaxTest(unittest.TestCase):
    def test_avoiding_losing(self):
        board=Board()
        board.place_piece(1,1)
        board.place_piece(1,1)
        board.place_piece(1,1)
        move=minimax(board, depth=4, current_player=2, alpha=-99999, beta=99999)[1]
        self.assertEqual(move, 1)
