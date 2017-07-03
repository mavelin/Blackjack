from GlobalVar import *
from Card import Card
from Hand import Hand
import random


class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)
        return self.cards

    def deal_card(self):
        poppedcard = self.cards.pop(0)
        return poppedcard

    # def __str__(self):
    #     s = ''
    #     for c in self.cards:
    #         s = s + str(c) + ''
    #     return s


def deal():
    global in_play, player, dealer, deck, message, score, outcome
    if in_play is True:
        message = "Here is the new hand"
        score = -1
        deck = Deck()
        player = Hand()
        dealer = Hand()
        player.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
        player.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
    if in_play is False:
        # starts a new hand
        deck = Deck()
        player = Hand()
        dealer = Hand()
        player.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
        player.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
        message = "New Hand. Hit or Stand?"
    in_play = True
    outcome = ''


def hit():
    global in_play, score, message, outcome
    if in_play is True:
        player.add_card(deck.deal_card())
        message = "Hit or Stand?"
        if player.get_value() > 21:
            in_play = False
            message = 'Player busted! You Lose! Play again?'
            score = -1
            outcome = 'Dealer: ' + str(dealer.get_value()) + "Player: " + str(player.get_value())


def stand():
    global in_play, score, message, outcome
    if in_play is False:
        message = 'The hand is over. Deal again.'
    else:
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
        if dealer.get_value() > 21:
            message = "Dealer busted. You win."
            score += 1
            in_play = False

        elif dealer.get_value() > player.get_value():
            message = 'Dealer wins.'
            score -= 1
            in_play = False

        elif dealer.get_value() == player.get_value():
            message = 'Push'
            in_play = False

        outcome = 'Dealer: ' + str(dealer.get_value()) + "Player: " + str(player.get_value())
