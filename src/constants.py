import pygame
pygame.init()

# WINDOW PROPERTIES
WIDTH = 840
HEIGHT = 840

# URLS
GIT_URL = 'https://github.com/Krsmanovic-S/'
LINKEDIN_URL = 'https://www.linkedin.com/in/stefan-krsmanovic-7698a4235/'

# -------------------------------------------#
#                   IMAGES                   #
# -------------------------------------------#
WINDOW_ICON = pygame.image.load('images/icons/window_logo.png')
BG_IMAGE = pygame.image.load('images/icons/logo.png')
GIT_ICON = pygame.image.load('images/buttons/git_button.png')
LINKEDIN_ICON = pygame.image.load('images/buttons/linkedin_button.png')
BACK_ARROW = pygame.image.load('images/icons/back_arrow.png')

PLAY_BUTTON = pygame.image.load('images/Buttons/play_button.png')
OPTIONS_BUTTON = pygame.image.load('images/Buttons/options_button.png')
EXIT_BUTTON = pygame.image.load('images/buttons/exit_button.png')

PLAYER_COLOR_RED = pygame.image.load('images/buttons/player_red_button.png')
PLAYER_COLOR_YELLOW = pygame.image.load('images/buttons/player_yellow_button.png')
PVP_ENABLED = pygame.image.load('images/buttons/pvp_enabled_button.png')
PVP_DISABLED = pygame.image.load('images/buttons/pvp_disabled_button.png')
EASY_DIFFICULTY = pygame.image.load('images/buttons/easy_difficulty.png')
MEDIUM_DIFFICULTY = pygame.image.load('images/buttons/medium_difficulty.png')
HARD_DIFFICULTY = pygame.image.load('images/buttons/hard_difficulty.png')

HOVERED_PLAY = pygame.image.load('images/buttons/hovered_play.png')
HOVERED_OPTIONS = pygame.image.load('images/buttons/hovered_options.png')
HOVERED_EXIT = pygame.image.load('images/buttons/hovered_exit.png')
HOVERED_GIT = pygame.image.load('images/buttons/hovered_git.png')
HOVERED_LINKEDIN = pygame.image.load('images/buttons/hovered_linkedin.png')
HOVERED_BACK_ARROW = pygame.image.load('images/icons/hovered_back_arrow.png')

HOVERED_COLOR_RED = pygame.image.load('images/buttons/hovered_player_red.png')
HOVERED_COLOR_YELLOW = pygame.image.load('images/buttons/hovered_player_yellow.png')
HOVERED_PVP_ENABLED = pygame.image.load('images/buttons/hovered_pvp_enabled.png')
HOVERED_PVP_DISABLED = pygame.image.load('images/buttons/hovered_pvp_disabled.png')
HOVERED_EASY_DIFFICULTY = pygame.image.load('images/buttons/hovered_easy_difficulty.png')
HOVERED_MEDIUM_DIFFICULTY = pygame.image.load('images/buttons/hovered_medium_difficulty.png')
HOVERED_HARD_DIFFICULTY = pygame.image.load('images/buttons/hovered_hard_difficulty.png')

# -------------------------------------------#
#                   COLORS                   #
# -------------------------------------------#
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TABLE_BLUE = (31, 111, 215)
HIGHLIGHTED = (61, 138, 239)
LIGHT_BLUE = (202, 228, 241)

YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
