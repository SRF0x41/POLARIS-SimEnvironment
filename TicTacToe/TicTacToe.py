import sys
from SocketComm import SocketComm

#start game state
gameState = list(range(0,10))

def drawBoard():
    for i in range(1,10):
        
        if i % 3 == 0:
            print(str(gameState[i]))
            print("---------")
        else:
            print(str(gameState[i]) + " |", end = " ")
            
def updateGameState(c, pos):
    if isinstance(gameState[pos], int):
        gameState[pos] = c

def detectWin():
    # Check rows for a win (Positions 1-3, 4-6, 7-9)
    for i in range(1, 10, 3):  # Starts at position 1, 4, 7
        if gameState[i] == gameState[i+1] == gameState[i+2]:
            return gameState[i]

    # Check colums
    for i in range(1,4):
        if gameState[i] == gameState[i+3] == gameState[i+6]:
            return gameState[i]

    # Check diagonals for a win
    if gameState[1] == gameState[5] == gameState[9]:
        return gameState[1]
    if gameState[3] == gameState[5] == gameState[6]:
        return gameState[3] 

    return None


    

def main():
    user_input = ""
    # main input loop
    
    sock_comm = SocketComm('localhost',12345)
    
    while True:
        data = sock_comm.recieveData()
        print("recieved data: ",data)
        
        print("Sent data ");
        sock_comm.sendMessage("Message recieved")
        
        
       
    
    
    '''
    while True:
        drawBoard()
        user_input = input("Enter a move: ")
        if user_input == 'q':
            break
        
        user_input = int(user_input)
        updateGameState('X', user_input)
        
        winner = detectWin()
        if winner != None:
            drawBoard()
            print(winner+" wins")
            break
            '''
            
       
        
        
        

if __name__ == "__main__":
    main()
