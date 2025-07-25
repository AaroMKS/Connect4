
class Board:
    def __init__(self):
        # Määritetään pelilauta
        self.grid=[[0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],]

    def place_piece(self, x, player):
        # Asetetaan pelinappula pelilaudalle
        for i in reversed(range(len(self.grid))):
            if self.grid[i][x]==0:
                self.grid[i][x]=player
                return i
        return "error"  # Palautetaan "error" jos sarake on täynnä
    def print_board(self):
        # Tulostetaan pelilauta
        for row in self.grid:
            print(" ".join(str(v) for v in row))
        print()
        #print(self.grid)        
    
            