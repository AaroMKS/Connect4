from game.game import Board

def winner(board, column ,player, row):
    count=0
    for i in board[row]:
        if i==player:
            count+=1
        else:
            count=0
        if count==4:
            return True
    count=0
    for i in board:
        if i[column]==player:
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
    
