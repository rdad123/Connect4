"""
    Program - Connect 4
    Name - Robbie D A Dickson
    Student ID - 2935586
    Advanced Programming with Python Assignment
"""
import numpy as np
class GameBoard:
    def __init__(self):
        self.board = np.array([
            ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
            ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
            ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
            ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
            ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
            ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]
        ])

    def addToken(self, player, row):
        if player == 1:
            token = "[X]"
        else:
            token = "[O]"

        for r in range(5, -1, -1):
            if self.board[r][row] == "[ ]":
                self.board[r][row] = token
                placed = True
            else:
                placed = False
            if placed == True:
                break

    def __repr__(self):
        return '\n' + '\n'.join([' '.join(row) for row in self.board])