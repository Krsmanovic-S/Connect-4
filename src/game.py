from board import *
from AI import *
from button import *

class Game:
    # Constructor
    def __init__(self):
        pygame.init()

        # Window settings
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_icon(WINDOW_ICON)
        pygame.display.set_caption("Connect 4")

        # Variables
        self.mouse_pos = (-1, -1)
        self.board = Board()
        self.computer = AI()
        self.is_player_red = True

        # Buttons
        self.play_button = Button(WIDTH // 2 - 200, 150, PLAY_BUTTON, HOVERED_PLAY)
        self.options_button = Button(WIDTH // 2 - 200, 350, OPTIONS_BUTTON, HOVERED_OPTIONS)
        self.exit_button = Button(WIDTH // 2 - 200, 550, EXIT_BUTTON, HOVERED_EXIT)

        self.player_color_red = Button(WIDTH // 2 - 200, 150, PLAYER_COLOR_RED, HOVERED_COLOR_RED)
        self.player_color_yellow = Button(WIDTH // 2 - 200, 150, PLAYER_COLOR_YELLOW, HOVERED_COLOR_YELLOW)
        self.pvp_disabled = Button(WIDTH // 2 - 200, 350, PVP_DISABLED, HOVERED_PVP_DISABLED)
        self.pvp_enabled = Button(WIDTH // 2 - 200, 350, PVP_ENABLED, HOVERED_PVP_ENABLED)

        # Placeholders (Options Menu)
        self.holder_3 = Button(WIDTH // 2 - 200, 550, PLAYER_COLOR_RED, HOVERED_COLOR_RED)

        # Menu control
        self.in_menu = True
        self.in_options = False

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
                        if self.play_button.is_mouse_over(self.mouse_pos):
                            if self.is_player_red or self.board.pvp:
                                self.board.player_turn = True
                                self.board.player_color = 'Red'
                            else:
                                self.board.player_turn = False
                                self.board.player_color = 'Yellow'
                            self.in_menu = False
                            self.in_options = False
                            return
                        # Transition to the options' menu if player clicks the options button.
                        elif self.options_button.is_mouse_over(self.mouse_pos):
                            self.in_options = True
                            self.in_menu = False
                            return
                        elif self.exit_button.is_mouse_over(self.mouse_pos):
                            pygame.quit()
                            quit()

            self.play_button.draw(self.window, self.mouse_pos)
            self.options_button.draw(self.window, self.mouse_pos)
            self.exit_button.draw(self.window, self.mouse_pos)

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
                        self.in_options = False
                        self.in_menu = True
                        return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        # Handle button presses.
                        if self.player_color_red.is_mouse_over(self.mouse_pos):
                            self.is_player_red = not self.is_player_red
                            break
                        if self.pvp_enabled.is_mouse_over(self.mouse_pos):
                            self.board.pvp = not self.board.pvp
                            break

            if self.is_player_red:
                self.player_color_red.draw(self.window, self.mouse_pos)
            else:
                self.player_color_yellow.draw(self.window, self.mouse_pos)

            if self.board.pvp:
                self.pvp_enabled.draw(self.window, self.mouse_pos)
            else:
                self.pvp_disabled.draw(self.window, self.mouse_pos)

            self.holder_3.draw(self.window, self.mouse_pos)

            pygame.display.update()

    # Game Functions
    def update_events(self):
        self.mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.board.reset()
                    self.in_menu = True
                    return
                # Resetting the board when pressing 'r'
                elif event.key == pygame.K_r:
                    self.board.reset()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.board.game_over:
                        self.board.reset()

                    if self.board.player_turn:
                        self.board.play_move(self.mouse_pos)

    def update(self):
        if self.board.game_over == False:
            self.board.check_winner()

        if not self.board.game_over and not self.board.player_turn\
           and not self.board.pvp:
            self.computer.generate_move(self.board)

    def render(self):
        self.board.draw_grid(self.window, self.mouse_pos[0])
        pygame.display.update()

    def run(self):
        while True:
            if self.in_options:
                self.options_menu()
            elif self.in_menu:
                self.main_menu()
            else:
                self.update_events()
                self.update()
                self.render()
