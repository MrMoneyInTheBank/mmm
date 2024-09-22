from Cards.card import Rank
from Market.market import Side


class Player:
    def __init__(self, name: str, startingBalance: int) -> None:
        self.name = name
        self.balance = startingBalance

    @classmethod
    def createPlayer(cls, name: str, startingBalance: int) -> "Player":
        return Player(name, startingBalance)

    def setBalance(self, newBalance: int) -> None:
        self.balance = newBalance

    def getBalance(self) -> int:
        return self.balance

    def addBalance(self, addition: int) -> None:
        newBalance = self.getBalance() + addition
        self.setBalance(newBalance)

    def deductBalance(self, deduction: int) -> None:
        newBalance = self.getBalance() - deduction
        self.setBalance(newBalance)

    def makeBet(self, marketPrice: int, side: Side, size: int) -> bool:
        maximumHandValue = Rank.ACE.value * 3
        marginNeeded = size * (maximumHandValue - marketPrice)

        if side.name == "LONG" and self.getBalance() >= size * marketPrice:
            self.deductBalance(marketPrice)
            return True
        elif side.name == "SHORT" and self.getBalance() >= marginNeeded:
            self.addBalance(marketPrice)
            return True
        else:
            print(f"{self.name} is unable to {side.name.lower()} at {marketPrice}.")
            return False
