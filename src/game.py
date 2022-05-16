from board import *
from AI import *

class Game:
    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.board = Board()
        self.computer = AI()
        self.mouse_pos = 0

    def update_events(self):
        self.mouse_pos = pygame.mouse.get_pos()
        # EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.board.game_over:
                        self.board.reset()
                    if self.board.player_turn and not self.board.game_over:
                        self.board.play_move(self.mouse_pos)

    def update(self):
        if self.board.game_over == False:
            self.board.check_winner()

        if not self.board.game_over and not self.board.player_turn:
            self.computer.generate_move(self.board)

    def render(self):
        pygame.display.set_caption("Connect 4")

        self.board.draw_grid(self.window)

        pygame.display.update()

    def run(self):
        while True:
            self.update_events()
            self.update()
            self.render()
