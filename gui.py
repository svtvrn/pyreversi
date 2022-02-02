from tkinter import *
from tkinter import messagebox

from State import *
from SpaceSearcher import *
import math
import time

root=Tk()
root.title('Reversi')

#Variables used for the frame values.
player_colour = 0
cpu_colour = 1
player_text = "B"
cpu_text = "W"
cpu_pass = False
state = State()
choice =IntVar(value=1)
score = StringVar(value="Score: Player: "+str(state.calculateScore(player_colour))+"  CPU: "+str(state.calculateScore(cpu_colour)))
score_label = Label(root,text=score.get(),font=("Helvetica",15))

depth_label = Label(root,text=("Enter a maximum search depth"),font=("Helvetica",15))
depth_label.grid(row=0,column=2,pady=5,padx=10)
depth = Entry(root,font=("Helvetica",15))
depth.grid(row=1,column=2,pady=5,padx=10)

#Pressing confirm calls gameloop() to draw the main board frame.
def depthClick():
    if(int(depth.get())>0):
        gameloop()

#Assigns colours for the player and CPU based on the player's choice.
def assignColours(val):
    global player_colour
    global cpu_colour
    global player_text
    global cpu_text
    if(val):
        player_colour = State.BLACK
        cpu_colour = State.WHITE
        player_text = "B"
        cpu_text = "W"
    elif(not val):
        player_colour = State.WHITE
        cpu_colour = State.BLACK
        player_text = "W"
        cpu_text = "B"

question = Label(root,text=("Do you wanna play first?"),font=("Helvetica",15))
question.grid(row=3,column=2,pady=5)
first = Radiobutton(root, text="First",font=("Helvetica",12),height=1,width=7, variable=choice, value=1, command=lambda: (assignColours(1)))
second =  Radiobutton(root, text="Second",font=("Helvetica",12),height=1,width=7, variable=choice, value=0, command=lambda: (assignColours(0)))
first.grid(row=4,column=2)
second.grid(row=5,column=2)

depth_button = Button(root,text="Confirm",font=("Helvetica",12),height=1,width=6,command=depthClick)
depth_button.grid(row=6,column=2,pady=5)

#Creates the board frame with the score.
def gameloop():
    depth.grid_forget()
    depth_button.grid_forget()
    depth_label.grid_forget()
    question.grid_forget()
    first.grid_forget()
    second.grid_forget()
    for i in range (state.board_size):
        for j in range (state.board_size):
            if(state.board[i][j]==-1):
                button = Button (root,text=" ",font=("Helvetica",20),height=2,width=4,bg="white",command=lambda row=i, col=j: click(button,row,col))
            elif(state.board[i][j]==0):
                button = Button (root,text="B",font=("Helvetica",20),height=2,width=4,bg="white",command=lambda row=i, col=j: click(button,row,col))
            elif(state.board[i][j]==1):
                button = Button (root,text="W",font=("Helvetica",20),height=2,width=4,bg="white",command=lambda row=i, col=j: click(button,row,col))
            button.grid(row=i,column=j)
    score_label.grid(row=9,column=1,columnspan = 5)
    playerPass()
    if(cpu_colour==state.BLACK):
        cpuplay()

#CPU turn, checking if CPU has available moves, proceeds to choose the best move based on minimax and changing the board frame.
def cpuplay():
    global cpu_pass
    if(state.isFinal(cpu_colour)):
        cpu_pass = True
        playerPass()
        win = Toplevel()
        win.wm_title("Reversi")
        err = Label(win, text="CPU doesn't have any available moves, play again",font=("Helvetica",15))
        err.pack(padx = 30, pady=30)
    else:
        cpu_pass=False
        if(cpu_colour==State.WHITE):
            best_score = math.inf
            best_move=[]
            for i in range(state.board_size):
                for j in range(state.board_size):
                    if(state.isValidMove(cpu_colour,i,j)!=None):
                        current_score = SpaceSearcher.minimax(state,int(depth.get()),-math.inf,math.inf,cpu_colour)
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
                        current_score = SpaceSearcher.minimax(state,int(depth.get()),-math.inf,math.inf,cpu_colour)
                        if(current_score>best_score):
                            best_move.clear()
                            best_score = current_score
                            best_move.append(i)
                            best_move.append(j)
            state.makeMove(cpu_colour,best_move[0],best_move[1])
        for i in range (state.board_size):
            for j in range (state.board_size):
                if(state.board[i][j]==cpu_colour):
                    widget = root.grid_slaves(row=i, column=j)[0]
                    widget.config(text=cpu_text)
        score.set(value="Score: Player: "+str(state.calculateScore(player_colour))+"  CPU: "+str(state.calculateScore(cpu_colour)))
        score_label.config(text=score.get())   
        playerPass()

#Clicks on a button, move is made if the position is valid. If it is the move happens, board frame updates and CPU plays. If not the button flashes.
def click(button,i,j):     
    if(state.makeMove(player_colour,i,j)):
        for i in range (state.board_size):
            for j in range (state.board_size):
                if(state.board[i][j]==player_colour):
                    widget = root.grid_slaves(row=i, column=j)[0]
                    widget.config(text=player_text)
        score.set(value="Score: Player: "+str(state.calculateScore(player_colour))+"  CPU: "+str(state.calculateScore(cpu_colour)))
        score_label.config(text=score.get())
        cpuplay()
    else:
        root.grid_slaves(row=i, column=j)[0].flash()

#Creates a "pass" button when the player has no available moves. Also checks for game-over.
def playerPass():
    if(state.isFinal(player_colour)):
        if(state.isFinal(cpu_colour)):
            gameOver()
            return;
        player_pass = Button(root,text="PASS",font=("Helvetica",15),height=1,width=8,command=lambda: destroyPass(player_pass) )
        player_pass.grid(row=9,column=6,columnspan = 3)

#Function that destroys the pass button widget, CPU plays next.
def destroyPass(button):
    button.destroy()
    cpuplay()

#Pop-up window after the game ends, presenting score.
def gameOver():
    win = Toplevel()
    win.wm_title("Reversi")
    err = Label(win, text="Game Over!",font=("Helvetica",15))
    err.pack(padx = 30, pady=30)
    final_score = Label(win, text=score.get(),font=("Helvetica",15))
    final_score.pack(pady=10)

root.mainloop()