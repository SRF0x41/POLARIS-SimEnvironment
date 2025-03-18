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


# Send to machine translation
def parseToNum():
    parsedNumerical = []
    for val in gameState:
        if isinstance(val,int):
            parsedNumerical.append(0)
        elif val == 'X':
            parsedNumerical.append(-1)
        else:
            parsedNumerical.append(1)
    return parsedNumerical

def legalMove(move):
    if not isinstance(gameState[move],int):
        return False
    return True

def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def validMove(self,userInput):
    if is_integer(userInput) and legalMove(userInput):
        return True
    return False
        

        

def main():
    # Socket tooling
    user_input = ""
    sock_comm = SocketComm('localhost',12345)
    
    # Game tooling
    win_state = 0 # 0 for ongoing game or draw, -1 human 1 machine
    running = True;
    
    
    # Main running loop
    while running:
        drawBoard()
        
        # User input
        user_input = input("Enter a move")
        while not validMove(user_input):
            print("Illegal move or invalid input")
            user_input = input("Enter a move")
            if user_input == 'q':
                sock_comm.close_connection()
                break
        
        user_move = int(user_input)
        gameState[user_move] = 'X'
        
        # JSON send to polaris
        numerical_gamestate = parseToNum()
        send_POLARIS = {"Command":"POLARIS_move", "data": numerical_gamestate, "win_state": win_state}
        sock_comm.sendMessage(send_POLARIS)
        
        
        
    
    sock_comm.close_connection()
    
    
       
        
        
        

if __name__ == "__main__":
    main()
