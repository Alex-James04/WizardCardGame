from card_attributes import Suit
from card import Card
from card_set import CardSet
from move import Move

class GameState:

    def __init__(self) -> None:
        self._players = []
        self._full_deck = CardSet(set())
        self._dealer_index = 0
        self._player_scores = []
        self._round_log = []
        self._total_rounds = 0
        self._current_round = 0

        self._current_player_index = 0
        self._total_tricks_available = 0
        self._total_tricks_bid = 0
        self._trick_log = []
        self._player_bids = []
        self._trump_card = Card()
        self._player_hand = CardSet(set())

        self._lead_suit = Suit.NULL
        self._move_log = []
        self._winning_move = Move()
        self._cards_played = CardSet(set())


    def getPlayers(self) -> list:
        return self._players
    
    def getFullDeck(self) -> CardSet:
        return self._full_deck
    
    def getDealerIndex(self) -> int:
        return self._dealer_index
    
    def getPlayerScores(self) -> list:
        return self._player_scores
    
    def getRoundLog(self) -> list:
        return self._round_log
    
    def getTotalRounds(self) -> int:
        return self._total_rounds
    
    def getCurrentRound(self) -> int:
        return self._current_round
    

    def getCurrentPlayerIndex(self) -> int:
        return self._current_player_index
    
    def getTotalTricksAvailable(self) -> int:
        return self._total_tricks_available
    
    def getTotalTricksBid(self) -> int:
        return self._total_tricks_bid
    
    def getTrickLog(self) -> list:
        return self._trick_log
    
    def getPlayerBids(self) -> list:
        return self._player_bids
    
    def getTrumpCard(self) -> Card:
        return self._trump_card
    
    def getHand(self) -> CardSet:
        return self._player_hand
    
    
    def getLeadSuit(self) -> Suit:
        return self._lead_suit
    
    def getMoveLog(self) -> list:
        return self._move_log
    
    def getWinningMove(self) -> Move:
        return self._winning_move
    
    def getCardsPlayed(self) -> CardSet:
        return self._cards_played
    
    
    def setGameAttributes(self, players:list, full_deck:CardSet, player_scores:list, dealer_index:int, round_log:list, total_rounds:int, current_round:int) -> None:
        self._players = players
        self._full_deck = full_deck
        self._player_scores = player_scores
        self._dealer_index = dealer_index
        self._round_log = round_log
        self._total_rounds = total_rounds
        self._current_round = current_round

    def setRoundAttributes(self, current_player_index:int, total_tricks_available:int, total_tricks_bid:int, trick_log:list, player_bids:list, trump_card:Card, player_hand:CardSet) -> None:
        self._current_player_index = current_player_index
        self._total_tricks_available = total_tricks_available
        self._total_tricks_bid = total_tricks_bid
        self._trick_log = trick_log
        self._player_bids = player_bids
        self._trump_card = trump_card
        self._player_hand = player_hand

    def setTrickAttributes(self, lead_suit:Suit, move_log:list, winning_move:Move, cards_played:CardSet) -> None:
        self._lead_suit = lead_suit
        self._move_log = move_log
        self._winning_move = winning_move
        self._cards_played = cards_played