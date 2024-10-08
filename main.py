from Game.dealer import Dealer
from Game.player import Player
from Game.game import Game


if __name__ == "__main__":
    try:
        dealer = Dealer()
        player = Player.createPlayer()
        game = Game.createGame(dealer, player)

        game.playGame()
    except Exception as e:
        print(f"An error occurred: {e}")
        print("I guess it wasn't meant to be.")
