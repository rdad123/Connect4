"""
    Program - Connect 4
    Name - Robbie D A Dickson
    Student ID - 2935586
    Advanced Programming with Python Assignment
"""
import tkinter as tk
from Game import Game
from GUI import GUI
from GameBoard import GameBoard
def main():
    if __name__ == "__main__":
        root = tk.Tk()
        app = GUI(root)
        root.mainloop()
    game1 = Game()
    game1.createGame()

main()
