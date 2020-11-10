from card import Card
import random

class Deck():
    def __init__(self):
        self.values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.suites = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
        self.cards = []

    def construct_deck(self):
        for value in self.values:
            for suite in self.suites:
                self.cards.append(Card(value, suite))
    
    def print_deck(self):
        for card in self.cards:
            print(f"{card.value} of {card.suite}")

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        card = self.cards.pop(0)
        return card

    def return_to_deck(self, card):
        self.cards.append(card)
