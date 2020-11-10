from card import Card

class Hand():
    def __init__(self):
        self.hand = []
        self.values = set()
        self.suites = set()

    def read_hand(self, hand):
        for card in hand:
            self.hand.append(card)
        for card in self.hand:
            self.values.add(card.value)
            self.suites.add(card.suite)
        print(f"hand: {self.hand}\nvalues: {len(self.values)}\nsuites: {len(self.suites)}")
        print(self.evaluate_hand())

    def evaluate_hand(self):
        self.check_for_pair()
        self.check_for_two_pair()
        self.check_for_three_of_a_kind()
        self.check_for_flush()
        self.check_for_full_house()
        self.check_for_four_of_a_kind()

    def check_for_pair(self):
        if len(self.values) == 4:
            for card in self.hand:
                if self.hand.count(card.value) == 2:
                    pair = f"Pair of {card.value}s"
                    print(pair)
                    return pair

    def check_for_two_pair(self):
        if len(self.values) == 3:
            for card1 in self.hand:
                for card2 in self.hand:
                    if self.hand.count(card1) == 2 and self.hand.count(card2) == 2:
                        pairs = f"Pair of {card1.value}s and pair of {card2.value}s"
                        print(pairs)
                        return pairs

    def check_for_three_of_a_kind(self):
        if len(self.values) == 3:
            for card in self.hand:
                if self.hand.count(card) == 3:
                    three_kind = f"Three {card.value}s"

    def check_for_full_house(self):
        self.check_for_pair()
        self.check_for_three_of_a_kind

    def check_for_four_of_a_kind(self):
        if len(self.values) == 2:
            for card in self.hand:
                if self.hand.count(card) == 4:
                    four_kind = f"Four {card.value}s"

    def check_for_flush(self):
        if len(self.suites) == 1:
            for card in self.hand:
                if self.hand.count(card.suite) == 5:
                    flush = f"{card.suite} flush"
                    print(flush)
                    return flush
