import unittest
import copy
from game.game import Board
from ai.ai import heuristic_function, iterative
class MinimaxTest(unittest.TestCase):
    def test_avoiding_losing(self):
        board=Board()
        board.place_piece(1,1)
        board.place_piece(1,1)
        board.place_piece(1,1)
        board.dictionary={}
        move=iterative(board,2, 10, 10.0)[1]
        self.assertEqual(move, 1)

    def test_certain_win(self):
        board=Board()
        board.place_piece(1,2)
        board.place_piece(5,1)
        board.place_piece(1,2)
        board.place_piece(0,1)
        board.place_piece(1,2)
        board.place_piece(0,1)
        board.dictionary={}
        move=iterative(board,2, 10, 10.0)[1]
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
        self.assertEqual(heuristic_function(board, 0,5,0), (-5000, 0))

    
    def test_certain_win_2(self):
        board=Board()
        board.place_piece(2,1)
        board.place_piece(3,2)
        board.place_piece(2,1)
        board.place_piece(3,2)
        board.place_piece(3,1)
        board.place_piece(2,2)
        board.place_piece(1,1)
        board.place_piece(3,2)

        board.place_piece(4,1)
        board.place_piece(3,2)
        board.place_piece(4,1)
        board.place_piece(2,2)

        board.place_piece(4,1)
        board.place_piece(4,2)
        board.place_piece(5,1)
        board.place_piece(1,2)
        board.place_piece(5,1)
        board.dictionary={}
        


        move=iterative(board,2, 10, 10.0)[1]
        self.assertEqual(move, 4)

    def test_avoid_certain_losing_diagonal(self):
        board = Board()
        board.place_piece(0, 1) 
        board.place_piece(1, 2)
        board.place_piece(1, 1)  
        board.place_piece(2, 2)
        board.place_piece(2, 1)  
        board.place_piece(3, 2)

        board.place_piece(4, 1)
        board.place_piece(4, 2)
        board.place_piece(5, 1)
        board.place_piece(5, 2)
        board.place_piece(6, 1)
        board.place_piece(6, 2)
        
        board.dictionary = {}
        move = iterative(board, 2, 10, 10.0)[1]
        self.assertEqual(move, 3)
    def test_heuristic(self):
        board=Board()
        board.place_piece(2,1)
        board.place_piece(3,2)
        board.place_piece(2,1)
        board.place_piece(3,2)
        board.place_piece(3,1)
        board.place_piece(2,2)
        board.place_piece(1,1)
        board.place_piece(3,2)

        board.place_piece(4,1)
        board.place_piece(3,2)
        board.place_piece(4,1)
        board.place_piece(2,2)

        board.place_piece(4,1)
        board.place_piece(4,2)
        board.place_piece(5,1)
        board.place_piece(1,2)
        board.place_piece(5,1)
        board.dictionary={}
        for i in range(7):
            board_copy=copy.deepcopy(board)
            row=board_copy.place_piece(i,2)
            print(heuristic_function(board,i,row,1))
    def test_heuristic_2(self):
        board=Board()
        board.place_piece(1,2)
        board.place_piece(5,1)
        board.place_piece(1,2)
        board.place_piece(0,1)
        board.place_piece(1,2)
        board.place_piece(0,1)
        board.dictionary={}
        for i in range(7):
            board_copy=copy.deepcopy(board)
            row=board_copy.place_piece(i,2)
            print(heuristic_function(board,i,row,1))

    def test_ai_does_not_play_full_column(self):
        board = Board()
        for _ in range(6):
            board.place_piece(0, 1)
        board.dictionary = {}
        move = iterative(board, 2, 4, 5.0)[1]
        self.assertNotEqual(move, 0)

    def test_ai_never_makes_illegal_move(self):
        board = Board()
        max_turns = 30  # pelataan enintään 30 siirtoa
        current_player = 1

        for turn in range(max_turns):
            if current_player == 1:
                # AI:n vuoro
                move = iterative(board, current_player, 3, time_limit=5.0)[1]
                self.assertIn(move, range(7), f"AI antoi laittoman siirron {move}")
                self.assertTrue(board.is_legal_move(move), f"AI yritti laittaa täyteen sarakkeeseen {move}")
                board.place_piece(move, current_player)
            else:
                # Vastustaja: yksinkertainen strategia = valitse eka vapaa sarake
                for col in range(7):
                    if board.is_legal_move(col):
                        board.place_piece(col, current_player)
                        break

            # Tarkista ettei peli ole vielä loppunut
            if board.check_winner(current_player):
                break

            current_player = 3 - current_player  # vaihdetaan pelaajaa









        

