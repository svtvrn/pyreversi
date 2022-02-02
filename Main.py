from State import *
from SpaceSearcher import *
import math

#Initializing Board.
state = State()
state.printBoard()
depth = int(input("Please enter the maximum search depth of the algorithm: "))

#Determines who plays first.
print('Do you want to play first?')
while(True):
    answer = input('Enter "Y" to play first or "N" to let the CPU play first: ')
    if(answer=='Y' or answer=='y'):
        state.player_turn = True
        player_colour = State.BLACK
        cpu_colour = State.WHITE
        break
    elif(answer=='N'or answer=='n'):
        state.player_turn = False
        player_colour = State.WHITE
        cpu_colour = State.BLACK
        break
    else:
        print("Wrong answer.")

player_pass = False
cpu_pass = False

# Game Loop.
# Terminates when no further move is available.
# Black player goes first. 
while True:

    # Player's Turn.
    if(state.player_turn):
        print("It's your turn!")
        # Checks if Player has no moves left.
        if(state.isFinal(player_colour)):
            player_pass = True
            print('You have no moves left.')
            state.player_turn = False
        else:
            player_pass = False                     
            while (True):
                print("Enter coordinates:")                          
                x = input('Row: ')
                y = input('Column: ')
                if(state.makeMove(player_colour,int(x),int(y))):
                    state.player_turn = False
                    state.printBoard()
                    break
                else:                    
                    print('Invalid move!')
     
    # Checks if the game is over.
    if(player_pass and cpu_pass):
        print('Game Over!')
        break

    # CPU's Turn.                
    if(not state.player_turn):
        print("It's CPU's turn!")
        # Checks if CPU has no moves left.
        if(state.isFinal(cpu_colour)):
            cpu_pass = True
            print('CPU has no moves left.')
            state.player_turn = True
        else:
            cpu_pass = False          
            if(cpu_colour==State.WHITE):
                best_score = math.inf
                best_move=[]
                for i in range(state.board_size):
                    for j in range(state.board_size):
                        if(state.isValidMove(cpu_colour,i,j)!=None):
                            current_score = SpaceSearcher.minimax(state,depth,-math.inf,math.inf,cpu_colour)
                            if(current_score<best_score):
                                best_move.clear()
                                best_score = current_score
                                best_move.append(i)
                                best_move.append(j)

                state.makeMove(cpu_colour,best_move[0],best_move[1])

            elif(cpu_colour==State.BLACK):
                best_score = -math.inf
                best_move=[]
                for i in range(state.board_size):
                    for j in range(state.board_size):
                        if(state.isValidMove(cpu_colour,i,j)!=None):
                            current_score = SpaceSearcher.minimax(state,depth,-math.inf,math.inf,cpu_colour)
                            if(current_score>best_score):
                                best_move.clear()
                                best_score = current_score
                                best_move.append(i)
                                best_move.append(j)

                state.makeMove(cpu_colour,best_move[0],best_move[1])

            state.printBoard()
            state.player_turn = True

    # Checks if the game is over.
    if(player_pass and cpu_pass):
        print('Game Over!')
        break
    
player_score = state.calculateScore(player_colour)
cpu_score = state.calculateScore(cpu_colour)
if (player_score > cpu_score):
    print("You won! Congratulations!")
elif (player_score < cpu_score):
    print("You lost! Better luck next time!")
else:
    print("Draw!")

        
    