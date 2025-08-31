from game.game import Board
from game import rules
from ai.ai import iterative, pieces_in_row
def main():
    """
    Pelin pääsilmukka. Pelaaja 1 on käyttäjä (konsoli), pelaaja 2 on tekoäly (minimax).
    -Määrittää kenen pelivuoro
    -Luo pelilaudan
    -Kysyy käyttäjältä siirtoa ja laittaa sen pelilautaan
    -Tarkistaa voiton ja tasapelin
    """
    player = 1
    game = Board()
    game.print_board()

    while True:
        if player == 1:
            move=valid()
        else:
            move=iterative(game, player, max_depth=8, time_limit=3.0)[1]
        row=game.place_piece(move, player)
        if row == "error":
            print("Täynnä")
            continue
        if player == 2:
            game.print_board()
        if rules.full_board(game.grid):
            print("Tasapeli")
            break
        if pieces_in_row(game.grid,player,4, move, row):
            game.print_board()
            print(f"Voittaja: {player}")
            break
        player = 3 - player

def valid():
    """
    Kysytään käyttäjältä siirtoa ja tarkastetaan onko se validi.
    """
    while True:
        try:
            move = int(input("Aseta (0-6):"))
            if move > 6 or move < 0:
                print("Ei pelilaudalla")
                continue
            return move
        except ValueError:
            print("Ei numero")
if __name__ == "__main__":
    main()
