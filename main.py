from game.game import Board
from game import rules
def main():
    # Määritä pelaaja aloittamaan peli
    turn = 1
    game = Board()
    print(Board().grid)
    # Aloita loop-jonka aikana pelia pelataan
    while True:
        move=valid() # Tarkasta onko syötetty liike hyväksyttävä
        row=game.place_piece(move, turn)  # Määritä mille riville nappula tippui
        if row == "error":     # Tarkasta onko sarake täynnä
            print("Täynnä")
            continue
        game.print_board()   # Tulosta pelilauta
        if rules.full_board(game.grid):   # Peli päättyy tasapeliin jos lauta on täynnä
            print("Tasapeli")
            break
        if rules.winner(game.grid, move,turn, row):     # Tarkista onko peli voitettu
            print("Voittaja")
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