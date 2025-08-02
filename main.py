from game.game import Board
from game import rules
from ai.ai import minimax
def main():
    # Määritä pelaaja aloittamaan peli
    turn = 1
    game = Board()
    game.print_board()
    # Aloita loop-jonka aikana pelia pelataan
    while True:
        if turn == 1:
            move=valid() # Tarkasta onko syötetty liike hyväksyttävä
        else:
            move=minimax(game, 10,2, alpha=-99999, beta=99999)[1]

        row=game.place_piece(move, turn)  # Määritä mille riville nappula tippui
        if row == "error":     # Tarkasta onko sarake täynnä
            print("Täynnä")
            continue
        if turn==2:
            game.print_board()   # Tulosta pelilauta
        if rules.full_board(game.grid):   # Peli päättyy tasapeliin jos lauta on täynnä
            print("Tasapeli")
            break
        if rules.winner(game.grid, move,turn, row):     # Tarkista onko peli voitettu
            game.print_board()
            print(f"Voittaja: {turn}")
            break
        turn = 3 - turn    # Vaihda pelaajan vuoroa

def valid():
    while True:
        # Kysytään käyttäjältä siirtoa ja tarkastetaan onko se väliltä 0-6 ja onko se numero.
        # Jos siirto on validi, se palautetaan.
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
