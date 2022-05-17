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

        # Buttons
        self.play_button = Button(WIDTH // 2 - 200, 150, PLAY_BUTTON, HOVERED_PLAY)
        self.options_button = Button(WIDTH // 2 - 200, 350, OPTIONS_BUTTON, HOVERED_OPTIONS)
        self.exit_button = Button(WIDTH // 2 - 200, 550, EXIT_BUTTON, HOVERED_EXIT)

        # Placeholders (Options Menu)
        self.holder_1 = Button(15, 50, PLAY_BUTTON, HOVERED_PLAY)
        self.holder_2 = Button(15, 275, PLAY_BUTTON, HOVERED_PLAY)
        self.holder_3 = Button(15, 500, PLAY_BUTTON, HOVERED_PLAY)
        self.back_button = Button(425, 500, BACK_BUTTON, HOVERED_BACK)

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
                        if self.play_button.rect.collidepoint(self.mouse_pos):
                            self.in_menu = False
                            self.in_options = False
                            return
                        # Transition to the options' menu if player clicks the options button.
                        elif self.options_button.rect.collidepoint(self.mouse_pos):
                            self.in_options = True
                            self.in_menu = False
                            return
                        elif self.exit_button.rect.collidepoint(self.mouse_pos):
                            pygame.quit()
                            quit()

            self.play_button.draw(self.window, self.mouse_pos)
            self.options_button.draw(self.window, self.mouse_pos)
            self.exit_button.draw(self.window, self.mouse_pos)

            pygame.display.update()

    def options_menu(self):
        # Setting up the options menu and its game-loop.
        self.window.fill(LIGHT_BLUE)
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
                        if self.back_button.rect.collidepoint(self.mouse_pos):
                            self.in_menu = True
                            self.in_options = False
                            return

            self.holder_1.draw(self.window, self.mouse_pos)
            self.holder_2.draw(self.window, self.mouse_pos)
            self.holder_3.draw(self.window, self.mouse_pos)
            self.back_button.draw(self.window, self.mouse_pos)

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.board.game_over:
                        self.board.reset()

                    if self.board.player_turn:
                        self.board.play_move(self.mouse_pos)

    def update(self):
        if self.board.game_over == False:
            self.board.check_winner()

        if not self.board.game_over and not self.board.player_turn:
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
