# General setup / imports
import sys
import pygame
pygame.init()
import visuals
from button import *
from colors import *


# Game screen
screen_dimensions = (1100, 600)
screen_width = screen_dimensions[0]
screen_height = screen_dimensions[1]
screen = pygame.display.set_mode(screen_dimensions)
backing = visuals.Backdrop()
sprites = visuals.Clickable()
fps = 30
fps_clock = pygame.time.Clock()


def main_menu():
    while True:
        # Set backdrop
        screen.blit(backing.menu, (0, 0))

        menu_mouse_loc = pygame.mouse.get_pos()

        # All clickables (buttons) should be placed here
        PLAY_BUTTON = Button(sprites.menu_to_mainscreen, (0.5*screen_width, .66*screen_height))

        for button in [PLAY_BUTTON]:
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.check_input(menu_mouse_loc):
                    mainroom()

        pygame.display.flip()
        fps_clock.tick(fps)


def mainroom():
    while True:
        # menu specific code
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(backing.mainroom, (0, 0))
        pygame.display.flip()
        fps_clock.tick(fps)


def tasks():
    while True:
        # menu specific code
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(backing.tasks, (0, 0))
        pygame.display.flip()
        fps_clock.tick(fps)


def stairs():
    while True:
        # menu specific code
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(backing.stairs, (0, 0))
        pygame.display.flip()
        fps_clock.tick(fps)


main_menu()
