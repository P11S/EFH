import pygame

# SCREEN SIZES
screen_dimensions = (1100, 600)
screen_width = screen_dimensions[0]
screen_height = screen_dimensions[1]
ratio = screen_dimensions[0] / screen_dimensions[1]

# COLORS
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)

# CARD STUFF
SUITS = ['C', 'S', 'H', 'D']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']