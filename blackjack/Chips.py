class Chips:

    def __init__(self, total=100):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self, blackjack):
        if blackjack:
            self.total += int(self.bet * 1.5)
        else:
            self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet
