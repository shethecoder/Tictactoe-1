import random
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy

sign = 0

# creates the empty board.
global board
board=[[" " for x in range(3)] for y in range(3)]

# Check 1 (O/X) wont the match or not
# according to the rules of the game
b="1"

def winner(b,1):
    return(
        (b[0][0] == 1 and b[0][1] == 1 and b[0][2] == 1)
        (b[1][0] == 1 and b[1][1] == 1 and b[1][2] == 1)
        (b[2][0] == 1 and b[2][1] == 1 and b[2][2] == 1)
        (b[0][0] == 1 and b[1][0] == 1 and b[2][0] == 1)
        (b[0][1] == 1 and b[1][1] == 1 and b[2][1] == 1)
        (b[0][2] == 1 and b[1][2] == 1 and b[2][2] == 1)
        (b[0][0] == 1 and b[1][1] == 1 and b[2][2] == 1)
        (b[0][2] == 1 and b[1][1] == 1 and b[2][0] == 1)
       
    )

# changing the text shown on the button when playing with another player

def get_text(i,j,gb,l1,l2):
    global sign
    if board[i][j] == ' ':

        if sign % 2 ==0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        sign +=1
        button[i][j].config(text=board[i][j])
    if winner(board,"X"):
        gb.destroy()
        box = messagebox.showinfo("Winner, Player 1 won the match")
    if winner(board,"O"):
        gb.destroy()
        box = messagebox.showinfo("Winner, Player 2 won the match")
    elif(isfull()):
        gb.destroy()
        box = messagebox.showinfo("Tie Game", "Tie Game")

    
def isfree(i,j):
    return board[i][j] == ""

# check if the board is full or not

def isFull():
    flag = True
    for i in board:
        if(i.count('') > 0):
            flag = False
    return flag

