#isAnshTHEmaN - Minesweeper
import tkinter as tk
from tkinter import messagebox
import random

class Minesweeper:
    def __init__(self, width, height, numBombs):
        self.width = width
        self.height = height
        self.numBombs = numBombs
        self.board = [[0 for _ in range(width)] for _ in range(height)]
        self.flags = 0
        self.create_board()
        self.create_gui()

    def create_board(self):
        bombs_placed = 0
        while bombs_placed < self.numBombs:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.board[y][x] != -1:
                self.board[y][x] = -1
                bombs_placed += 1
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if 0 <= x + i < self.width and 0 <= y + j < self.height and self.board[y + j][x + i] != -1:
                            self.board[y + j][x + i] += 1

    def create_gui(self):
        self.root = tk.Tk()
        self.buttons = [[tk.Button(self.root, width=2, height=1, command=lambda x=x, y=y: self.click(x, y)) for x in range(self.width)] for y in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                self.buttons[y][x].grid(row=y, column=x)
        self.root.mainloop()

    def click(self, x, y):
        if self.board[y][x] == -1:
            self.game_over()
        else:
            self.reveal(x, y)
            if self.check_win():
                self.game_won()

    def reveal(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height and self.buttons[y][x]['state'] != 'disabled':
            self.buttons[y][x]['state'] = 'disabled'
            if self.board[y][x] == 0:
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        self.reveal(x + i, y + j)

    def game_over(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == -1:
                    self.buttons[y][x]['text'] = '*'
        messagebox.showerror('Minesweeper', 'KABOOM! You lose.')
        self.root.destroy()

    def game_won(self):
        messagebox.showinfo('Minesweeper', 'Congratulations -- you won!')
        self.root.destroy()

    def check_win(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] != -1 and self.buttons[y][x]['state'] != 'disabled':
                    return False
        return True
    
    def reveal(self, x, y):
    if 0 <= x < self.width and 0 <= y < self.height and self.buttons[y][x]['state'] != 'disabled':
        self.buttons[y][x]['state'] = 'disabled'
        if self.board[y][x] == 0:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    self.reveal(x + i, y + j)
        elif self.board[y][x] > 0:
            self.buttons[y][x]['text'] = str(self.board[y][x])

play_minesweeper = Minesweeper
play_minesweeper(12, 10, 15)
