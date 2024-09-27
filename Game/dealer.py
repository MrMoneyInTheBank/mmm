from typing import Optional
import random
import math
from Game.constants import EXPECTED_HAND_VALUE, VOLATILITY
from Cards.deck import Deck
from Cards.hand import Hand
from Market.market import Bid, Ask, Quote


class Dealer:
    def __init__(self, deck: Optional[Deck] = None) -> None:
        self.deck = deck if deck else Deck.createDeck()

    def deal(self) -> Hand:
        return self.deck.drawThree()

    def getQuote(self, hand: Hand, tolerance: float = 1.0) -> Quote:
        if hand.value < EXPECTED_HAND_VALUE:
            tolerance = random.uniform(0.5, 1.0)
        elif hand.value > EXPECTED_HAND_VALUE:
            tolerance = random.uniform(1.0, 1.5)

        bid = Bid(math.floor(EXPECTED_HAND_VALUE - tolerance * VOLATILITY))
        ask = Ask(math.ceil(EXPECTED_HAND_VALUE - tolerance * VOLATILITY))

        quote = Quote(bid, ask)

        return quote
