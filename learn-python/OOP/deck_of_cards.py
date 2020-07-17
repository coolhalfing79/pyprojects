import random


class Card:
    def __init__(self, suite, value):
        self.suite = suite
        self.value = value

    def __repr__(self):
        return f'{self.value} of {self.suite}'


class Deck:
    suites = ['spade', 'diamond', 'clove', 'heart']
    values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self):
        self.cards = []
        for suite in Deck.suites:
            for value in Deck.values:
                self.cards.append(Card(suite, value))

    def __repr__(self):
        return f'Deck of {len(self.cards)} cards'

    def count(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def _deal(self, no_of_cards):
        try:
            dealt_cards = []
            for x in range(no_of_cards):
                dealt_cards.append(self.cards.pop())
        except IndexError:
            raise ValueError('All cards have been dealt')
        finally:
            return dealt_cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, no_of_cards):
        return self._deal(no_of_cards)
