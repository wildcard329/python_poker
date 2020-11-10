class Card:
    def __init__(self, value, suite):
        self.value = value
        self.suite = suite

    def __str__(self):
        return f"{self.value} of {self.suite}"

    def print_card(self):
        v = self.value
        s = self.suite[0]
        l = v + s
        card = f"""
          __________
        / {l}        \\
        |           |
        |           |
        |           |
        |           |
        |           |
        \\        {l} /
         -----------
         """
        print(card)
