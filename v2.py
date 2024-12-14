import random
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy

sign = 0

# creates the empty board.
global board
board = [[" " for x in range(3)] for y in range(3)]

# Function to check if a player has won
def winner(b, l):
    return (
        (b[0][0] == l and b[0][1] == l and b[0][2] == l) or
        (b[1][0] == l and b[1][1] == l and b[1][2] == l) or
        (b[2][0] == l and b[2][1] == l and b[2][2] == l) or
        (b[0][0] == l and b[1][0] == l and b[2][0] == l) or
        (b[0][1] == l and b[1][1] == l and b[2][1] == l) or
        (b[0][2] == l and b[1][2] == l and b[2][2] == l) or
        (b[0][0] == l and b[1][1] == l and b[2][2] == l) or
        (b[0][2] == l and b[1][1] == l and b[2][0] == l)
    )

# Check if the board is full
def isfull():
    for row in board:
        if " " in row:
            return False
    return True

# Function to handle a player's move
def get_text(i, j, gb, l1, l2):
    global sign
    if board[i][j] == " ":
        if sign % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=board[i][j])
        
        if winner(board, "X"):
            gb.destroy()
            messagebox.showinfo("Winner", "Player 1 (X) wins!")
        elif winner(board, "O"):
            gb.destroy()
            messagebox.showinfo("Winner", "Player 2 (O) wins!")
        elif isfull():
            gb.destroy()
            messagebox.showinfo("Tie", "It's a tie!")

# Function to create the game board for multiplayer
def gameboard_pl(game_board, l1, l2):
    global button
    button = []
    for i in range(3):
        button.append([])
        for j in range(3):
            get_t = partial(get_text, i, j, game_board, l1, l2)
            btn = Button(game_board, bd=5, command=get_t, height=4, width=8)
            btn.grid(row=i+3, column=j)
            button[i].append(btn)
    game_board.mainloop()

# Function to handle computer's move
def pc():
    possible_moves = [[i, j] for i in range(3) for j in range(3) if board[i][j] == " "]
    for let in ["O", "X"]:
        for move in possible_moves:
            board_copy = deepcopy(board)
            board_copy[move[0]][move[1]] = let
            if winner(board_copy, let):
                return move

    corners = [move for move in possible_moves if move in [[0, 0], [0, 2], [2, 0], [2, 2]]]
    if corners:
        return random.choice(corners)

    edges = [move for move in possible_moves if move in [[0, 1], [1, 0], [1, 2], [2, 1]]]
    if edges:
        return random.choice(edges)

    return random.choice(possible_moves)

# Function to handle a player's move against the computer
def get_text_pc(i, j, gb, l1, l2):
    global sign
    if board[i][j] == " ":
        if sign % 2 == 0:
            board[i][j] = "X"
            button[i][j].config(text="X")
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            sign += 1

        if winner(board, "X"):
            gb.destroy()
            messagebox.showinfo("Winner", "Player wins!")
        elif isfull():
            gb.destroy()
            messagebox.showinfo("Tie", "It's a tie!")
        else:
            move = pc()
            if move:
                board[move[0]][move[1]] = "O"
                button[move[0]][move[1]].config(text="O")
                sign += 1

                if winner(board, "O"):
                    gb.destroy()
                    messagebox.showinfo("Winner", "Computer wins!")
                elif isfull():
                    gb.destroy()
                    messagebox.showinfo("Tie", "It's a tie!")

# Function to create the game board for single-player
def gameboard_pc(game_board, l1, l2):
    global button
    button = []
    for i in range(3):
        button.append([])
        for j in range(3):
            get_t = partial(get_text_pc, i, j, game_board, l1, l2)
            btn = Button(game_board, bd=5, command=get_t, height=4, width=8)
            btn.grid(row=i+3, column=j)
            button[i].append(btn)
    game_board.mainloop()

# Initialize the game board for single-player
def withpc(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title("Tic Tac Toe")
    l1 = Button(game_board, text="Player: X", width=10)
    l1.grid(row=1, column=1)
    l2 = Button(game_board, text="Computer: O", width=10, state=DISABLED)
    l2.grid(row=2, column=1)
    gameboard_pc(game_board, l1, l2)

# Initialize the game board for multiplayer
def withplayer(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title("Tic Tac Toe")
    l1 = Button(game_board, text="Player 1: X", width=10)
    l1.grid(row=1, column=1)
    l2 = Button(game_board, text="Player 2: O", width=10, state=DISABLED)
    l2.grid(row=2, column=1)
    gameboard_pl(game_board, l1, l2)

# Main menu to choose game mode
def play():
    menu = Tk()
    menu.geometry("250x250")
    menu.title("Tic Tac Toe")
    wpc = partial(withpc, menu)
    wpl = partial(withplayer, menu)

    head = Button(menu, text="---Welcome to Tic Tac Toe---",
                  bg="black", fg="grey", width=500, font="summer", state=DISABLED)
    B1 = Button(menu, text="Single Player", command=wpc, bg="black", fg="grey", font="summer")
    B2 = Button(menu, text="Multiplayer", command=wpl, bg="black", fg="grey", font="summer")
    B3 = Button(menu, text="Exit", command=menu.quit, bg="black", fg="grey", font="summer")

    head.pack(side="top")
    B1.pack(side="top")
    B2.pack(side="top")
    B3.pack(side="top")
    menu.mainloop()

# Run the game
if __name__ == "__main__":
    play()

