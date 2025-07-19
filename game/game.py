class Board:
    def __init__(self):
        self.grid=[[0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],]
        #self.heights=[0, 0, 0, 0, 0, 0, 0]
    def place_piece(self, x, player):
        for i in reversed(range(len(self.grid))):
            if self.grid[i][x]==0:
                self.grid[i][x]=player
                #self.heights[x-1]=len(self.grid)-i
                return i
        return "error"
    def print_board(self):
        print(self.grid)        
    
            