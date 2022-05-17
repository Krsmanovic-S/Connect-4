from board import *
from AI import *
from button import *

class Game:
    def __init__(self):
        # Variables
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.mouse_pos = (-1, -1)
        self.board = Board()
        self.computer = AI()

        # Buttons
        self.play_button = Button(170, 25, PLAY_BUTTON, HOVERED_PLAY)
        self.options_button = Button(170, 225, OPTIONS_BUTTON, HOVERED_OPTIONS)
        self.exit_button = Button(170, 425, EXIT_BUTTON, HOVERED_EXIT)

        # Menu control
        self.in_menu = True

    # Function that sets up the main menu and runs its game-loop.
    def main_menu(self):
        self.window.fill((202, 228, 241))
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
                            return
                        # Transition to the options' menu if player clicks the options button.
                        elif self.options_button.rect.collidepoint(self.mouse_pos):
                            pass
                        elif self.exit_button.rect.collidepoint(self.mouse_pos):
                            pygame.quit()
                            quit()

            self.play_button.draw(self.window, self.mouse_pos)
            self.options_button.draw(self.window, self.mouse_pos)
            self.exit_button.draw(self.window, self.mouse_pos)

            pygame.display.update()

    # Setting up the options menu and its game-loop.
    def options_menu(self):
        pass

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
        pygame.display.set_caption("Connect 4")

        self.board.draw_grid(self.window, self.mouse_pos[0])

        pygame.display.update()

    def run(self):
        while True:
            if self.in_menu:
                self.main_menu()
            else:
                self.update_events()
                self.update()
                self.render()
