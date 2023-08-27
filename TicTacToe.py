import board_game
class TicTacToe(board_game.Board_game):
    def __init__(self):
        self.board = board_game.Board_game(3,3,3)
        self.board.game()

TTC = TicTacToe()
