# General setup / imports

import pygame

pygame.init()
from button import *
from blackjack_deck import *
from lockbox import *
from constants import *
# Game screen


# backing = visuals.Backdrop()
# sprites = visuals.Clickable()
fps = 30
fps_clock = pygame.time.Clock()

box_code = LockBox(code_nums)



def main_menu():
    while True:
        # Set backdrop
        screen.blit(backing.menu, (0, 0))
        menu_mouse_loc = pygame.mouse.get_pos()

        # All clickables (buttons) should be placed here
        PLAY_BUTTON = Button(sprites.menu_to_mainscreen, (0.5 * screen_width, .66 * screen_height))
        SETTINGS_BUTTON = Button(sprites.menu_to_settings, (0.7 * screen_width, .66 * screen_height))
        ACHIEVEMENTS_BUTTON = Button(sprites.menu_to_achievements, (0.3 * screen_width, .66 * screen_height))

        for button in [PLAY_BUTTON, SETTINGS_BUTTON, ACHIEVEMENTS_BUTTON]:
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.check_input(menu_mouse_loc):
                    mainroom(JUST_LAUNCHED)
                if SETTINGS_BUTTON.check_input(menu_mouse_loc):
                    settings()
                if ACHIEVEMENTS_BUTTON.check_input(menu_mouse_loc):
                    achievements()

        pygame.display.flip()
        fps_clock.tick(fps)


def mainroom(first_open):
    while True:
        # Set Backdrop
        screen.blit(backing.mainroom, (0, 0))
        menu_mouse_loc = pygame.mouse.get_pos()

        TO_MENU_BUTTON = Button(sprites.any_to_menu, (.03 * screen_width, .05 * screen_height))
        TASK1_BUTTON = Button(sprites.task1, (0.5 * screen_width, .66 * screen_height))

        for button in [TO_MENU_BUTTON, TASK1_BUTTON]:
            button.update(screen)

        # Intro Dialogue
        if first_open:
            # NEW TEXT BUTTON MENU
            first_open = False
            for x in intro_dialogue:

                game_finish(x[0], (screen_width // 2, screen_height // 2), black)
                time.sleep(x[1])
                screen.blit(backing.mainroom, (0, 0))
                TO_MENU_BUTTON = Button(sprites.any_to_menu, (.03 * screen_width, .05 * screen_height))
                TASK1_BUTTON = Button(sprites.task1, (0.5 * screen_width, .66 * screen_height))
                for button in [TO_MENU_BUTTON, TASK1_BUTTON]:
                    button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if TO_MENU_BUTTON.check_input(menu_mouse_loc):
                    main_menu()
                if TASK1_BUTTON.check_input(menu_mouse_loc):
                    task1()

        pygame.display.flip()
        fps_clock.tick(fps)


def task1():
    screen.blit(backing.task1, (0, 0))
    play_blackjack = Play()
    just_dealt = False
    can_hit = False


    while True:
        # menu specific code
        menu_mouse_loc = pygame.mouse.get_pos()

        TO_MAINROOM_BUTTON = Button(sprites.task_to_main, (.03 * screen_width, .05 * screen_height))
        DEAL_BUTTON = Button(sprites.deal, (0.1 * screen_width, .25 * screen_height))
        HIT_BUTTON = Button(sprites.hit, (0.1 * screen_width, .5 * screen_height))
        STAND_BUTTON = Button(sprites.stand, (0.1 * screen_width, .75 * screen_height))
        LOCK_BUTTON = Button(sprites.lock, (.9 * screen_width, .5 * screen_height))

        for button in [TO_MAINROOM_BUTTON, DEAL_BUTTON, HIT_BUTTON, STAND_BUTTON, LOCK_BUTTON]:
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if TO_MAINROOM_BUTTON.check_input(menu_mouse_loc):
                    mainroom(first_open=False)
                if DEAL_BUTTON.check_input(menu_mouse_loc) and len(play_blackjack.player.card_img) == 0:
                    play_blackjack.deal()
                    just_dealt = True
                    can_hit = True

                    if not play_blackjack.just_won and not play_blackjack.just_tied and play_blackjack.loss_differential != 0:
                         try:
                            box_code.row1_keys[play_blackjack.loss_differential - 1] = abs(
                                box_code.row1_keys[play_blackjack.loss_differential - 1] - 1)
                            box_code.row2_keys[play_blackjack.loss_differential - 1] = abs(
                                 box_code.row2_keys[play_blackjack.loss_differential - 1] - 1)
                            print('Loss differential: ' +str(play_blackjack.loss_differential))
                         except:
                             pass
                if HIT_BUTTON.check_input(menu_mouse_loc) and can_hit:

                    try:
                        play_blackjack.hit()
                        just_dealt = False
                        can_hit = True
                    except:
                        pass
                if STAND_BUTTON.check_input(menu_mouse_loc):
                    just_dealt = False
                    can_hit = False
                    try:
                        play_blackjack.stand()
                    except:
                        pass
                if LOCK_BUTTON.check_input(menu_mouse_loc):
                    just_dealt = False
                    if play_blackjack.just_won:
                        print(box_code.row1_keys)
                        play_blackjack.just_won = False
                        lockbox()
                    else:
                        pass

        pygame.display.flip()
        fps_clock.tick(fps)


def lockbox():
    box_code.code_reached = 0
    while True:
        # Set Backdrop
        screen.blit(backing.lockbox, (0, 0))
        menu_mouse_loc = pygame.mouse.get_pos()

        TO_TABLE_BUTTON = Button(sprites.box_to_table, (.03 * screen_width, .05 * screen_height))
        for x in range(0, box_code.code_reached + 1):
            try:
                box_code.row1_buttons[x].update(screen)
            except:
                pass

        for y in range(0, box_code.code_reached + 1):
            try:
                box_code.row2_buttons[y].update(screen)
            except:
                pass

        for button in [TO_TABLE_BUTTON]:
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if TO_TABLE_BUTTON.check_input(menu_mouse_loc):
                    task1()
                try:
                    if box_code.row1_buttons[box_code.code_reached].check_input(menu_mouse_loc):
                        if box_code.row1_keys[box_code.code_reached] == 0:
                            task1()
                        else:
                            box_code.code_reached += 1
                    if box_code.row2_buttons[box_code.code_reached].check_input(menu_mouse_loc):
                        if box_code.row2_keys[box_code.code_reached] == 0:
                            task1()
                        else:
                            box_code.code_reached += 1
                except:
                    print('game over!')
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
