def winner(board, column ,player, row):
    count=0
    for i in board[row]:     # Tarkastetaan onko rivillä neljä vierekkäistä saman pelaajan nappulaa
        if i==player:
            count+=1
        else:
            count=0
        if count==4:
            return True
    count=0
    for i in board:  # Tarkastetaan onko sarakkeella neljä päällekkäistä saman pelaajan nappulaa
        if i[column]==player:
            count+=1
        else:
            count=0
        if count==4:
            return True   
    count=0
    placer=-min(3,column, row)    
    for i in range(column+placer,min(column+4,7)):
        if row+(i-column) >= 6 or row+(i-column)<0:
            continue
        if board[row+(i-column)][i]==player:
            count+=1
        else:
            count=0
        if count==4:
            return True 
    count=0
    placer=-min(3,column,5-row)    
    for i in range(column+placer,min(column+4,7)):
        if row-(i-column) >= 7 or row-(i-column)<0:
            continue
        if board[row-(i-column)][i]==player:
            count+=1
        else:
            count=0
        if count==4:
            return True 
    return False 


def full_board(board):
    # Tarkastetaan onko pelilauta täynnä 
    for i in board[0]:
        if i==0:
            return False
    return True
    
