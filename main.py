from game.game import Board
from game import rules
def main():
    turn=1
    game=Board()

    while True:
        move=valid()

        row=game.place_piece(move, turn)
        if row == "error":
            print("Täynnä")
            continue
        game.print_board()
        if rules.full_board(game.grid):
            print("Tasapeli")
            break
        if rules.winner(game.grid, move,turn, row):
            print("Voittaja")
            break
        turn = 3 - turn

def valid():
    while True:
        try: 
            move = int(input("Aseta (0-6):"))
            if move>6 or move<0:
                print("Ei pelilaudalla")
                continue
            return move
        except ValueError:
            print("Ei numero")
if __name__ == "__main__":
    main()