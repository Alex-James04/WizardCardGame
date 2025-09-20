from card import Card
from card_set import CardSet
from player import Player
from game import Game

class Round:

    def __init__(self, game:Game, shuffled_deck:list, dealer:Player, total_tricks_avilable:int) -> None:
        self._game = game
        self._shuffled_deck = shuffled_deck
        self._deck_top_pointer = len(self._shuffled_deck)-1
        self._dealer = dealer
        self._total_tricks_available = total_tricks_avilable
        self._total_tricks_bid = 0
        self._player_hands = {}
        self._completed_tricks = {}
        self._player_bids = {}
        self._trump_card = Card()

    def getGameInstance(self) -> Game:
        return self._game

    def _getShuffledDeck(self) -> list:
        return self._shuffled_deck
    
    def getDeckTopPointer(self) -> int:
        return self._deck_top_pointer
    
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
        for player in self._game.getPlayers():
            if player not in self._player_hands.keys(): self._player_hands[player] = CardSet()
            for trick_index in range(self._total_tricks_available):
                self._player_hands[player].addCard(self._shuffled_deck[self._deck_top_pointer])
                self._deck_top_pointer -= 1
        self._trump_card = self._shuffled_deck[self._deck_top_pointer]
        self._deck_top_pointer -= 1
    
    def _playBiddingPhase(self) -> None:
        ### looped gameplay of taking player's bids and setting them using repeated calls to setPlayerBid
        ### will pass a GameState object to the player every time they make a bid

        self._updateTotalTricksBid()

    def _playGamePhase(self) -> None:
        ### looped gameplay of tricks that calls updateCompletedTricks and updatePlayerBids after every trick completed
        ### will pass a GameState object to the player every time they make a move

        pass

    def playRound(self) -> None:
        self._dealCards()
        self._playBiddingPhase()
        self._playGamePhase()