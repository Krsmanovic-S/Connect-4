from board import *
from AI import AI
from button import Button


class Game:
    def __init__(self):
        # Window settings
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_icon(WINDOW_ICON)
        pygame.display.set_caption("Connect 4")

        # Variables
        self.mouse_pos = (-1, -1)
        self.board = Board()
        self.computer = AI()

        # Buttons
        self._play_button = Button(WIDTH // 2 - 200, 150, PLAY_BUTTON, HOVERED_PLAY)
        self._options_button = Button(WIDTH // 2 - 200, 350, OPTIONS_BUTTON, HOVERED_OPTIONS)
        self._exit_button = Button(WIDTH // 2 - 200, 550, EXIT_BUTTON, HOVERED_EXIT)

        self._player_color_red = Button(WIDTH // 2 - 200, 150, PLAYER_COLOR_RED, HOVERED_COLOR_RED)
        self._player_color_yellow = Button(WIDTH // 2 - 200, 150, PLAYER_COLOR_YELLOW, HOVERED_COLOR_YELLOW)
        self._pvp_disabled = Button(WIDTH // 2 - 200, 350, PVP_DISABLED, HOVERED_PVP_DISABLED)
        self._pvp_enabled = Button(WIDTH // 2 - 200, 350, PVP_ENABLED, HOVERED_PVP_ENABLED)
        self._difficulty_button = Button(WIDTH // 2 - 200, 550, DIFFICULTY, DIFFICULTY)

        # Menu control
        self._in_menu = True
        self._in_options = False

    # Menu Functions
    def main_menu(self):
        # Function that sets up the main menu and runs its game-loop.
        self.window.fill(LIGHT_BLUE)
        self.window.blit(BG_IMAGE, (120, 0))

        while True:
            self.mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        # Transition into the game screen if the player clicks play.
                        if self._play_button.is_mouse_over(self.mouse_pos):
                            if self.board.player_color == 'Red' or self.board.pvp:
                                self.board.player_turn = True
                                self.board.player_color = 'Red'
                            else:
                                self.board.player_turn = False
                                self.board.player_color = 'Yellow'
                            self._in_menu = False
                            self._in_options = False
                            return
                        # Transition to the options' menu if player clicks the options button.
                        elif self._options_button.is_mouse_over(self.mouse_pos):
                            self._in_options = True
                            self._in_menu = False
                            return
                        elif self._exit_button.is_mouse_over(self.mouse_pos):
                            pygame.quit()
                            quit()
            self.draw_menu_buttons()
            pygame.display.update()

    def options_menu(self):
        # Setting up the options menu and its game-loop.
        self.window.fill(LIGHT_BLUE)
        self.window.blit(BG_IMAGE, (120, 0))
        while True:
            self.mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    # Transitioning from the options' menu to the main menu.
                    if event.key == pygame.K_ESCAPE:
                        self._in_options = False
                        self._in_menu = True
                        return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        # Handle button presses.
                        if self._player_color_red.is_mouse_over(self.mouse_pos):
                            if self.board.player_color == 'Red':
                                self.board.player_color = 'Yellow'
                            else:
                                self.board.player_color = 'Red'
                            break
                        if self._pvp_enabled.is_mouse_over(self.mouse_pos):
                            self.board.pvp = not self.board.pvp
                            break

            self.draw_options_buttons(self.board.player_color, self.board.pvp)

            self._difficulty_button.draw(self.window, self.mouse_pos)

            pygame.display.update()

    def draw_menu_buttons(self):
        self._play_button.draw(self.window, self.mouse_pos)
        self._options_button.draw(self.window, self.mouse_pos)
        self._exit_button.draw(self.window, self.mouse_pos)

    def draw_options_buttons(self, player_color: str, pvp: bool):
        if player_color == 'Red':
            self._player_color_red.draw(self.window, self.mouse_pos)
        else:
            self._player_color_yellow.draw(self.window, self.mouse_pos)

        if pvp:
            self._pvp_enabled.draw(self.window, self.mouse_pos)
        else:
            self._pvp_disabled.draw(self.window, self.mouse_pos)

    # Game Functions
    def update_events(self):
        self.mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                # Pressing Escape resets the board and goes to main-menu.
                if event.key == pygame.K_ESCAPE:
                    self.board.reset()
                    self._in_menu = True
                    return
                # Resetting the board when pressing 'r'.
                elif event.key == pygame.K_r:
                    self.board.reset()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.board.game_over:
                        self.board.reset()

                    if self.board.player_turn:
                        self.board.play_move(self.mouse_pos)

    def update(self):
        if not self.board.game_over:
            self.board.check_winner()

        if not self.board.game_over and not self.board.player_turn\
           and not self.board.pvp and not self._in_menu:
            self.computer.generate_move(self.board)

    def render(self):
        self.board.draw_grid(self.window, self.mouse_pos[0])
        pygame.display.update()

    def run(self):
        while True:
            if self._in_options:
                self.options_menu()
            elif self._in_menu:
                self.main_menu()
            else:
                self.update_events()
                self.update()
                self.render()
