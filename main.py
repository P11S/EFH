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
        SETTINGS_BUTTON = Button(sprites.menu_to_settings, (0.7*screen_width, .66*screen_height))
        ACHIEVEMENTS_BUTTON = Button(sprites.menu_to_achievements, (0.3 * screen_width, .66 * screen_height))

        for button in [PLAY_BUTTON, SETTINGS_BUTTON, ACHIEVEMENTS_BUTTON]:
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.check_input(menu_mouse_loc):
                    mainroom()
                if SETTINGS_BUTTON.check_input(menu_mouse_loc):
                    settings()
                if ACHIEVEMENTS_BUTTON.check_input(menu_mouse_loc):
                    achievements()

        pygame.display.flip()
        fps_clock.tick(fps)


def mainroom():
    while True:
        # Set Backdrop
        screen.blit(backing.mainroom, (0, 0))
        menu_mouse_loc = pygame.mouse.get_pos()

        TO_MENU_BUTTON = Button(sprites.any_to_menu, (.03 * screen_width, .05 * screen_height))

        for button in [TO_MENU_BUTTON]:
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if TO_MENU_BUTTON.check_input(menu_mouse_loc):
                    main_menu()

        pygame.display.flip()
        fps_clock.tick(fps)


def settings():
    while True:
        # Set Backdrop
        screen.blit(backing.settings, (0, 0))
        menu_mouse_loc = pygame.mouse.get_pos()

        TO_MENU_BUTTON = Button(sprites.any_to_menu, (.03 * screen_width, .05 * screen_height))

        for button in [TO_MENU_BUTTON]:
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if TO_MENU_BUTTON.check_input(menu_mouse_loc):
                    main_menu()

        pygame.display.flip()
        fps_clock.tick(fps)


def achievements():
    while True:
        # Set Backdrop
        screen.blit(backing.achievements, (0, 0))
        menu_mouse_loc = pygame.mouse.get_pos()

        TO_MENU_BUTTON = Button(sprites.any_to_menu, (.03 * screen_width, .05 * screen_height))

        for button in [TO_MENU_BUTTON]:
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if TO_MENU_BUTTON.check_input(menu_mouse_loc):
                    main_menu()

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
