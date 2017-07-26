import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck(object):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


if __name__ == "__main__":
    # since Python 2.6, namedtuple can be used to construct a simple
    # class of objects are just bundles with no custom methods, like
    # a database records
    beer_card = Card('7', 'diamonds')
    print(beer_card)

    deck = FrenchDeck()

    # because of __len__
    print(len(deck))

    # because of __getitem__
    print(deck[-1])
    print(deck[2:34])
    print(deck[12::13])

    # pick a random card
    print(choice(deck))
    print(choice(deck))
    print(choice(deck))
    print(choice(deck))
    print(choice(deck))
