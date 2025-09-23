from card_attributes import Value
from card import Card
from card_set import CardSet
from trick import Trick
from bid import Bid
from game_state import GameState

class Round:

    def __init__(self, players:list, shuffled_deck:list, dealer_index:int, total_tricks_avilable:int) -> None:
        self._players = players
        self._shuffled_deck = shuffled_deck
        self._dealer_index = dealer_index
        self._current_player_index = dealer_index
        self._total_tricks_available = total_tricks_avilable
        self._deck_top_pointer = len(self._shuffled_deck) - 1
        self._total_tricks_bid = 0
        self._trick_log = []
        self._player_bids = []
        self._trump_card = Card()
        self._player_hands = []

    def getPlayers(self) -> list:
        return self._players

    def _getShuffledDeck(self) -> list:
        return self._shuffled_deck
    
    def getDealerIndex(self) -> int:
        return self._dealer_index
    
    def getCurrentPlayerIndex(self) -> int:
        return self._current_player_index
    
    def _setCurrentPlayerIndex(self, index:int) -> None:
        self._current_player_index = index

    def _updateCurrentPlayerIndex(self) -> None:
        if self._current_player_index == len(self._players) - 1: self._setCurrentPlayerIndex(0)
        else: self._setCurrentPlayerIndex(self._current_player_index + 1)
    
    def getTotalTricksAvailable(self) -> int:
        return self._total_tricks_available
    
    def getDeckTopPointer(self) -> int:
        return self._deck_top_pointer
    
    def getTotalTricksBid(self) -> int:
        return self._total_tricks_bid
    
    def getTrickLog(self) -> list:
        return self._trick_log

    def getPlayerBids(self) -> list:
        return self._player_bids
    
    def getPlayerBid(self, player_index:int) -> Bid:
        return self._player_bids[player_index]
    
    def _setPlayerBid(self, player_index:int, bid:int) -> None:
        self._player_bids[player_index] = bid

    def getTrumpCard(self) -> Card:
        return self._trump_card
    
    def _getPlayerHands(self) -> list:
        return self._player_hands
    
    def _getPlayerHand(self, player_index:int) -> CardSet:
        return self._player_hands[player_index]
    
    def _addCardToHand(self, player_index:int, card:Card) -> None:
        self._player_hands[player_index].addCard(card)

    def _removeCardFromHand(self, player_index:int, card:Card) -> None:
        self._player_hands[player_index].removeCard(card)
    
    def _dealCards(self, current_state:GameState) -> None:
        for player_index in range(len(self._players)):
            self._player_hands.append(CardSet(set()))
            for trick_index in range(self._total_tricks_available):
                self._addCardToHand(player_index, self._shuffled_deck[self._deck_top_pointer])
                self._deck_top_pointer -= 1
        self._trump_card = self._shuffled_deck[self._deck_top_pointer]
        self._deck_top_pointer -= 1
        current_state.setRoundAttributes(self._current_player_index, self._total_tricks_available, self._total_tricks_bid, self._trick_log, self._player_bids, self._trump_card, self._getPlayerHand(self._current_player_index))
        if self._trump_card.isWizard(): self._trump_card = Card(self._players[self._dealer_index].setTrumpSuit(current_state), Value.NULL)
    
    def _playBiddingPhase(self, current_state:GameState) -> None:
        submitted_bids = 0
        while submitted_bids < len(self._players):
            self._updateCurrentPlayerIndex()
            current_state.setRoundAttributes(self._current_player_index, self._total_tricks_available, self._total_tricks_bid, self._trick_log, self._player_bids, self._trump_card, self._getPlayerHand(self._current_player_index))
            current_bid = self._players[self._current_player_index].makeBid(current_state)
            self._player_bids.append(Bid(current_bid))
            self._total_tricks_bid += current_bid
            submitted_bids += 1

    def _playGamePhase(self, current_state:GameState) -> None:
        for trick_index in range(self._total_tricks_available):
            trick = Trick(self._trump_card.getSuit())
            total_played_cards = 0
            while total_played_cards < len(self._players):
                self._updateCurrentPlayerIndex()
                current_state.setRoundAttributes(self._current_player_index, self._total_tricks_available, self._total_tricks_bid, self._trick_log, self._player_bids, self._trump_card, self._getPlayerHand(self._current_player_index))
                current_state.setTrickAttributes(trick.getLeadSuit(), trick.getMoveLog(), trick.getWinningMove(), trick.getCardsPlayed())
                card_played = self._players[self._current_player_index].playCardFromHand(current_state)
                trick.playMove(self._current_player_index, card_played)
                self._removeCardFromHand(self._current_player_index, card_played)
                total_played_cards += 1
            self._trick_log.append(trick)
            trick_winner_index = trick.getWinningMove().getPlayerIndex()
            self._player_bids[trick_winner_index].incrementMadeBids()
            self._setCurrentPlayerIndex(trick_winner_index - 1)

    def playRound(self, current_state:GameState) -> None:
        self._dealCards(current_state)
        self._playBiddingPhase(current_state)
        self._playGamePhase(current_state)