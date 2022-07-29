import pygame
screen_dimensions = (1100, 600)
ratio = screen_dimensions[0]/screen_dimensions[1]


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
        # Backdrop for the stairwell
        stairs_png = pygame.image.load('visuals/Backdrops/EFH_stairs.png')
        stairs_png = pygame.transform.scale(stairs_png, screen_dimensions)
        self.stairs = stairs_png
        # Backdrop for the task rooms
        tasks_png = pygame.image.load('visuals/Backdrops/EFH_tasks.png')
        tasks_png = pygame.transform.scale(tasks_png, screen_dimensions)
        self.tasks = tasks_png


class Clickable:
    """
    This class will house every 'sprite' that one can click throughout the game
    """
    def __init__(self):
        # Sprite for the button with path MENU -> MAIN GAME
        menu_to_mainscreen_png = pygame.image.load('visuals/Sprites/menu_to_main.png')
        menu_to_mainscreen_png = pygame.transform.scale(menu_to_mainscreen_png, tuple(i * 0.15 for i in screen_dimensions))
        self.menu_to_mainscreen = menu_to_mainscreen_png
        # Sprite for button with path ANYWHERE -> MENU
        any_to_menu_png = pygame.image.load('visuals/Sprites/exit_to_home.png')
        any_to_menu_png = pygame.transform.scale(any_to_menu_png, (screen_dimensions[0]*.05, screen_dimensions[1] * .05 * ratio))
        self.any_to_menu = any_to_menu_png



