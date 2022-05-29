from traitlets import HasTraits, Int, default, Any
from constants import *


class Button(HasTraits):
    x = Int()
    y = Int()
    highlighted = Any()
    image = Any()
    rect = Any()

    @default('x')
    def _default_x(self):
        return WIDTH // 2 - 200

    @default('rect')
    def _default_rect(self):
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        return self.rect

    # Functions
    def draw_button(self, window: pygame.display, mouse: tuple):
        if self.rect.collidepoint(mouse[0] - 5, mouse[1] - 5):
            window.blit(self.highlighted, (self.rect.x, self.rect.y))
        else:
            window.blit(self.image, (self.rect.x, self.rect.y))

    def is_mouse_over(self, mouse_pos: tuple):
        if self.rect.collidepoint(mouse_pos):
            return True
        else:
            return False

    def draw_changing_button(self, window, mouse, button, check: bool):
        # This function is used for buttons which have multiple images
        # representing them, here we can decide which one to show.
        if not check:
            self.draw_button(window, mouse)
        else:
            button.draw_button(window, mouse)


# Git/LinkedIn Buttons
class Git(Button):
    x = int(30)
    y = int(700)

    @default('image')
    def _default_image(self):
        return GIT_ICON

    @default('highlighted')
    def _default_highlighted(self):
        return HOVERED_GIT


class LinkedIn(Git):
    x = int(720)

    @default('image')
    def _default_image(self):
        return LINKEDIN_ICON

    @default('highlighted')
    def _default_highlighted(self):
        return HOVERED_LINKEDIN


# Main Menu Buttons
class Play(Button):
    y = int(175)

    @default('x')
    def _default_x(self):
        return WIDTH // 2 - 200

    @default('image')
    def _default_image(self):
        return PLAY_BUTTON

    @default('highlighted')
    def _default_highlighted(self):
        return HOVERED_PLAY


class Options(Play):
    y = int(400)

    @default('image')
    def _default_image(self):
        return OPTIONS_BUTTON

    @default('highlighted')
    def _default_highlighted(self):
        return HOVERED_OPTIONS


class Exit(Play):
    y = int(625)

    @default('image')
    def _default_image(self):
        return EXIT_BUTTON

    @default('highlighted')
    def _default_highlighted(self):
        return HOVERED_EXIT


# Options Menu Buttons
class PlayerRed(Button):
    y = int(175)

    @default('image')
    def _default_image(self):
        return PLAYER_COLOR_RED

    @default('highlighted')
    def _default_highlighted(self):
        return HOVERED_COLOR_RED


class PlayerYellow(PlayerRed):

    @default('image')
    def _default_image(self):
        return PLAYER_COLOR_YELLOW

    @default('highlighted')
    def _default_highlighted(self):
        return HOVERED_COLOR_YELLOW


class PvpEnabled(Button):
    y = int(400)

    @default('image')
    def _default_image(self):
        return PVP_ENABLED

    @default('highlighted')
    def _default_highlighted(self):
        return HOVERED_PVP_ENABLED


class PvpDisabled(PvpEnabled):

    @default('image')
    def _default_image(self):
        return PVP_DISABLED

    @default('highlighted')
    def _default_highlighted(self):
        return HOVERED_PVP_DISABLED


class EasyDifficulty(Button):
    y = int(625)

    @default('image')
    def _default_image(self):
        return EASY_DIFFICULTY

    @default('highlighted')
    def _default_highlighted(self):
        return HOVERED_EASY_DIFFICULTY


class MediumDifficulty(EasyDifficulty):

    @default('image')
    def _default_image(self):
        return MEDIUM_DIFFICULTY

    @default('highlighted')
    def _default_highlighted(self):
        return HOVERED_MEDIUM_DIFFICULTY


class HardDifficulty(EasyDifficulty):

    @default('image')
    def _default_image(self):
        return HARD_DIFFICULTY

    @default('highlighted')
    def _default_highlighted(self):
        return HOVERED_HARD_DIFFICULTY


class BackArrow(Button):
    x = int(720)
    y = int(700)

    @default('image')
    def _default_image(self):
        return BACK_ARROW

    @default('highlighted')
    def _default_highlighted(self):
        return HOVERED_BACK_ARROW
