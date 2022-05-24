from traitlets import HasTraits, Int, Unicode, default, Any



class Button(HasTraits):
    x = Int()
    y = Int()
    highlighted = Any()
    image = Any()
    rect = Any()

    @default('rect')
    def _default_rect(self):
        result = self.image.get_rect()
        result.topleft = (self.x, self.y)


class Play(Button):
    y = int(175)

    @default('x')
    def _default_x(self):
        return WIDTH // 2 - 200


    @default('highlighted')
    def _default_highlighted(self):
        return HOVERED_PLAY
            
    @default('image')
    def _default_highlighted(self):
        return PLAY_BUTTON


class Options(Play):
    """inherits x from play button."""

    y = Int(400)

    @default('highlighted')
    def _default_highlighted(self):
        return HOVERED_OPTIONS
            
    @default('image')
    def _default_highlighted(self):
        return OPTIONS_BUTTON
