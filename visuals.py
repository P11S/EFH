import pygame
from constants import *

screen_dimensions = (1100, 600)
ratio = screen_dimensions[0] / screen_dimensions[1]


class Backdrop:
    """
    This class will house every 'Background' style image that is used in the game
    """

    def __init__(self):
        # Backdrop for the main menu
        menu_png = pygame.image.load('visuals/Backdrops/EFH_menu.png')
        menu_png = pygame.transform.scale(menu_png, screen_dimensions)
        self.menu = menu_png
        # Backdrop for the main game room
        mainroom_png = pygame.image.load('visuals/Backdrops/EFH_mainroom.png')
        mainroom_png = pygame.transform.scale(mainroom_png, screen_dimensions)
        self.mainroom = mainroom_png
        # Backdrop for the settings screen
        settings_png = pygame.image.load('visuals/Backdrops/EFH_settings.png')
        settings_png = pygame.transform.scale(settings_png, screen_dimensions)
        self.settings = settings_png
        # Backdrop for the achievements screen
        achievements_png = pygame.image.load('visuals/Backdrops/EFH_achievements.png')
        achievements_png = pygame.transform.scale(achievements_png, screen_dimensions)
        self.achievements = achievements_png
        # Backdrop for the stairwell
        stairs_png = pygame.image.load('visuals/Backdrops/EFH_stairs.png')
        stairs_png = pygame.transform.scale(stairs_png, screen_dimensions)
        self.stairs = stairs_png
        # Backdrop for the task rooms
        task1_png = pygame.image.load('visuals/Backdrops/EFH_task1.png')
        task1_png = pygame.transform.scale(task1_png, screen_dimensions)
        self.task1 = task1_png


class Clickable:
    """
    This class will house every 'sprite' that one can click throughout the game
    """

    def __init__(self):
        # Sprite for the button with path MENU -> MAIN GAME
        menu_to_mainscreen_png = pygame.image.load('visuals/Sprites/menu_to_main.png')
        menu_to_mainscreen_png = pygame.transform.scale(menu_to_mainscreen_png,
                                                        tuple(i * 0.15 for i in screen_dimensions))
        self.menu_to_mainscreen = menu_to_mainscreen_png
        # Sprite for button with path ANYWHERE -> MENU
        any_to_menu_png = pygame.image.load('visuals/Sprites/exit_to_home.png')
        any_to_menu_png = pygame.transform.scale(any_to_menu_png,
                                                 (screen_dimensions[0] * .05, screen_dimensions[1] * .05 * ratio))
        self.any_to_menu = any_to_menu_png
        # Sprite for button with path MENU -> SETTINGS
        menu_to_settings_png = pygame.image.load('visuals/Sprites/to_settings.png')
        menu_to_settings_png = pygame.transform.scale(menu_to_settings_png,
                                                      tuple(i * 0.15 for i in screen_dimensions))
        self.menu_to_settings = menu_to_settings_png
        # Sprite for button with path MAINSCREEN -> TASK1
        task1_png = pygame.image.load('visuals/Sprites/task1.png')
        task1_png = pygame.transform.scale(task1_png,
                                           tuple(i * 0.15 for i in screen_dimensions))
        self.task1 = task1_png
        # Sprite for the button with path MENU -> ACHIEVEMENTS
        menu_to_achievements_png = pygame.image.load('visuals/Sprites/to_achievements.png')
        menu_to_achievements_png = pygame.transform.scale(menu_to_achievements_png,
                                                          tuple(i * 0.15 for i in screen_dimensions))
        self.menu_to_achievements = menu_to_achievements_png
        # Sprite for the button with path TASK -> MAIN GAME
        task_to_main_png = pygame.image.load('visuals/Sprites/task_to_main.png')
        task_to_main_png = pygame.transform.scale(task_to_main_png, (screen_dimensions[0] * .05,
                                                                     screen_dimensions[1] * .05 * ratio))
        self.task_to_main = task_to_main_png
        # Sprite for the button DEAL
        deal_png = pygame.image.load('visuals/Sprites/deal.png')
        deal_png = pygame.transform.scale(deal_png,
                                                          tuple(i * 0.15 for i in screen_dimensions))
        self.deal = deal_png
        # Sprite for the button HIT
        hit_png = pygame.image.load('visuals/Sprites/hit.png')
        hit_png = pygame.transform.scale(hit_png,
                                          tuple(i * 0.15 for i in screen_dimensions))
        self.hit = hit_png
        # Sprite for the button STAND
        stand_png = pygame.image.load('visuals/Sprites/stand.png')
        stand_png = pygame.transform.scale(stand_png,
                                          tuple(i * 0.15 for i in screen_dimensions))
        self.stand = stand_png
