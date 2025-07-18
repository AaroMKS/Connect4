class Board:
    def __init__(self):
        self.grid=[[0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],]
        self.heights=[0, 0, 0, 0, 0, 0, 0]
    def place_piece(self, x, player):
        for i in reversed(range(len(self.grid))):
            if self.grid[i][x-1]==0:
                self.grid[i][x-1]=player
                self.heights[x-1]=len(self.grid)-i
                #print(self.heights)
                return len(self.grid)-i
                #break
    def print_board(self):
        print(self.grid)
    def heights(self):
        return self.heights            
    
            