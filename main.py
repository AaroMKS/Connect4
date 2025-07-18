from game.game import Board
from game import rules
def main():
    turn=1
    game=Board()

    while  True:
        #if turn==1:
        move=int(input("Move:"))
        row=game.place_piece(move, turn)
        #print(row)
        
        game.print_board()
        if rules.full_board(game.grid):
            break
        if rules.winner(game.grid, move,turn, row):
            print("voittaja")
            break
        if turn==1:
            turn=2
        else:
            turn=1

if __name__ == "__main__":
    main()