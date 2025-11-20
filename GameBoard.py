"""
    Program - Connect 4
    Name - Robbie D A Dickson
    Student ID - 2935586
    Advanced Programming with Python Assignment
"""
import numpy as np
class GameBoard:
    player1Win = False
    player2Win = False

    EMPTY_TOKEN = "⬛"
    PLAYER1_TOKEN = "🔴"
    PLAYER2_TOKEN = "🔵"
    def __init__(self):
        self.board = np.array([
            ["⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛"],
            ["⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛"],
            ["⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛"],
            ["⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛"],
            ["⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛"],
            ["⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛"]
        ])

    def addToken(self, player, row):
        if player == 1:
            token = "🔴"
        else:
            token = "🔵"

        for r in range(5, -1, -1):
            if self.board[r][row] == "⬛":
                self.board[r][row] = token
                placed = True
            else:
                placed = False
            if placed == True:
                break

    def rowFull(self, row):
        if(self.board[0][row] != "⬛"):
            return False
        else:
            return True

    def checkBoardState(self):
        player1Token = "🔴"
        player2Token = "🔵"

        self.checkWinHor(player1Token, player2Token)
        self.checkWinVer(player1Token, player2Token)
        self.checkWinDiagL(player1Token, player2Token)
        self.checkWinDiagR(player1Token, player2Token)


    def checkWinHor(self, player1Token, player2Token):
        for i in range(6):
            p1 = 0
            p2 = 0
            for x in range(7):
                currentSlot = self.board[i][x]
                if currentSlot == player1Token:
                    p1 += 1
                    p2 = 0
                elif currentSlot == player2Token:
                    p2 += 1
                    p1 = 0
                else:
                    p1 = 0
                    p2 = 0
                if p1 >= 4:
                    self.player1Win = True
                    print("player 1 wins horizontally")
                if p2 >= 4:
                    self.player2Win = True
                    print("player 2 wins horizontally")

    def checkWinVer(self, player1Token, player2Token):
        for i in range(7):
            p1 = 0
            p2 = 0
            for x in range(5, -1, -1):
                currentSlot = self.board[x][i]
                if currentSlot == player1Token:
                    p1 += 1
                    p2 = 0
                elif currentSlot == player2Token:
                    p2 += 1
                    p1 = 0
                else:
                    p1 = 0
                    p2 = 0
                if p1 >= 4:
                    self.player1Win = True
                    print("player 1 wins vertically")
                if p2 >= 4:
                    self.player2Win = True
                    print("player 2 wins vertically")

    def checkWinDiagL(self, player1Token, player2Token):
        p1 = 0
        p2 = 0
        rows = self.getHorizontalR()
        for i in range(6):
            row = rows[i]
            for x in range(6):
                currentSlot = row[x]
                if currentSlot == player1Token:
                    p1 += 1
                    p2 = 0
                elif currentSlot == player2Token:
                    p2 += 1
                    p1 = 0
                else:
                    p1 = 0
                    p2 = 0
                if p1 >= 4:
                    self.player1Win = True
                    print("player 1 wins diagonally")
                if p2 >= 4:
                    self.player2Win = True
                    print("player 2 wins diagonally")


    def checkWinDiagR(self, player1Token, player2Token):
        p1 = 0
        p2 = 0
        rows = self.getHorizontalL()
        for i in range(6):
            row = rows[i]
            for x in range(6):
                currentSlot = row[x]
                if currentSlot == player1Token:
                    p1 += 1
                    p2 = 0
                elif currentSlot == player2Token:
                    p2 += 1
                    p1 = 0
                else:
                    p1 = 0
                    p2 = 0
                if p1 >= 4:
                    self.player1Win = True
                    print("player 1 wins diagonally")
                if p2 >= 4:
                    self.player2Win = True
                    print("player 2 wins diagonally")
    def getHorizontalR(self):
        row1 = self.board[3][0], self.board[2][1], self.board[1][2], self.board[0][3],  "⬛",  "⬛"
        row2 = self.board[4][0], self.board[3][1], self.board[2][2], self.board[1][3], self.board[0][4],  "⬛"
        row3 = self.board[5][0], self.board[4][1], self.board[3][2], self.board[2][3], self.board[1][4], self.board[0][5]
        row4 = self.board[5][1], self.board[4][2], self.board[3][3], self.board[2][4], self.board[1][5], self.board[0][6]
        row5 = self.board[5][2], self.board[4][3], self.board[3][4], self.board[2][5], self.board[1][6],  "⬛"
        row6 = self.board[5][3], self.board[4][4], self.board[3][5], self.board[2][6],  "⬛",  "⬛"

        rowsR = row1, row2, row3, row4, row5, row6
        return rowsR

    def getHorizontalL(self):
        row1 = self.board[5][3], self.board[4][2], self.board[3][1], self.board[2][0],  "⬛",  "⬛"
        row2 = self.board[5][4], self.board[4][3], self.board[3][2], self.board[2][1], self.board[1][0],  "⬛"
        row3 = self.board[5][5], self.board[4][4], self.board[3][3], self.board[2][2], self.board[1][1], self.board[0][0]
        row4 = self.board[5][6], self.board[4][5], self.board[3][4], self.board[2][3], self.board[1][2], self.board[0][1]
        row5 = self.board[4][6], self.board[3][5], self.board[2][4], self.board[1][3], self.board[0][2],  "⬛"
        row6 = self.board[3][6], self.board[2][5], self.board[1][4], self.board[0][3],  "⬛",  "⬛"

        rowsL = row1, row2, row3, row4, row5, row6
        return rowsL


    def getBoard(self):
        print(self.board)
        return self.board

    def getWinP1(self):
        return self.player1Win

    def getWinP2(self):
        return self.player2Win

    def __repr__(self):
        return '\n' + '\n'.join([' '.join(row) for row in self.board])