from card import Card

class Hand():
    def __init__(self):
        self.hand = []
        self.values = {}
        self.suites = {}
        self.pair = None
        self.two_pair = None
        self.three_kind = None
        self.flush = None
        self.full_house = None
        self.four_kind = None

    def read_hand(self, hand):
        vals = {}
        for card in hand:
            self.hand.append(card)
        for card in self.hand:
            if card.value not in self.values:
                self.values[card.value] = []
            self.values[card.value].append(card)
            if card.suite not in self.suites:
                self.suites[card.suite] = []
            self.suites[card.suite].append(card)

        for card in self.values:
            if len(self.values[card]) == 2:
                self.pair = f"Pair of {card}s"
                self.two_pair = []
                self.two_pair.append(card)
            elif len(self.values[card]) == 3:
                self.three_kind = f"Three {card}s"
            elif len(self.values[card]) == 4:
                self.four_kind = f"Four {card}s"

        if self.pair is not None and self.three_kind is not None:
            self.full_house = f"{self.three_kind}, {self.pair}"

        for card in self.suites:
            if len(self.suites[card]) == 1:
                self.flush = f"{card} flush"
        self.evaluate_hand()
        
    def evaluate_hand(self):
        if self.pair is not None:
            print(self.pair)
        if self.two_pair is not None and len(self.two_pair) == 2:
            print(f"Pair of {self.two_pair[0]}s and {self.two_pair[1]}s")
        if self.three_kind is not None:
            print(self.three_kind)
        if self.four_kind is not None:
            print(self.four_kind)
        if self.full_house is not None:
            print(self.full_house)
        
