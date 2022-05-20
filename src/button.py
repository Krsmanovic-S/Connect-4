
class Button:
    def __init__(self, x, y, image, highlighted):
        self.image = image
        self.highlighted = highlighted
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    # Functions
    def draw(self, window, mouse):
        if self.rect.collidepoint(mouse[0] - 5, mouse[1] - 5):
            window.blit(self.highlighted, (self.rect.x, self.rect.y))
        else:
            window.blit(self.image, (self.rect.x, self.rect.y))

    def is_mouse_over(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True
        else:
            return False

    def draw_changing_button(self, window, mouse, button, check: bool):
        if not check:
            self.draw(window, mouse)
        else:
            button.draw(window, mouse)
