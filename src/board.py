import pygame
from constants import *

class Board:
    # Constructor
    def __init__(self):
        self.field = [[0 for i in range(7)] for j in range(6)]

        self.field_height = len(self.field[0])
        self.field_width = len(self.field)

        self.player_turn = True
        self.game_over = False
        self.player_color = 'Red'

    # Functions
    def draw_rect(self, surface, fill_color, outline_color, rect, border = 1):
        surface.fill(outline_color, rect)
        surface.fill(fill_color, rect.inflate(-border * 2, -border * 2))

    def draw_grid(self, window):
        for i in range(6):
            for j in range(7):
                cell = pygame.Rect(j * 100, i * 100, 100, 100)
                self.draw_rect(window, GRAY, BLACK, cell)

                if self.field[i][j] == 0:
                    pygame.draw.circle(window, WHITE, (j * 100 + 50, i * 100 + 50), 45, 0)
                elif self.field[i][j] == 1:
                    pygame.draw.circle(window, RED, (j * 100 + 50, i * 100 + 50), 45, 0)
                elif self.field[i][j] == 2:
                    pygame.draw.circle(window, YELLOW, (j * 100 + 50, i * 100 + 50), 45, 0)
                else:
                    pygame.draw.circle(window, GREEN, (j * 100 + 50, i * 100 + 50), 45, 0)

    def play_move(self, mouse):
        col = mouse[0] // 100

        for i in range(5, -1, -1):
            if self.field[i][col] == 0:
                self.field[i][col] = 1
                self.player_turn = False
                return

    def check_winner(self):
        # Check rows for a winner.
        for y in range(self.field_height):
            for x in range(self.field_width - 3):
                if self.field[x][y] == self.field[x + 1][y] and \
                   self.field[x + 1][y] == self.field[x + 2][y] and \
                   self.field[x + 2][y] == self.field[x + 3][y]:
                    if self.field[x][y] != 0:
                        self.field[x][y], self.field[x+1][y], self.field[x+2][y], self.field[x+3][y] = 3, 3, 3, 3
                        self.game_over = True

        # Check columns.
        for x in range(self.field_width):
            for y in range(self.field_height - 3):
                if self.field[x][y] == self.field[x][y + 1] and \
                   self.field[x][y + 1] == self.field[x][y + 2] and \
                   self.field[x][y + 2] == self.field[x][y + 3]:
                    if self.field[x][y] != 0:
                        self.field[x][y], self.field[x][y+1], self.field[x][y+2], self.field[x][y+3] = 3, 3, 3, 3
                        self.game_over = True

        # Check left->right diagonals.
        for x in range(self.field_width - 3):
            for y in range(3, self.field_height):
                if self.field[x][y] == self.field[x + 1][y - 1] and \
                   self.field[x + 1][y - 1] == self.field[x + 2][y - 2] and \
                   self.field[x + 2][y - 2] == self.field[x + 3][y - 3]:
                    if self.field[x][y] != 0:
                        self.field[x][y], self.field[x+1][y-1], self.field[x+2][y-2], self.field[x+3][y-3] = 3, 3, 3, 3
                        self.game_over = True

        # Check right->left diagonals.
        for x in range(self.field_width - 3):
            for y in range(self.field_height - 3):
                if self.field[x][y] == self.field[x + 1][y + 1] and \
                   self.field[x + 1][y + 1] == self.field[x + 2][y + 2] and \
                   self.field[x + 2][y + 2] == self.field[x + 3][y + 3]:
                    if self.field[x][y] != 0:
                        self.winning_indexes = [(x, y), (x+1, y+1), (x+2, y+2), (x+3, y+3)]
                        self.field[x][y], self.field[x+1][y+1], self.field[x+2][y+2], self.field[x+3][y+3] = 3, 3, 3, 3
                        self.game_over = True

    def reset(self):
        self.field = [[0 for i in range(7)] for j in range(6)]
        self.player_turn = True
        self.game_over = False