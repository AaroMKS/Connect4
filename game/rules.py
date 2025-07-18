from game.game import Board

def winner(board, column ,player, row):
    #gameboard=Board()
    #row=gameboard.heights
    #row=row[column-1]
    #print(gameboard.heights)
    #current=board[row][Board.heights[row]]
    #directions=[(0,1),(1,0),(1,1),(1,-1)]
    count=0
    #print((row,column))
    for i in board[6-row]:
        #print(i)
        print(player)
        if i==player:
            count+=1
        else:
            count=0
        if count==4:
            return True
    count=0
    for i in board:
        if i[column-1]==player:
            count+=1
        else:
            count=0
        if count==4:
            return True       

    
    return False


def full_board(board):
    for i in board[0]:
        if i==0:
            return False
        return True
    
