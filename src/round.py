from card import Card
from card_set import CardSet
from player import Player

class Round:

    def __init__(self, unshuffled_deck:CardSet, dealer:Player, total_tricks_avilable:int) -> None:
        self._shuffled_deck = unshuffled_deck.shuffleCards()
        self._dealer = dealer
        self._total_tricks_available = total_tricks_avilable
        self._total_tricks_bid = 0
        self._player_hands = {}
        self._completed_tricks = {}
        self._player_bids = {}
        self._trump_card = Card()

    def _getShuffledDeck(self) -> list:
        return self._shuffled_deck
    
    def getDealer(self) -> Player:
        return self._dealer
    
    def getTotalTricksAvailable(self) -> int:
        return self._total_tricks_available
    
    def getTotalTricksBid(self) -> int:
        return self._total_tricks_bid
    
    def _updateTotalTricksBid(self) -> None:
        pass
    
    def _getPlayerHands(self) -> dict:
        return self._player_hands
    
    def _addCardToHand(self, player:Player, card:Card) -> None:
        self._player_hands[player].addCard(card)

    def _removeCardFromHand(self, player:Player, card:Card) -> None:
        self._player_hands[player].removeCard(card)

    def getCompletedTricks(self) -> dict:
        return self._completed_tricks
    
    def _updateCompletedTricks(self) -> None:
        pass

    def getPlayerBids(self) -> dict:
        return self._player_bids
    
    def _setPlayerBid(self, player:Player, bid:int) -> None:
        self._player_bids[player] = bid

    def _updatePlayerBids(self) -> None:
        pass

    def getTrumpCard(self) -> Card:
        return self._trump_card
    
    def _dealCards(self) -> None:
        pass
    
    def _playBiddingPhase(self) -> None:
        self._updatePlayerBids()
        self._updateTotalTricksBid()

    def _playGamePhase(self) -> None:
        pass

    def playRound(self) -> None:
        self._dealCards()
        self._playBiddingPhase()
        self._playGamePhase()