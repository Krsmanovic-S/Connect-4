import pygame

# WINDOW PROPERTIES
WIDTH = 840
HEIGHT = 720

#--------------------------------------------#
#                   IMAGES                   #
#--------------------------------------------#
WINDOW_ICON = pygame.image.load('images/icons/window_logo.png')
BG_IMAGE = pygame.image.load('images/icons/logo.png')

PLAY_BUTTON = pygame.image.load('images/Buttons/play_button.png')
OPTIONS_BUTTON = pygame.image.load('images/Buttons/options_button.png')
EXIT_BUTTON = pygame.image.load('images/buttons/exit_button.png')

PLAYER_COLOR_RED = pygame.image.load('images/buttons/player_red_button.png')
PLAYER_COLOR_YELLOW = pygame.image.load('images/buttons/player_yellow_button.png')
PVP_ENABLED = pygame.image.load('images/buttons/pvp_enabled_button.png')
PVP_DISABLED = pygame.image.load('images/buttons/pvp_disabled_button.png')

HOVERED_PLAY = pygame.image.load('images/buttons/hovered_play.png')
HOVERED_OPTIONS = pygame.image.load('images/buttons/hovered_options.png')
HOVERED_EXIT = pygame.image.load('images/buttons/hovered_exit.png')

HOVERED_COLOR_RED = pygame.image.load('images/buttons/hovered_player_red.png')
HOVERED_COLOR_YELLOW = pygame.image.load('images/buttons/hovered_player_yellow.png')
HOVERED_PVP_ENABLED = pygame.image.load('images/buttons/hovered_pvp_enabled.png')
HOVERED_PVP_DISABLED = pygame.image.load('images/buttons/hovered_pvp_disabled.png')

#--------------------------------------------#
#                   COLORS                   #
#--------------------------------------------#
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (75, 75, 75)
HIGHLIGHTED = (105, 105, 105)
LIGHT_BLUE = (202, 228, 241)

YELLOW = (255,255,0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)