import random
from copy import deepcopy

class AI:
    def __init__(self):
        self.column_list = [0, 1, 2, 3, 4, 5, 6]

        # Minimax
        self.max_val = 2
        self.best_move = -1

    def generate_move(self, board):
        #col = random.choice(self.column_list)
        #x = self.countSequence(board, 1, 2)
        #print(x)
        self.MiniMaxAlphaBeta(board, 5, 2)
        for i in range(5, -1, -1):
           if board.field[i][self.best_move] == 0:
               if board.player_color == 'Red':
                   board.field[i][self.best_move] = 2
               else:
                   board.field[i][self.best_move] = 1
               board.player_turn = True
               return

    def countSequence(self, board, player, length):
        def verticalSeq(row, col):
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

        def horizontalSeq(row, col):
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

        def negDiagonalSeq(row, col):
            count = 0
            colIndex = col
            for rowIndex in range(row, -1, -1):
                if colIndex > 5:
                    break
                elif board.field[rowIndex][colIndex] == board.field[row][col]:
                    count += 1
                else:
                    break
                colIndex += 1  # increment column when row is incremented
            if count >= length:
                return 1
            else:
                return 0

        def posDiagonalSeq(row, col):
            count = 0
            colIndex = col
            for rowIndex in range(row, 6):
                if colIndex > 5:
                    break
                elif board.field[rowIndex][colIndex] == board.field[row][col]:
                    count += 1
                else:
                    break
                colIndex += 1
            if count >= length:
                return 1
            else:
                return 0

        totalCount = 0
        for row in range(6):
            for col in range(7):
                if board.field[row][col] == player:
                    totalCount += verticalSeq(row, col)
                    totalCount += horizontalSeq(row, col)
                    totalCount += (posDiagonalSeq(row, col) + negDiagonalSeq(row, col))
        return totalCount

    def utilityValue(self, board, player):
        if player == 1:
            opponent = 2
        else:
            opponent = 1

        player_fours = self.countSequence(board, player, 4)
        player_threes = self.countSequence(board, player, 3)
        player_twos = self.countSequence(board, player, 2)
        player_score = player_fours * 99999 + player_threes * 999 + player_twos * 99

        opponent_fours = self.countSequence(board, opponent, 4)
        opponent_threes = self.countSequence(board, opponent, 3)
        opponent_twos = self.countSequence(board, opponent, 2)
        opponent_score = opponent_fours * 99999 + opponent_threes * 999 + opponent_twos * 99

        if opponent_fours > 0:
            # This means that the current player lost the game
            return float('-inf')
        else:
            return player_score - opponent_score

    # Sequence of 4 means the game is over
    def gameIsOver(self, board):
        if self.countSequence(board, 1, 4) >= 1:
            return True
        elif self.countSequence(board, 2, 4) >= 1:
            return True
        else:
            return False

    def isValidMove(self, col, board):
        for row in range(6):
            if board[row][col] == 0:
                return True
        return False

    def MiniMaxAlphaBeta(self, board, depth, player):
        valid_moves = board.get_valid_moves()
        self.best_move = valid_moves[0]
        bestScore = float("-inf")

        alpha = float("-inf")
        beta = float("inf")

        if player == 2:
            opponent = 1
        else:
            opponent = 2

        # go through all of those boards
        for move in valid_moves:
            temp_board = self.makeMove(board, move, player)[0]
            # call min on that new board
            boardScore = self.minimizeBeta(temp_board, depth - 1, alpha, beta, player, opponent)
            if boardScore > bestScore:
                bestScore = boardScore
                self.best_move = move
        return

    def minimizeBeta(self, board, depth, a, b, player, opponent):
        validMoves = []
        for col in range(7):
            # if column col is a legal move...
            if self.isValidMove(col, board):
                # make the move in column col for curr_player
                temp = self.makeMove(board, col, player)[2]
                validMoves.append(temp)

        # check to see if game over
        if depth == 0 or len(validMoves) == 0 or self.gameIsOver(board):
            return self.utilityValue(board, player)

        validMoves = board.get_valid_moves()
        beta = b

        # if end of tree evaluate scores
        for move in validMoves:
            boardScore = float("inf")
            # else continue down tree as long as ab conditions met
            if a < beta:
                tempBoard = self.makeMove(board, move, opponent)[0]
                boardScore = self.maximizeAlpha(tempBoard, depth - 1, a, beta, player, opponent)

            if boardScore < beta:
                beta = boardScore
        return beta

    def maximizeAlpha(self, board, depth, a, b, player, opponent):
        validMoves = []
        for col in range(7):
            # if column col is a legal move...
            if self.isValidMove(col, board):
                # make the move in column col for curr_player
                temp = self.makeMove(board, col, player)[2]
                validMoves.append(temp)
        # check to see if game over
        if depth == 0 or len(validMoves) == 0 or self.gameIsOver(board):
            return self.utilityValue(board, player)

        alpha = a
        # if end of tree, evaluate scores
        for move in validMoves:
            boardScore = float("-inf")
            if alpha < b:
                tempBoard = self.makeMove(board, move, player)[0]
                boardScore = self.minimizeBeta(tempBoard, depth - 1, alpha, b, player, opponent)

            if boardScore > alpha:
                alpha = boardScore
        return alpha