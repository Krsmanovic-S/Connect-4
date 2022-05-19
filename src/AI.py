from random import shuffle


class AI:
    def __init__(self):
        self.best_move = 0
        self.search_depth = 3
        self.computer_symbol = 2

    def change_computer_symbol(self):
        if self.computer_symbol == 2:
            self.computer_symbol = 1
        else:
            self.computer_symbol = 2

    def generate_best(self, board):
        self.alpha_beta_minimax(board, self.search_depth, self.computer_symbol)

        for i in range(5, -1, -1):
            if board.field[i][self.best_move] == 0:
                board.field[i][self.best_move] = self.computer_symbol
                board.player_turn = True
                return

    @staticmethod
    def count_sequence(board, player, length):
        # Function will count the amount of connected pieces
        # that are a certain length.
        def vertical(row, col):
            count = 0
            for rowIndex in range(row, 6):
                if board.field[rowIndex][col] == board.field[row][col]:
                    count += 1
                else:
                    break
            if count >= length:
                return 1
            else:
                return 0

        def horizontal(row, col):
            count = 0
            for colIndex in range(col, 7):
                if board.field[row][colIndex] == board.field[row][col]:
                    count += 1
                else:
                    break
            if count >= length:
                return 1
            else:
                return 0

        def negative_diagonal(row, col):
            count = 0
            col_index = col
            for rowIndex in range(row, -1, -1):
                if col_index > 6:
                    break
                elif board.field[rowIndex][col_index] == board.field[row][col]:
                    count += 1
                else:
                    break
                col_index += 1  # increment column when row is incremented
            if count >= length:
                return 1
            else:
                return 0

        def positive_diagonal(row, col):
            count = 0
            col_index = col
            for rowIndex in range(row, 6):
                if col_index > 6:
                    break
                elif board.field[rowIndex][col_index] == board.field[row][col]:
                    count += 1
                else:
                    break
                col_index += 1  # increment column when row incremented
            if count >= length:
                return 1
            else:
                return 0

        total_count = 0

        for row in range(6):
            for col in range(7):
                if board.field[row][col] == player:
                    total_count += vertical(row, col)
                    total_count += horizontal(row, col)
                    total_count += (positive_diagonal(row, col) + negative_diagonal(row, col))

        return total_count

    def utility_value(self, board, player):
        # This function is used to evaluate the current score of a board.
        if player == 2:
            opponent = 1
        else:
            opponent = 2

        player_fours = self.count_sequence(board, player, 4)
        player_threes = self.count_sequence(board, player, 3)
        player_twos = self.count_sequence(board, player, 2)
        player_score = player_fours * 9999 + player_threes * 99 + player_twos * 9

        opponent_fours = self.count_sequence(board, opponent, 4)
        opponent_threes = self.count_sequence(board, opponent, 3)
        opponent_twos = self.count_sequence(board, opponent, 2)
        opponent_score = opponent_fours * 9999 + opponent_threes * 99 + opponent_twos * 9

        if opponent_fours > 0:
            return float('-inf')
        else:
            return player_score - opponent_score

    def game_is_over(self, board):
        if self.count_sequence(board, 1, 4) >= 1 or\
           self.count_sequence(board, 2, 4) >= 1:
            return True
        else:
            return False

    def alpha_beta_minimax(self, board, depth, player):
        valid_moves = board.get_valid_columns()
        shuffle(valid_moves)

        best_score = float("-inf")
        alpha = float("-inf")
        beta = float("inf")

        if player == 2:
            opponent = 1
        else:
            opponent = 2

        for move in valid_moves:
            # Make every move that we can, calculate the new board score
            # and then check how it compares to the best one we have.
            temp_board = board.make_move(move, player)[0]

            # We need to call the appropriate function based on the AI's symbol,
            # as well as deal with the best move value according to the same thing.
            board_score = self.minimize_beta(temp_board, depth - 1, alpha, beta, player, opponent)

            if board_score > best_score:
                best_score = board_score
                self.best_move = move

    def minimize_beta(self, board, depth, alpha, beta, player, opponent):
        valid_moves = []
        for col in range(7):
            if board.is_valid_move(col):
                temp = board.make_move(col, player)[2]
                valid_moves.append(temp)

        if depth == 0 or len(valid_moves) == 0 or self.game_is_over(board):
            return self.utility_value(board, player)

        valid_moves = board.get_valid_columns()
        beta = beta

        for move in valid_moves:
            board_score = float("inf")

            if alpha < beta:
                temp_board = board.make_move(move, opponent)[0]
                board_score = self.maximize_alpha(temp_board, depth - 1, alpha, beta, player, opponent)

            # We must always have the order of beta < board_score < alpha.
            if board_score < beta:
                beta = board_score
        return beta

    def maximize_alpha(self, board, depth, alpha, beta, player, opponent):
        valid_moves = []
        for col in range(7):
            if board.is_valid_move(col):
                temp = board.make_move(col, player)[2]
                valid_moves.append(temp)

        if depth == 0 or len(valid_moves) == 0 or self.game_is_over(board):
            return self.utility_value(board, player)

        alpha = alpha

        for move in valid_moves:
            board_score = float("-inf")
            # We must always have the order of beta < board_score < alpha.
            if alpha < beta:
                temp_board = board.make_move(move, player)[0]
                board_score = self.minimize_beta(temp_board, depth - 1, alpha, beta, player, opponent)
            if board_score > alpha:
                alpha = board_score
        return alpha
