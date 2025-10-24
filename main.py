"""
    Program - Connect 4
    Name - Robbie D A Dickson
    Student ID - 2935586
    Advanced Programming with Python Assignment
"""
from GameBoard import GameBoard
def main():
    game1 = GameBoard()
    showBoard(game1)

    for i in range(1, 43):
        turn = i
        if turn % 2 == 0:
            player = 2
        else:
            player = 1
        valid_number = False
        while(valid_number == False):
            row_input = input(f"player {player}, enter row to put token, must be 1-7: ")
            try:
                row = int(row_input) - 1
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 7.")
                valid_number = False
            if(0 <= row < 7):
                valid_number = True
            else:
                print("Invalid input. Please enter a number between 1 and 7.")
                valid_number = False
        game1.addToken(player, row)

        showBoard(game1)

    pass
def showBoard(game):
    print(game)
    print("1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣")
    game.checkBoardState()

main()
