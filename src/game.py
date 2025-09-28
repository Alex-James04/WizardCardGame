from card_attributes import Suit, Value
from card import Card
from card_set import CardSet
from round import Round
from game_state import GameState

# Class representing a game of Wizard - updated as rounds have been played
class Game:
    
    # Constructor - takes in list of players used as universal point of reference for the rest of the game
    def __init__(self, players:list) -> None:
        self._players = players
        self._full_deck = CardSet(set())
        self._dealer_index = 0
        self._player_scores = []
        self._round_log = []
        self._total_rounds = 60//len(players)
        self._current_round = 1

    # Get the list of players in the game
    def getPlayers(self) -> list:
        return self._players
    
    # Private method to generate the full 60 card deck - for each suit and value add a card to the deck plus four Wizards and four Jesters
    def _generateDeck(self) -> None:
        for suit in Suit:
            if suit == Suit.NULL:
                for special_card in range(4):
                    self._full_deck.addCard(Card(suit, Value.WIZARD))
                    self._full_deck.addCard(Card(suit, Value.JESTER))
                continue
            for value in Value:
                if value != Value.NULL and value != Value.WIZARD and value != Value.JESTER: self._full_deck.addCard(Card(suit, value))

    # Get the set of all 60 cards in the game
    def getFullDeck(self) -> CardSet:
        return self._full_deck

    # Get a list of the current scores in the game - scores indexed by the same order as the list of all players in the game
    def getPlayerScores(self) -> list:
        return self._player_scores
    
    # Get the score of a specific player in the game (by index)
    def getPlayerScore(self, player_index:int) -> int:
        return self._player_scores[player_index]
    
    # Private method to update the scores of all the players in the game with the results of a completed round
    def _updatePlayerScores(self, round) -> None:

        # Get the bids set/made from the round and loop through each player to update their scores
        round_bids = round.getPlayerBids()
        for player_index in range(len(self._players)):
            current_player_bid = round_bids[player_index]

            # If it's the first round then set the current player's score to 0
            if len(self._player_scores) < len(self._players): self._player_scores.append(0)

            # Update scores based on results of the inputted round
            if current_player_bid.isMet(): self._player_scores[player_index] += (20 + (10*current_player_bid.getMade()))
            else: self._player_scores[player_index] -= abs(10*(current_player_bid.getMade() - current_player_bid.getGoal()))

    # Get the index of the player in the list of players in the game who is the dealer in the current round 
    def getDealerIndex(self) -> int:
        return self._dealer_index

    # Private method to set the index of the player in the list of players in the game who is the dealer in the current round
    def _setDealerIndex(self, index:int) -> None:
        self._dealer_index = index
    
    # Private method to increment the index of the player in the list of players in the game who is the dealer in the current round
    def _incrementDealerIndex(self) -> None:
        self._dealer_index += 1

    # Private method that increments the index of the player in the list of players who is the dealer in the current round - treats player list a circular list
    def _updateDealerIndex(self) -> None:
        if self._dealer_index == len(self._players) - 1: self._setDealerIndex(0)
        else: self._incrementDealerIndex()

    # Get a list of rounds completed in the game so far ordered from earliest round to most recent round
    def getRoundLog(self) -> list:
        return self._round_log

    # Get the number of total rounds to be played in the game
    def getTotalRounds(self) -> int:
        return self._total_rounds
    
    # Get what number the current round is in the game
    def getCurrentRound(self) -> int:
        return self._current_round

    # Private method that handles playing each round of the game
    def _playRounds(self) -> None:

        # Loop to play each round in the game
        for game_round in range(self._total_rounds):

            # Create a game-state object for the current round to be passed to the player in the round
            current_state = GameState()

            # Set game-level attributes of the game
            current_state.setGameAttributes(self._players, self._full_deck, self._player_scores, self._dealer_index, self._round_log, self._total_rounds, self._current_round)

            # Create a round with the current game state and play the round
            round = Round(self._players, self._full_deck.getShuffledList(), self._dealer_index, self._current_round)
            round.playRound(current_state)

            # Update scores, dealer, round log, and current round with the results of the round played
            self._updatePlayerScores(round)
            self._updateDealerIndex()
            self._round_log.append(round)
            self._current_round += 1

    # Function used to simulate a full game given the initialized list of players
    def playGame(self) -> list:
        self._generateDeck()
        self._playRounds()
        return self._player_scores