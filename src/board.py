from constants import *


class Board:
    # Constructor
    def __init__(self):
        self.field = [[0 for i in range(7)] for j in range(6)]

        self._field_height = len(self.field[0])
        self._field_width = len(self.field)

        self.player_turn = True
        self.game_over = False
        self.player_color = 'Red'
        self.pvp = False

    # Functions
    @staticmethod
    def draw_rect(surface, fill_color, outline_color, rect, border=1):
        surface.fill(outline_color, rect)
        surface.fill(fill_color, rect.inflate(-border * 2, -border * 2))

    def draw_grid(self, window, mouse_x):
        # Width of the window as well as all the colors are defined in constants.py
        for i in range(6):
            for j in range(7):
                cell = pygame.Rect(j * (WIDTH // 7), i * (WIDTH // 7), 120, 120)

                if mouse_x // 120 == j:
                    self.draw_rect(window, HIGHLIGHTED, BLACK, cell)
                else:
                    self.draw_rect(window, GRAY, BLACK, cell)

                if self.field[i][j] == 0:
                    pygame.draw.circle(window, WHITE, (j * (WIDTH // 7) + 60, i * (WIDTH // 7) + 60), 55, 0)
                elif self.field[i][j] == 1:
                    pygame.draw.circle(window, RED, (j * (WIDTH // 7) + 60, i * (WIDTH // 7) + 60), 55, 0)
                elif self.field[i][j] == 2:
                    pygame.draw.circle(window, YELLOW, (j * (WIDTH // 7) + 60, i * (WIDTH // 7) + 60), 55, 0)
                else:
                    pygame.draw.circle(window, GREEN, (j * (WIDTH // 7) + 60, i * (WIDTH // 7) + 60), 55, 0)

    def play_move(self, mouse):
        col = mouse[0] // (WIDTH // 7)

        for i in range(5, -1, -1):
            if self.field[i][col] == 0:
                if self.player_color == 'Red':
                    self.field[i][col] = 1
                else:
                    self.field[i][col] = 2

                if not self.pvp:
                    self.player_turn = False
                else:
                    self.set_player_symbol()
                return

    def set_player_symbol(self):
        if self.player_color == 'Red':
            self.player_color = 'Yellow'
        else:
            self.player_color = 'Red'

    def check_winner(self):
        # Check rows for a winner.
        for y in range(self._field_height):
            for x in range(self._field_width - 3):
                if self.field[x][y] == self.field[x + 1][y] and \
                   self.field[x + 1][y] == self.field[x + 2][y] and \
                   self.field[x + 2][y] == self.field[x + 3][y]:
                    if self.field[x][y] != 0:
                        self.field[x][y], self.field[x+1][y], self.field[x+2][y], self.field[x+3][y] = 3, 3, 3, 3
                        self.game_over = True

        # Check columns.
        for x in range(self._field_width):
            for y in range(self._field_height - 3):
                if self.field[x][y] == self.field[x][y + 1] and \
                   self.field[x][y + 1] == self.field[x][y + 2] and \
                   self.field[x][y + 2] == self.field[x][y + 3]:
                    if self.field[x][y] != 0:
                        self.field[x][y], self.field[x][y+1], self.field[x][y+2], self.field[x][y+3] = 3, 3, 3, 3
                        self.game_over = True

        # Check left->right diagonals.
        for x in range(self._field_width - 3):
            for y in range(3, self._field_height):
                if self.field[x][y] == self.field[x + 1][y - 1] and \
                   self.field[x + 1][y - 1] == self.field[x + 2][y - 2] and \
                   self.field[x + 2][y - 2] == self.field[x + 3][y - 3]:
                    if self.field[x][y] != 0:
                        self.field[x][y], self.field[x+1][y-1], self.field[x+2][y-2], self.field[x+3][y-3] = 3, 3, 3, 3
                        self.game_over = True

        # Check right->left diagonals.
        for x in range(self._field_width - 3):
            for y in range(self._field_height - 3):
                if self.field[x][y] == self.field[x + 1][y + 1] and \
                   self.field[x + 1][y + 1] == self.field[x + 2][y + 2] and \
                   self.field[x + 2][y + 2] == self.field[x + 3][y + 3]:
                    if self.field[x][y] != 0:
                        self.field[x][y], self.field[x+1][y+1], self.field[x+2][y+2], self.field[x+3][y+3] = 3, 3, 3, 3
                        self.game_over = True

    def reset(self):
        self.field = [[0 for i in range(7)] for j in range(6)]
        self.game_over = False

        if not self.pvp:
            if self.player_color == 'Red':
                self.player_turn = True
            else:
                self.player_turn = False
        else:
            self.player_turn = True
            if self.player_color == 'Yellow':
                self.set_player_symbol()
