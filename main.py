from game.game import Board
from game import rules
def main():
    turn=1
    game=Board()

    while  True:
        #if turn==1:
        move=int(input("Move:"))
        game.place_piece(move, turn)
        if turn==1:
            turn=2
        else:
            turn=1
        game.print_board()
        if rules.winner(game.grid, move,turn):
            break
        if rules.full_board(game.grid):
            break

if __name__ == "__main__":
    main()