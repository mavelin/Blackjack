from Player import *


class Game:
    def __init__(self):
        self.dealer = Player(name='Dealer')
        self.player = Player()
        self.deck = Deck()

    def get_player_bet(self):
        while True:
            bet_input = raw_input('Enter bet for this hand (or exit to quite): ').strip().lower()
            if bet_input == 'exit':
                print 'Thank for playing.'
            if not bet_input.isdigit():
                print 'Input Error. Try again.'
            elif int(bet_input) > self.player.chips:
                print 'You do not have enough chips. Please bet again.'
            elif int(bet_input) <= 0:
                print 'You cannot bet less than 0 chips. Please bet again.'
            else:
                return int(bet_input)

    def deal_initial_hands(self):
        self.dealer.hand = self.deck.deal_card()
        self.player.hand = self.deck.deal_card
        self.dealer.hand = self.deck.deal_card()
        self.player.hand = self.deck.deal_card

    def blackjack_check(self):
        if self.player.hand.get_value() == 21 and self.dealer.hand.get_value() == 21:
            print 'Push.'
            self.player.push(self.player.bet)
            return True
        elif self.player.hand.get_value == 21:
            print 'Blackjack!'
            self.player.win(self.player.bet * 1.5)
            return True
        elif self.dealer.hand.get_value == 21:
            print 'Dealer Blackjack!'
            self.player.lose(self.player.bet)
            return True
        return False

    def player_choices(self):
        print ''
        while not self.player.stand and not self.player.is_bust():
            correct_input = False
            while not correct_input:
                hit_or_stand = raw_input('Enter hit or stand: ').strip().lower()
                if (hit_or_stand != 'hit' and hit_or_stand != 'stand' and
                        hit_or_stand != 'h' and hit_or_stand != 's'):
                    print 'Input Error! Please try again.'
                else:
                    correct_input = True

            if hit_or_stand == 'hit' or hit_or_stand == 'h':
                self.player.hit(self.deck.deal_card())
            elif hit_or_stand == 'stand' or hit_or_stand == 's':
                self.player.stand = True

    def check_player_bust
