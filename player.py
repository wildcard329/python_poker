from deck import Deck
from hand import Hand
import random

class Player():
    def __init__(self):
        self.deck = Deck()
        self.hand = []
        self.not_keeping = []
        self.pot = 0
        self.money = 500

    def start(self):
        self.deck.construct_deck()
        self.deck.shuffle()

    def draw_opening(self):
        self.start()
        self.hand.append(self.deck.draw())
        self.hand.append(self.deck.draw())
        self.hand.append(self.deck.draw())
        self.hand.append(self.deck.draw())
        self.hand.append(self.deck.draw())
        self.evaluate_hand()
        self.print_hand()

    def print_hand(self):
        for i in range(len(self.hand)):
            print(f"{self.hand[i].value} of {self.hand[i].suite}\t\t{i + 1}")
            # card.print_card()

    def evaluate_hand(self):
        hand_value = Hand()
        hand_value.read_hand(self.hand)

    def place_bet(self):
        bet_amount = int(input('Bet amount? '))
        self.money -= bet_amount
        self.pot += bet_amount

    def exchange_message(self):
        print('You may exchange a card from your hand, enter card number, or 0 when done.')

    def exchange_cards(self):
        exchange = ''
        while exchange != '0':
            self.exchange_message()
            exchange = input('> ')
            if exchange != '0':
                self.not_keeping.append(self.hand[int(exchange) - 1])
            if exchange == '0':
                print(f"Exchange {self.not_keeping}?")
                self.confirm_exchange()
                confirmation = input('[y]\t[n] ')
                if confirmation == 'y':
                    self.finalize_exchange()
                elif confirmation == 'n':
                    self.not_keeping = []
                    self.exchange_cards()

    def confirm_exchange(self):
        for card in self.not_keeping:
            print(card),

    def finalize_exchange(self):
        for card in self.hand:
            if card in self.not_keeping:
                self.deck.return_to_deck(card)
                self.hand.remove(card)
                self.hand.append(self.deck.draw())
        self.not_keeping = []
        self.evaluate_hand()
        self.print_hand()

    def claim_pot(self):
        if self.evaluate_hand() is not None:
            self.money += self.pot
            self.pot = 0

    def show_money(self):
        print(self.money)

    def show_pot(self):
        print(self.pot)

    def close(self):
        for card in self.hand:
            self.deck.return_to_deck(card)
            self.hand.remove(card)

    def round(self):
        self.show_money()
        self.show_pot()
        self.draw_opening()
        self.place_bet()
        self.exchange_cards()
        self.place_bet()
        self.close()


p = Player()
while p.money > 0:
    p.round()
