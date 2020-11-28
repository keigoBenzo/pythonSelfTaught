from random import shuffle
from war import card

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(card.Card(i, j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

if __name__ == "__main__":
    deck = Deck()
    for card in deck.cards:
        print(card)