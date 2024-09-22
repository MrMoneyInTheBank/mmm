from typing import List
import random
from Cards.card import Card


class Hand:
    def __init__(self, cards: List[Card]) -> None:
        self.cards = cards
        self.hiddenCards: List[bool] = self.hideCards()
        self.value = sum([card.rank.value for card in self.cards])

    @classmethod
    def createHand(cls, cards: List[Card]) -> "Hand":
        return Hand(cards)

    def hideCards(self) -> List[bool]:
        shown = 0
        hiddenCards = [True for _ in range(len(self.cards))]

        for idx in range(len(hiddenCards)):
            hidden = random.choice([True, False]) if shown != 2 else True
            if not hidden:
                shown += 1

            hiddenCards[idx] = hidden

        return hiddenCards

    def showHand(self, reveal: bool = False) -> None:
        for index, card in enumerate(self.cards):
            if self.hiddenCards[index] and not reveal:
                print(f"{index + 1}. This card is hidden.")
            else:
                print(f"{index + 1}. {card}")
