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
        hand = self.dealer.deal()
        print("The dealer has drawn the following cards.\n")
        hand.showHand()

        quote = self.dealer.getQuote(hand)
        print(f"The dealer quotes {quote.bid.price} at {quote.ask.price}.")

        action = self.getPlayerAction()
        size = self.getPositionSize(action)

        print(
            f"\n{self.player.name} wants to{' do' if action == 'nothing' else ''} {action}.\n\n"
        )
        print("The hidden card(s) were:")
        hand.showHand(reveal=True)

        net: int = 0
        acceptedTrade: bool = False
        if action == "buy":
            acceptedTrade |= self.player.makeBet(quote.ask.price, Side.LONG, size)
            net = hand.value - quote.ask.price
        elif action == "sell":
            acceptedTrade |= self.player.makeBet(quote.bid.price, Side.SHORT, size)
            net = quote.bid.price - hand.value

        self.roundResult(acceptedTrade, net)

    def playGame(self) -> None:
        round = 0

        while self.inPlay and round < self.rounds:
            self.playRound()

            if self.player.getBalance() <= 0:
                self.endGame()

            round += 1

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

    def roundResult(self, acceptedTrade: bool, net: int) -> None:
        if not acceptedTrade:
            print("Whoops, you lost your chance!")
        elif net == 0:
            print(f"\nYour balance is still: {self.player.getBalance()}")
        else:
            self.player.addBalance(net)
            print(
                f"\nYou {'made' if net > 0 else 'lost'} ${net}. Your new balance is {self.player.getBalance()}"
            )

        input("Press Enter to continue...")
        os.system("clear")
