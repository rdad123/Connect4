from GameBoard import GameBoard


class Game:

    def __init__(self):
        self.board_manager = GameBoard()
        self.current_player_num = 1
        self.game_in_progress = True
        self.winner = None

    def reset_game(self):
        self.board_manager = GameBoard()
        self.current_player_num = 1
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
            elif self.board_manager.getWinP2():
                self.winner = 2
                self.game_in_progress = False
            else:
                self.current_player_num = 2 if self.current_player_num == 1 else 1

            return True

        return False

    def get_board_state(self):
        return self.board_manager.getBoard()

    def get_current_player_token(self):
        return self.board_manager.PLAYER1_TOKEN if self.current_player_num == 1 else self.board_manager.PLAYER2_TOKEN

    def get_winner(self):
        return self.winner

    def is_in_progress(self):
        return self.game_in_progress