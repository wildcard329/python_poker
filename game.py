from deck import Deck
import random

class Game():
    def __init__(self):
        self.deck = Deck()
        self.hand = []
        self.not_keeping = []

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
        self.print_hand()

    def replace(self, **cards):
        for card in cards:
            self.hand.remove(card)
            self.deck.append(card)
            self.hand.append(self.deck.draw())

    def print_hand(self):
        for i in range(len(self.hand)):
            print(f"{self.hand[i].value} of {self.hand[i].suite}\t\t{i + 1}")
            # card.print_card()

    def exchange_message(self):
        print('You may exchange a card from your hand, enter card number, or 0 when done.')

    def exchange_cards(self):
        exchange = ''
        while exchange != '0':
            self.exchange_message()
            exchange = input('> ')
            self.not_keeping.append(int(exchange))
            if exchange == '0':
                self.not_keeping.remove(self.not_keeping[-1])
                for card in self.not_keeping:
                    print(card)
                    card = int(card)
                print(f"Exchange {self.not_keeping}?")
                confirmation = input('[y]\t[n] ')
                if confirmation == 'y':
                    self.finalize_exchange()
                elif confirmation == 'n':
                    self.not_keeping = []
                    self.exchange_cards()

    def finalize_exchange(self):
        for i in range(len(self.hand)):
            if i - 1 in self.not_keeping:
                self.deck.return_to_deck(self.hand[i - 1])
                self.hand.remove(self.hand[i - 1])
                self.hand.append(self.deck.draw())
        self.not_keeping = []
        self.print_hand()

    def round(self):
        self.draw_opening()
        self.exchange_cards()

g = Game()
g.round()