from Hand import Hand
from Deck import Deck
from GlobalVar import *


class Player:
    def __init__(self, name='You', chips=STARTING_CHIPS):
        self.name = name
        self.chips = chips
        self.bet = 0
        self.hand = None
        self.stand = False
        self.wins = 0
        self.pushes = 0
        self.losses = 0

    def __str__(self):
        return self.name

    def win(self, winnings):
        print 'You win %d chip(s).' % winnings
        self.chips += winnings
        self.wins += 1

    def lose(self, loss):
        print 'You lost %d chip(s).' % loss
        self.chips -= loss
        self.wins += 1

    def push(self, bet):
        print 'Push.'
        self.pushes += 1

    def hit(self, card):
        self.hand.add_card(card)

    def is_bust(self,):
        if self.hand.get_value() > 21:
            return True
