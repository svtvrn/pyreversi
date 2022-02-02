from array import *

#Current state of the board
class State:
    
    #Board
    board=[[]]
    board_size = 0
    WHITE = 1
    BLACK = 0
    EMPTY = -1
    state_score = 0

    #Starting state constructor
    def __init__(self):

        #Creates an starting state board
        self.board = [[-1 for i in range(8)] for i in range(8)]
        self.board[3][3] = State.WHITE
        self.board[4][4] = State.WHITE
        self.board[3][4] = State.BLACK
        self.board[4][3] = State.BLACK
        self.board_size = len(self.board)

    #Returns current board
    def getBoard(self):
        return self.board

    #Sets the board
    def setBoard(self,board):
        for i in range(self.board_size):
            for j in range(self.board_size):
                self.board[i][j] = board[i][j]
    
    #Prints the current state of the board
    def printBoard(self):
        print('\nCurrent Board State')      
        print('Black: ' + str(self.calculateScore(State.BLACK)) + ' - White: ' + str(self.calculateScore(State.WHITE)) + '\n')
        for i in range(self.board_size):
            if (i==0):
                print('  0 1 2 3 4 5 6 7')
            else:
                print()
            for j in range(self.board_size):
                if (j==0):
                    print(i, end=" ")
                if(self.board[i][j]==State.WHITE):
                    print('W', end=" ")
                elif(self.board[i][j]==State.BLACK):
                    print('B', end=" ")
                elif(self.board[i][j]==State.EMPTY):
                    print('-', end=" ")
        print('\n')

    #Returns opponent's colour
    def getOpponent(self,colour):
        if (colour == State.BLACK):
            opponent = State.WHITE
        elif (colour == State.WHITE):
            opponent = State.BLACK
        return opponent

    #Checks if the selected move is valid
    def makeMove(self,colour,i,j):
        opponent = self.getOpponent(colour)
        flip = []
        flip = self.isValidMove(colour,i,j)
        if (flip==None):
            return False
        else:
            for coordinates in flip:
                x = coordinates[0]
                y = coordinates[1]
                self.board[x][y] = colour
            flip.clear()
            self.board[i][j]=colour
            return True

    #Returns the coins that will be flipped if the move is valid, returns None otherwise
    def isValidMove(self,colour,i,j):
        if(self.board[i][j] != -1):
            return None
        opponent = self.getOpponent(colour)
        found_opponent = False
        valid = False

        coins= []
        flip = []
        #Searches for valid move on the left
        for a in range(j-1,-1,-1):
            if(self.board[i][a]==opponent):
                found_opponent = True
                coins.append([i,a])
            elif(self.board[i][a]==colour):
                if(found_opponent): 
                    for coordinates in coins:
                        flip.append(coordinates)
                    valid = True
                break
            elif(self.board[i][a]==State.EMPTY):
                found_opponent = False
                break
        coins.clear()
        found_opponent = False

        #Searches for valid move on the right
        for a in range(j+1,8,1):
            if(self.board[i][a]==opponent):
                found_opponent = True
                coins.append([i,a])                
            elif(self.board[i][a]==colour):
                if(found_opponent): 
                    for coordinates in coins:
                        flip.append(coordinates)
                    valid = True
                break
            elif(self.board[i][a]==State.EMPTY):
                found_opponent = False
                break
        coins.clear()
        found_opponent = False

        #Searches for valid move on the top
        for a in range(i-1,-1,-1):
            if(self.board[a][j]==opponent):
                found_opponent = True
                coins.append([a,j])              
            elif(self.board[a][j]==colour):
                if(found_opponent): 
                    for coordinates in coins:
                        flip.append(coordinates)
                    valid = True
                break
            elif(self.board[a][j]==State.EMPTY):
                found_opponent = False
                break
        coins.clear()
        found_opponent = False

        #Searches for valid move on the bottom
        for a in range(i+1,8,1):
            if(self.board[a][j]==opponent):
                found_opponent = True
                coins.append([a,j])               
            elif(self.board[a][j]==colour):
                if(found_opponent): 
                    for coordinates in coins:
                        flip.append(coordinates)
                    valid = True
                break
            elif(self.board[a][j]==State.EMPTY):
                found_opponent = False
                break
        coins.clear()
        found_opponent = False

        #Top-left diagonally
        x=i-1
        y=j-1
        while (x>=0 and y>=0):
             if(self.board[x][y]==opponent):
                found_opponent = True
                coins.append([x,y])
             elif(self.board[x][y]==colour):
                 if(found_opponent): 
                    for coordinates in coins:
                       flip.append(coordinates)
                    valid = True
                 break
             elif(self.board[x][y]==State.EMPTY):
                 found_opponent = False
                 break
             x=x-1
             y=y-1
        coins.clear()
        found_opponent = False
        
        #Top-right diagonally
        x=i-1
        y=j+1
        while (x>=0 and y<=7):
            if(self.board[x][y]==opponent):
                found_opponent = True
                coins.append([x,y])
            elif(self.board[x][y]==colour):
                 if(found_opponent): 
                    for coordinates in coins:
                      flip.append(coordinates)
                    valid = True
                 break
            elif(self.board[x][y]==State.EMPTY):
                 found_opponent = False
                 break
            x=x-1
            y=y+1
        coins.clear()
        found_opponent = False

        #Bottom-left diagonally 
        x=i+1
        y=j-1   
        while (x<=7 and y>=0):
            if(self.board[x][y]==opponent):
                found_opponent = True
                coins.append([x,y])
            elif(self.board[x][y]==colour):
                 if(found_opponent): 
                    for coordinates in coins:
                      flip.append(coordinates)
                    valid = True
                 break
            elif(self.board[x][y]==State.EMPTY):
                 found_opponent = False
                 break
            x=x+1
            y=y-1
        coins.clear()
        found_opponent = False

        #Bottom-right diagonally 
        x=i+1
        y=j+1
        while (x<=7 and y<=7):
            if(self.board[x][y]==opponent):
                found_opponent = True
                coins.append([x,y])
            elif(self.board[x][y]==colour):
                 if(found_opponent):
                    for coordinates in coins:
                      flip.append(coordinates)
                    valid = True
                 break
            elif(self.board[x][y]==State.EMPTY):
                 found_opponent = False
                 break
            x=x+1
            y=y+1
        coins.clear()
        found_opponent = False

        if (valid):
            return flip
        else:
            return None 

    #Determines if the game is over, returns true if no other move is available
    def isFinal(self,colour):
        opponent = self.getOpponent(colour)
        for i in range(self.board_size):
            for j in range(self.board_size):
                if(self.board[i][j]==State.EMPTY):
                    if(self.isValidMove(colour,i,j)!=None):
                       return False
        return True

    #Calculates the player's current score
    def calculateScore(self,colour):
        
        score = 0
        for i in range(self.board_size):
            for j in range(self.board_size):
                if(self.board[i][j]==colour):
                    score += 1
        return score

    #Heuristic function that calculates the state's score
    def heuristic(self,colour):

        #Calculates the difference of the players' coins
        coin_difference = ((self.calculateScore(colour) - self.calculateScore(self.getOpponent(colour)))/(self.calculateScore(colour) + self.calculateScore(self.getOpponent(colour))))*100
        
        #Calculates available moves for each player
        max_counter=0
        min_counter=0
        for i in range(self.board_size):
            for j in range(self.board_size):
                if(self.isValidMove(colour,i,j)!=None):
                    max_counter+=1
                if(self.isValidMove(self.getOpponent(colour),i,j)):
                    min_counter+=1

        if(max_counter + min_counter!=0):
            choice_difference = ((max_counter - min_counter)/(max_counter + min_counter))*100
        else:
            choice_difference=0
        
        max_corner_counter=0
        min_corner_counter=0

        #Calculates top left corner score
        if(self.board[0][0]==colour):
            max_corner_counter+=1
        elif(self.board[0][0]==self.getOpponent(colour)):
            min_corner_counter+=1

        #Calculates top right corner score
        if(self.board[0][7]==colour):
            max_corner_counter+=1
        elif(self.board[0][7]==self.getOpponent(colour)):
            min_corner_counter+=1

        #Calculates bottom left corner score
        if(self.board[7][0]==colour):
            max_corner_counter+=1
        elif(self.board[7][0]==self.getOpponent(colour)):
            min_corner_counter+=1

        #Calculates bottom right corner score
        if(self.board[7][7]==colour):
            max_corner_counter+=1
        elif(self.board[7][7]==self.getOpponent(colour)):
            min_corner_counter+=1
        
        if(max_corner_counter + min_corner_counter!=0):
            corner_difference = ((max_corner_counter - min_corner_counter)/(max_corner_counter + min_corner_counter))*100
        else:
            corner_difference=0

        State.state_score = coin_difference*(0.15) + choice_difference*(0.15) + corner_difference*(0.7)
        return State.state_score
    
    #Produces the children of the current state
    def getChildren(self,colour):
        
        children = []
        for i in range(self.board_size):
            for j in range(self.board_size):
                new_state = State()
                new_state.setBoard(self.board)
                if(new_state.makeMove(colour,i,j)):
                    children.append(new_state) 
                else:
                    new_state = None

        return children