import random

class AI:
    def __init__(self):
        self.computer_color = 'Yellow'
        self.column_list = [0, 1, 2, 3, 4, 5, 6]

    def generate_move(self, board):
        col = random.choice(self.column_list)

        for i in range(5, -1, -1):
            if board.field[i][col] == 0:
                board.field[i][col] = 2
                board.player_turn = True
                return
