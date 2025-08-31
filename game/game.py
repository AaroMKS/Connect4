
class Board:
    '''
    Luokka, jossa pelilauta.
    Myös dictionary, jossa jo laskettuja lautatilanteita.
    '''
    def __init__(self):
        '''
        Luodaan pelilauta
        '''
        self.grid=[[0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],]
        self.dictionary={}

    def place_piece(self, x, player):
        '''
        Asetetaan pelinappula pelilaudalle

        Parametrit:
            x: Sarake, johon nappula asetetaan (0-6)
            player: Pelaaja 1 vai 2

        Palauttaa:
            rivin johon nappula asetettiin
            tai "error" jos sarake on täynnä.
        '''
        for i in reversed(range(len(self.grid))):
            if self.grid[i][x]==0:
                self.grid[i][x]=player
                return i
        return "error"
    def print_board(self):
        '''
        Tulostaa pelilaudan.
        '''
        for row in self.grid:
            print(" ".join(str(i) for i in row))
        print()
