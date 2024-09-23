import os
from Game.dealer import Dealer
from Game.player import Player
from Market.market import Side


class Game:
    def __init__(self, dealer: Dealer, player: Player, rounds: int = 3) -> None:
        self.dealer = dealer
        self.player = player
        self.rounds = rounds
        self.inPlay: bool = True

    @classmethod
    def createGame(cls, dealer: Dealer, player: Player) -> "Game":
        rounds = int(input("How many rounds do you want to play: "))
        return Game(dealer, player, rounds)

    def endGame(self) -> None:
        self.inPlay = False

    def playRound(self) -> None:
        os.system("clear")
        hand = self.dealer.deal()
        hand.showHand()

        quote = self.dealer.getQuote(hand)
        print(f"The dealer quotes {quote.bid.price} at {quote.ask.price}.")

        action = self.getPlayerAction()
        size = self.getPositionSize(action)

        print(
            f"\n{self.player.name} wants to{' do' if action == 'nothing' else ''} {action}.\n\n"
        )
        hand.showHand(reveal=True)

        marketPrice = quote.ask.price if action == "buy" else quote.bid.price
        side = Side.LONG if action == "buy" else Side.SHORT

        net = (
            hand.value - marketPrice if side == Side.LONG else marketPrice - hand.value
        )
        net *= size

        acceptedTrade = self.player.makeBet(marketPrice, side, size)
        self.roundResult(acceptedTrade, net, hand.value, side, size)

    def playGame(self) -> None:
        round = 0

        while self.inPlay and round < self.rounds:
            self.playRound()

            if self.player.getBalance() <= 0:
                self.endGame()

            round += 1

        print(f"Thank you for playing {self.player.name}.")
        print(
            f"You {'made' if self.player.getBalance() - self.player.startingBalance > 0 else 'lost'} ${abs( self.player.getBalance() - self.player.startingBalance )} ending up with ${self.player.getBalance()}."
        )

        input("\nPress Enter to close game.")

    def getPlayerAction(self) -> str:
        action = input("\nWhat would you like to do? (buy, sell, nothing): ").lower()
        while action not in {"buy", "sell", "nothing"}:
            action = input(
                "Sorry, please re-enter your selection (buy, sell, nothing): "
            )

        return action

    def getPositionSize(self, action: str) -> int:
        if action != "nothing":
            return int(input("How many lots do you want to trade: "))
        return 0

    def roundResult(
        self, acceptedTrade: bool, net: int, handValue: int, side: Side, size: int
    ) -> None:
        if not acceptedTrade:
            print("Whoops, you lost your chance!")
        else:
            if side == Side.LONG:
                self.player.addBalance(handValue * size)
            elif side == Side.SHORT:
                self.player.addBalance(-handValue * size)

            if net == 0:
                print(f"\nYour balance is still: {self.player.getBalance()}")
            else:
                print(
                    f"\nYou {'made' if net > 0 else 'lost'} ${net}. Your new balance is ${self.player.getBalance()}"
                )

        input("Press Enter to continue...")
        os.system("clear")
