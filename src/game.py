from card_attributes import Suit, Value
from card import Card
from card_set import CardSet
from player import Player
from round import Round

class Game:
    
    def __init__(self, players:list) -> None:
        self._full_deck = CardSet()
        self._players = players
        self._player_scores = {}
        self._dealer_pointer = -1
        self._completed_rounds = []
        self._total_rounds = 60//len(players)
        self._current_round = 1

    def getFullDeck(self) -> CardSet:
        return self._full_deck

    def _generateDeck(self) -> None:
        for suit in Suit:
            if suit == Suit.NULL:
                for special_card in range(4):
                    self._full_deck.addCard(Card(suit, Value.WIZARD))
                    self._full_deck.addCard(Card(suit, Value.JESTER))
                continue
            for value in Value:
                if value != Value.NULL and value != Value.WIZARD and value != Value.JESTER: self._full_deck.addCard(Card(suit, value))

    def getPlayers(self) -> list:
        return self._players

    def findPlayer(self, Player) -> int:
        return self._players.index(Player)

    def getPlayerScores(self) -> dict:
        return self._player_scores
    
    def _updatePlayerScores(self, round) -> None:
        round_bids = round.getPlayerBids()
        for player in self._players:
            current_player_bid = round_bids[player]
            if current_player_bid.isMet(): self._player_scores[player] += (20 + (10*current_player_bid.getMade()))
            else: self._player_scores[player] -= abs(10*(current_player_bid.getMade() - current_player_bid.getGoal()))

    def getDealer(self) -> Player:
        return self._players[self._dealer_pointer]

    def _setDealerPointer(self, index:int) -> None:
        self._dealer_pointer = index
    
    def _incrementDealerPointer(self) -> None:
        self._dealer_pointer += 1

    def _getNextDealer(self) -> Player:
        if self._dealer_pointer == len(self._players) - 1: self._setDealerPointer(0)
        else: self._incrementDealerPointer()
        return self._players[self._players.index(self._dealer_pointer)]

    def getCompletedRounds(self) -> list:
        return self._completed_rounds

    def getTotalRounds(self) -> int:
        return self._total_rounds
    
    def getCurrentRound(self) -> int:
        return self._current_round

    def _playRounds(self) -> None:

        for game_round in range(self._total_rounds):

            round = Round(self._full_deck.shuffleCards(), self._getNextDealer(), self._current_round)
            round.playRound(self)

            self._updatePlayerScores(round)
            self._completed_rounds.append(round)
            self._current_round += 1

    def playGame(self) -> int:
        self._generateDeck()
        self._playRounds()
        final_scores = self._player_scores.items()
        winner = (Player(), 0)
        for player, score in final_scores:
            if score > winner[1]: winner = (player, score)
        return self.findPlayer(winner[0])