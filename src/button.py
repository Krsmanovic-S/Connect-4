
class Button:
    # Constructor
    def __init__(self, x, y, image, highlighted):
        self.image = image
        self.highlighted = highlighted
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    # Functions
    def draw(self, window, mouse):
        if self.rect.collidepoint(mouse[0], mouse[1]):
            window.blit(self.highlighted, (self.rect.x, self.rect.y))
        else:
            window.blit(self.image, (self.rect.x, self.rect.y))