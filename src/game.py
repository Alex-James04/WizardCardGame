from card_set import CardSet

class Game:
    
    def __init__(self, players:list) -> None:
        self._full_deck = CardSet()
        self._players = players
        self._player_scores = {}
        self._rounds = {}
        self._total_rounds = 60//len(players)
        self._current_round = 0

    def _generateDeck(self) -> None:
        pass

    def getFullDeck(self) -> CardSet:
        return self._full_deck

    def getPlayers(self) -> list:
        return self._players

    def getPlayerScores(self) -> dict:
        return self._player_scores

    def _updatePlayerScores(self) -> None:
        pass

    def getRounds(self) -> dict:
        return self._rounds
    
    def _updateRounds(self) -> None:
        pass

    def getTotalRounds(self) -> int:
        return self._total_rounds
    
    def getCurrentRound(self) -> int:
        return self._current_round
    
    def updateCurrentRound(self) -> None:
        pass

    def playGame(self) -> None:
        self._generateDeck()

        # looped gameplay of rounds that calls updatePlayerScores, updateRounds, and updateCurrentRound for every round in the game
        # the instance of the game "self" is passed to every round in updateRounds' round instances (as well as a shuffled version of the full deck) so players can access game-level attributes