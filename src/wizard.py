from game import Game
from player import Player

class Wizard():
    player1 = Player()
    player2 = Player()
    player3 = Player()
    player4 = Player()
    player_list = [player1, player2, player3, player4]
    game = Game(player_list)
    final_scores = game.playGame()
    print(final_scores)

if __name__ == "__main__":
    wizard = Wizard()