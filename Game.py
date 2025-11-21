"""
    Program - Connect 4
    Name - Robbie D A Dickson
    Student ID - 2935586
    Advanced Programming with Python Assignment
"""
from random import randrange

from GameBoard import GameBoard


class Game:
    DIFFICULTY = 0

    def __init__(self):
        self.board_manager = GameBoard()
        self.current_player_num = 1
        self.game_in_progress = True
        self.winner = None

    def reset_game(self, difficulty=None):
        self.board_manager = GameBoard()
        if difficulty is not None:
            self.DIFFICULTY = difficulty
        else:
            self.DIFFICULTY = 0

        self.current_player_num = randrange(1, 3)
        self.game_in_progress = True
        self.winner = None

    def make_move(self, col_index):
        if not self.game_in_progress:
            return False

        row_placed = self.board_manager.addToken(self.current_player_num, col_index)

        if row_placed != -1:
            self.board_manager.checkBoardState()

            if self.board_manager.getWinP1():
                self.winner = 1
                self.game_in_progress = False
                print(f"DEBUG: Player 1 WIN state triggered!")
            elif self.board_manager.getWinP2():
                self.winner = 2
                self.game_in_progress = False
                print(f"DEBUG: Player 2 WIN state triggered!")
            else:
                self.current_player_num = 2 if self.current_player_num == 1 else 1

            return True

        return False

    def AI_Move(self):
        if self.DIFFICULTY == 1:
            row_placed = -1
            while row_placed == -1:
                move = randrange(0, 7)
                row_placed = self.board_manager.addToken(2, move)

            if row_placed != -1:
                self.board_manager.checkBoardState()

                if self.board_manager.getWinP2():
                    self.winner = 2
                    self.game_in_progress = False
                else:
                    self.current_player_num = 1

                return move

            return -1

    def get_board_state(self):
        return self.board_manager.getBoard()

    def get_current_player_token(self):
        return self.board_manager.PLAYER1_TOKEN if self.current_player_num == 1 else self.board_manager.PLAYER2_TOKEN

    def get_winner(self):
        return self.winner

    def is_in_progress(self):
        return self.game_in_progress