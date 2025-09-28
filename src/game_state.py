from card_attributes import Suit
from card import Card
from card_set import CardSet
from move import Move

# Class that collects information about the state of the game from the other other classes and is passed to the player when they need to make an action
class GameState:

    # Constructor - list of all information available during a player's action
    def __init__(self) -> None:

        # Game-level information that is independent of the current round/trick
        self._players = []
        self._full_deck = CardSet(set())
        self._dealer_index = 0
        self._player_scores = []
        self._round_log = []
        self._total_rounds = 0
        self._current_round = 0

        # Round-level information that is independent of the current trick
        self._current_player_index = 0
        self._total_tricks_available = 0
        self._total_tricks_bid = 0
        self._trick_log = []
        self._player_bids = []
        self._trump_card = Card()
        self._player_hand = CardSet(set())

        # Trick-level information that updates every trick
        self._lead_suit = Suit.NULL
        self._move_log = []
        self._winning_move = Move()
        self._cards_played = CardSet(set())


    # Get individual game-level attributes

    # Get the list of players in the game
    def getPlayers(self) -> list:
        return self._players

    # Get the set of all 60 cards in the game
    def getFullDeck(self) -> CardSet:
        return self._full_deck
    
    # Get the index in the list of players of the dealer of the current round
    def getDealerIndex(self) -> int:
        return self._dealer_index
    
    # Get a list of the current scores in the game - scores indexed by the same order as the list of all players in the game
    def getPlayerScores(self) -> list:
        return self._player_scores
    
    # Get a list of rounds completed in the game so far ordered from earliest round to most recent round
    def getRoundLog(self) -> list:
        return self._round_log
    
    # Get the number of total rounds to be played in the game
    def getTotalRounds(self) -> int:
        return self._total_rounds
    
    # Get what number the current round is in the game
    def getCurrentRound(self) -> int:
        return self._current_round
    

    # Get individual round-level attributes

    # Get the index of the player currently making a move in the list of all players in the game
    def getCurrentPlayerIndex(self) -> int:
        return self._current_player_index
    
    # Get the total number of potentially winnable tricks in the round (equivalent to the current round number)
    def getTotalTricksAvailable(self) -> int:
        return self._total_tricks_available
    
    # Get the total number of tricks bid by players
    def getTotalTricksBid(self) -> int:
        return self._total_tricks_bid
    
    # Get a list of tricks completed in the round so far ordered from earliest round to most recent round
    def getTrickLog(self) -> list:
        return self._trick_log
    
    # Get a list of all bids made by players in the current round - bids indexed by the same order as the list of all players in the game
    def getPlayerBids(self) -> list:
        return self._player_bids
    
    # Get the trump card for the current round
    def getTrumpCard(self) -> Card:
        return self._trump_card
    
    # Get the collection of cards currently in the player's hand that can be used to make an action
    def getHand(self) -> CardSet:
        return self._player_hand
    

    # Get individual trick-level attributes

    # Get the suit lead in the current trick
    def getLeadSuit(self) -> Suit:
        return self._lead_suit
    
    # Get a list of the moves made by players in the current trick - moves indexed by the same order as the list of all players in the game
    def getMoveLog(self) -> list:
        return self._move_log
    
    # Get the move (player and card pair) that is currently winning the trick
    def getWinningMove(self) -> Move:
        return self._winning_move
    
    # Get the collection of all cards played in the trick so far - does not include the trump card or the cards still in the player's hand
    def getCardsPlayed(self) -> CardSet:
        return self._cards_played
    
    # Function used in the game to set the game-level accessible attributes
    def setGameAttributes(self, players:list, full_deck:CardSet, player_scores:list, dealer_index:int, round_log:list, total_rounds:int, current_round:int) -> None:
        self._players = players
        self._full_deck = full_deck
        self._player_scores = player_scores
        self._dealer_index = dealer_index
        self._round_log = round_log
        self._total_rounds = total_rounds
        self._current_round = current_round

    # Function used in the game to set the round-level accessible attributes
    def setRoundAttributes(self, current_player_index:int, total_tricks_available:int, total_tricks_bid:int, trick_log:list, player_bids:list, trump_card:Card, player_hand:CardSet) -> None:
        self._current_player_index = current_player_index
        self._total_tricks_available = total_tricks_available
        self._total_tricks_bid = total_tricks_bid
        self._trick_log = trick_log
        self._player_bids = player_bids
        self._trump_card = trump_card
        self._player_hand = player_hand

    # Function used in the game to set the trick-level accessible attributes
    def setTrickAttributes(self, lead_suit:Suit, move_log:list, winning_move:Move, cards_played:CardSet) -> None:
        self._lead_suit = lead_suit
        self._move_log = move_log
        self._winning_move = winning_move
        self._cards_played = cards_played