from enum import Enum, auto

class Side(Enum):
    LONG = auto()
    SHORT = auto()

class Bid:
    def __init__(self, price: int) -> None:
        self.price = price
    
    @classmethod
    def createBid(cls, price: int) -> "Bid":
        return Bid(price)

class Ask:
    def __init__(self, price: int) -> None:
        self.price = price
    
    @classmethod
    def createAsk(cls, price: int) -> "Ask":
        return Ask(price)

class Quote:
    def __init__(self, bid: Bid, ask: Ask) -> None:
        self.bid = bid
        self.ask = ask
    
    @classmethod
    def createQuote(cls, bid: Bid, ask: Ask) -> "Quote":
        return Quote(bid, ask)