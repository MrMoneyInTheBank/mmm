from enum import Enum, auto


class Side(Enum):
    LONG = auto()
    SHORT = auto()


class Bid:
    def __init__(self, price: int) -> None:
        self.price = price


class Ask:
    def __init__(self, price: int) -> None:
        self.price = price


class Quote:
    def __init__(self, bid: Bid, ask: Ask) -> None:
        self.bid = bid
        self.ask = ask
