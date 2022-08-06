import pygame
import visuals

backing = visuals.Backdrop()
sprites = visuals.Clickable()
lock_nums = 10
# SCREEN SIZES

screen_dimensions = (1100, 600)
screen_width = screen_dimensions[0]
screen_height = screen_dimensions[1]
ratio = screen_dimensions[0] / screen_dimensions[1]
screen = pygame.display.set_mode(screen_dimensions)

# COLORS
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)

# CARD STUFF
SUITS = ['C', 'S', 'H', 'D']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


font = pygame.font.SysFont("Arial", 20)
textfont = pygame.font.SysFont('Comic Sans MS', 35)
game_end = pygame.font.SysFont('dejavusans', 100)
blackjack = pygame.font.SysFont('roboto', 70)


