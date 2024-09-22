from typing import List
import random
from Cards.card import Rank, Suit, Card
from Cards.hand import Hand


class Deck:
    def __init__(self, deck: List[Card]) -> None:
        self.deck: List[Card] = deck

    @classmethod
    def createDeck(cls) -> "Deck":
        deck: List[Card] = []

        for rank in Rank:
            for suit in Suit:
                deck.append(Card.createCard(rank, suit))

        return Deck(deck)

    def drawThree(self) -> Hand:
        return Hand.createHand(random.sample(self.deck, k=3))
