class Board:
    def __init__(self):
        self.grid=[[0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],]
    def place_piece(self, x, player):
        for i in reversed(range(len(self.grid))):
            print((i,x))
            if self.grid[i][x-1]==0:
                self.grid[i][x-1]=player
                break
    def print_board(self):
        print(self.grid)
                
    
            