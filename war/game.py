from war import card
from war import deck
from war import player


class Game:
    def __init__(self):
        name1 = input("name of player1")
        name2 = input("name of player2")
        self.deck = deck.Deck()
        self.p1 = player.Player(name1)
        self.p2 = player.Player(name2)

    def wins(self, winner):
        w = "{} is the winner in this round."
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} は {}, {}　は　{}　を引きました"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("戦争を始めます")
        while len(cards) >= 2:
            m = "qで終了、それ以外のキーでPlay"
            response = input(m)
            if response == "q":
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n,p1c,p2n,p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)
        win = self.winner(self.p1, self.p2)
        print("End. {} is winner.".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p2.wins > p1.wins:
            return p2.name
        return "引き分け"
if __name__ == "__main__":
    game = Game()
    game.play_game()