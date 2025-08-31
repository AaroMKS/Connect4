import unittest
import time
from game.game import Board
from ai.ai import iterative

class TestIterative(unittest.TestCase):

    def setUp(self):
        """Luodaan pelilauta joka testien alussa."""
        self.board = Board()
        self.board.place_piece(1, 1)
        self.board.place_piece(3, 2)
        self.board.place_piece(1, 1)
        self.board.place_piece(3, 2)
        self.board.place_piece(0, 1)
        self.board.place_piece(0, 2)

    def test_depths(self):
        for depth in range(1, 10):
            start = time.time()
            value, column = iterative(self.board, 2, max_depth=depth, time_limit=10.0)
            length = time.time() - start
            print(depth, column, value,length)
    def test_time_limits(self):
        for time_limit in [0.5, 1.0, 2.0, 3.0]:
            start = time.time()
            column = iterative(self.board, 2, max_depth=20, time_limit=time_limit)[1]
            length = time.time() - start
            print(f"Time limit {time_limit:.1f}s: best column={column}, took={length:.3f}s")

if __name__ == "__main__":
    unittest.main()