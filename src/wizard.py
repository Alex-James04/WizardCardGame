import time
from game import Game
from player import Player

class Wizard():

    def __init__(self, players:int) -> None:
        self._players_list = [Player() for player in range(players)]

    def playGame(self) -> list:
        game = Game(self._players_list)
        return game.playGame()

if __name__ == "__main__":
    start_time = time.perf_counter_ns()
    num_sims = 100
    num_players = 4
    max_score = -3000
    min_score = 3000
    total_scores = 0
    positional_scores = [0 for player in range(num_players)]
    for i in range(num_sims):
        wizard = Wizard(num_players)
        scores = wizard.playGame()
        if max(scores) > max_score: max_score = max(scores)
        if min(scores) < min_score: min_score = min(scores)
        for j in range(len(positional_scores)): positional_scores[j] += scores[j]
        total_scores += sum(scores)
    print("Total Simulations: ", num_sims)
    print("Max Score: ", max_score)
    print("Min Score: ", min_score)
    print("Average Score: ", total_scores / (num_players * num_sims))
    print("Positional Average Scores: ", [score/num_sims for score in positional_scores])
    print(f"--- %s seconds ---" % ((time.perf_counter_ns() - start_time) / 1000000000))