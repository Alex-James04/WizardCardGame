from card_attributes import Suit, Value
from card import Card
from card_set import CardSet
from round import Round
from game_state import GameState

class Game:
    
    def __init__(self, players:list) -> None:
        self._players = players
        self._full_deck = CardSet(set())
        self._dealer_index = 0
        self._player_scores = []
        self._round_log = []
        self._total_rounds = 60//len(players)
        self._current_round = 1

    def getPlayers(self) -> list:
        return self._players
    
    def _generateDeck(self) -> None:
        for suit in Suit:
            if suit == Suit.NULL:
                for special_card in range(4):
                    self._full_deck.addCard(Card(suit, Value.WIZARD))
                    self._full_deck.addCard(Card(suit, Value.JESTER))
                continue
            for value in Value:
                if value != Value.NULL and value != Value.WIZARD and value != Value.JESTER: self._full_deck.addCard(Card(suit, value))

    def getFullDeck(self) -> CardSet:
        return self._full_deck

    def getPlayerScores(self) -> list:
        return self._player_scores
    
    def getPlayerScore(self, player_index:int) -> int:
        return self._player_scores[player_index]
    
    def _updatePlayerScores(self, round) -> None:
        round_bids = round.getPlayerBids()
        for player_index in range(len(self._players)):
            current_player_bid = round_bids[player_index]
            if len(self._player_scores) < len(self._players): self._player_scores.append(0)
            if current_player_bid.isMet(): self._player_scores[player_index] += (20 + (10*current_player_bid.getMade()))
            else: self._player_scores[player_index] -= abs(10*(current_player_bid.getMade() - current_player_bid.getGoal()))

    def getDealerIndex(self) -> int:
        return self._dealer_index

    def _setDealerPointer(self, index:int) -> None:
        self._dealer_index = index
    
    def _incrementDealerIndex(self) -> None:
        self._dealer_index += 1

    def _updateDealerIndex(self) -> None:
        if self._dealer_index == len(self._players) - 1: self._setDealerPointer(0)
        else: self._incrementDealerIndex()

    def getRoundLog(self) -> list:
        return self._round_log

    def getTotalRounds(self) -> int:
        return self._total_rounds
    
    def getCurrentRound(self) -> int:
        return self._current_round

    def _playRounds(self) -> None:

        for game_round in range(self._total_rounds):
            current_state = GameState()
            current_state.setGameAttributes(self._players, self._full_deck, self._player_scores, self._dealer_index, self._round_log, self._total_rounds, self._current_round)
            round = Round(self._players, self._full_deck.shuffleCards(), self._dealer_index, self._current_round)
            round.playRound(current_state)
            self._updatePlayerScores(round)
            self._updateDealerIndex()
            self._round_log.append(round)
            self._current_round += 1

    def playGame(self) -> list:
        self._generateDeck()
        self._playRounds()
        return self._player_scores