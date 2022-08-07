import random
from constants import *
import time
import sys


# https://medium.com/nerd-for-tech/creating-blackjack-game-with-python-80a3b87b1995

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def end_text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def game_texts(text, loc):
    TextSurf, TextRect = text_objects(text, textfont)
    TextRect.center = loc
    screen.blit(TextSurf, TextRect)
    pygame.display.update()


def game_finish(text, loc, color):
    TextSurf, TextRect = end_text_objects(text, game_end, color)
    TextRect.center = loc
    screen.blit(TextSurf, TextRect)
    pygame.display.update()


def black_jack(text, loc , color):
    TextSurf, TextRect = end_text_objects(text, blackjack, color)
    TextRect.center = loc
    screen.blit(TextSurf, TextRect)
    pygame.display.update()


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for value in RANKS:
            for suit in SUITS:
                self.cards.append((value, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop()


class Hand(Deck):
    def __init__(self):
        self.cards = []
        self.card_img = []
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)

    def calc_hand(self):
        first_card_index = [a_card[0] for a_card in self.cards]
        non_aces = [c for c in first_card_index if c != 'A']
        aces = [c for c in first_card_index if c == 'A']

        for card in non_aces:
            if card in 'JQK':
                self.value += 10
            else:
                self.value += int(card)

        for card in aces:
            if self.value <= 10:
                self.value += 11
            else:
                self.value += 1

    def display_cards(self):
        for card in self.cards:
            cards = "".join((card[0], card[1]))
            if cards not in self.card_img:
                self.card_img.append(cards)


class Play:
    def __init__(self):
        self.deck = Deck()
        self.dealer = Hand()
        self.player = Hand()
        self.deck.shuffle()
        self.just_won = False
        self.just_tied = False
        self.just_blackjack = False
        self.loss_differential = 0

    def blackjack(self):
        self.dealer.calc_hand()
        self.player.calc_hand()
        print(self.player.value)
        show_dealer_card = pygame.image.load('img/' + self.dealer.card_img[1] + '.png').convert()
        show_dealer_card = pygame.transform.scale(show_dealer_card,
                                                  tuple(i * 0.15 for i in screen_dimensions[::-1]))

        if self.player.value == 21 and self.dealer.value == 21:
            screen.blit(show_dealer_card, (screen_width * .66, screen_height * .25))
            black_jack("We tie with BlackJack", (screen_width//2, screen_height//2), black)
            time.sleep(4)
            self.just_won = False
            self.just_tied = True
            self.just_blackjack = True
            self.play_or_exit()
            self.loss_differential = 0
        elif self.player.value == 21:
            screen.blit(show_dealer_card, (screen_width * .66, screen_height * .25))
            black_jack("You win with BlackJack", (screen_width//2, screen_height//2), black)
            self.just_won = True
            self.just_tied = False
            self.just_blackjack = True
            time.sleep(4)
            self.loss_differential = 0
            self.play_or_exit()
        elif self.dealer.value == 21:
            screen.blit(show_dealer_card, (screen_width * .66, screen_height * .25))
            black_jack("I win with BlackJack", (screen_width//2, screen_height//2), black)
            time.sleep(4)
            self.just_won = False
            self.just_tied = False
            self.just_blackjack = True
            self.loss_differential = (self.dealer.value - self.player.value) % code_nums
            self.play_or_exit()

        self.player.value = 0
        self.dealer.value = 0

    def deal(self):
        for i in range(2):
            self.dealer.add_card(self.deck.deal())
            self.player.add_card(self.deck.deal())
        self.dealer.display_cards()
        self.player.display_cards()
        self.player_card = 1
        dealer_card = pygame.image.load('img/' + self.dealer.card_img[0] + '.png')
        dealer_card = pygame.transform.scale(dealer_card,
                                             tuple(i * 0.15 for i in screen_dimensions[::-1]))
        dealer_card_2 = pygame.image.load('img/back.png')
        dealer_card_2 = pygame.transform.scale(dealer_card_2,
                                               tuple(i * 0.15 for i in screen_dimensions[::-1]))
        player_card = pygame.image.load('img/' + self.player.card_img[0] + '.png')
        player_card = pygame.transform.scale(player_card,
                                             tuple(i * 0.15 for i in screen_dimensions[::-1]))
        player_card_2 = pygame.image.load('img/' + self.player.card_img[1] + '.png')
        player_card_2 = pygame.transform.scale(player_card_2,
                                               tuple(i * 0.15 for i in screen_dimensions[::-1]))

        screen.blit(dealer_card, (screen_width * .33, screen_height * .25))
        screen.blit(dealer_card_2, (screen_width * .66, screen_height * .25))

        screen.blit(player_card, (screen_width * .25, screen_height * .75))
        screen.blit(player_card_2, (screen_width * .5, screen_height * .75))
        self.blackjack()

    def hit(self):
        self.player.add_card(self.deck.deal())
        self.player_card += 1
        # self.blackjack()

        if self.player_card == 2:

            self.player.calc_hand()
            self.player.display_cards()
            player_card_3 = pygame.image.load('img/' + self.player.card_img[2] + '.png')
            player_card_3 = pygame.transform.scale(player_card_3,
                                                   tuple(i * 0.15 for i in screen_dimensions[::-1]))
            screen.blit(player_card_3, (screen_width * .75, screen_height * .75))

            print('hello')
            print(self.player.value)
            self.player.value = 0
            self.blackjack()

        if self.player_card == 3:
            self.player.calc_hand()
            self.player.display_cards()
            player_card_4 = pygame.image.load('img/' + self.player.card_img[3] + '.png')
            player_card_4 = pygame.transform.scale(player_card_4,
                                                   tuple(i * 0.15 for i in screen_dimensions[::-1]))
            screen.blit(player_card_4, (screen_width * .9, screen_height * .75))
            self.player.value = 0
            self.blackjack()
        self.player.calc_hand()
        if self.player.value > 21:
            game_finish("You Busted. I win", (screen_width//2, screen_height//2), black)
            time.sleep(4)
            self.just_won = False
            self.just_tied = False
            self.loss_differential = (self.player.value - 21) % code_nums
            self.play_or_exit()

        # self.player.value = 0

        if self.player_card > 4:
            self.play_or_exit()
            print('4')

    def stand(self):
        show_dealer_card = pygame.image.load('img/' + self.dealer.card_img[1] + '.png')
        show_dealer_card = pygame.transform.scale(show_dealer_card,
                                                  tuple(i * 0.15 for i in screen_dimensions[::-1]))
        screen.blit(show_dealer_card, (screen_width * .66, screen_height * .25))
        # self.blackjack()
        self.dealer.calc_hand()
        self.player.calc_hand()

        if self.player.value > self.dealer.value:
            game_finish("You Won!", (screen_width//2, screen_height//2), black)
            time.sleep(4)
            self.just_won = True
            self.just_tied = False
            self.play_or_exit()
        elif self.player.value < self.dealer.value:
            game_finish("I Won!", (screen_width//2, screen_height//2), black)
            self.loss_differential = (self.dealer.value - self.player.value) % code_nums
            self.just_won = False
            self.just_tied = False
            time.sleep(4)
            self.play_or_exit()
        else:
            game_finish("We tie", (screen_width//2, screen_height//2), black)
            self.just_won = False
            self.just_tied = True
            time.sleep(4)
            self.play_or_exit()

    def exit(self):
        sys.exit()

    def play_or_exit(self):
        # game_texts("Play again press Deal!", (screen_width//2, screen_height//2))

        self.player.value = 0
        self.dealer.value = 0
        self.deck = Deck()
        self.deck.shuffle()
        self.dealer = Hand()
        self.player = Hand()
        self.deck.shuffle()
        screen.fill(white)
        screen.blit(backing.task1, (0, 0))
        pygame.display.update()
