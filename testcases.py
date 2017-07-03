import unittest
from Card import Card
from Hand import Hand
from Deck import Deck


class TestCard(unittest.TestCase):
    def test(self):
        kingofclubs = Card('Clubs', 'K')
        nocard = Card('A', 'S')
        self.assertEquals(kingofclubs.rank, 'K')
        self.assertEquals(kingofclubs.suit, 'Clubs')
        self.assertEquals(nocard.suit, None)
        self.assertEquals(nocard.rank, None)
        print 'Test 1 Passed'


class TestHand(unittest.TestCase):
    def test(self):
        hand = Hand()
        kingofclubs = Card('Clubs', 'K')
        hand.add_card(kingofclubs)
        self.assertEquals(hand.get_value(), 10)
        print 'Test 2 Passed'


class TestDeck(unittest.TestCase):
    def test(self):
        newdeck = Deck()
        print newdeck

