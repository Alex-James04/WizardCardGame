from card_attributes import Suit, Value
from card import Card
from card_set import CardSet
from player import Player
from game import Game
from trick import Trick
from move import Move
from bid import Bid

class Round:

    def __init__(self, shuffled_deck:list, dealer:Player, total_tricks_avilable:int) -> None:
        self._shuffled_deck = shuffled_deck
        self._deck_top_pointer = len(self._shuffled_deck)-1
        self._dealer = dealer
        self._current_player = dealer
        self._total_tricks_available = total_tricks_avilable
        self._total_tricks_bid = 0
        self._player_hands = {}
        self._completed_tricks = []
        self._player_bids = {}
        self._trump_card = Card()

    def _getShuffledDeck(self) -> list:
        return self._shuffled_deck
    
    def getDeckTopPointer(self) -> int:
        return self._deck_top_pointer
    
    def getDealer(self) -> Player:
        return self._dealer
    
    def getCurrentPlayer(self) -> Player:
        return self._current_player
    
    def _setCurrentPlayer(self, player:Player) -> None:
        self._current_player = player
    
    def getTotalTricksAvailable(self) -> int:
        return self._total_tricks_available
    
    def getTotalTricksBid(self) -> int:
        return self._total_tricks_bid
    
    def _getPlayerHands(self) -> dict:
        return self._player_hands
    
    def _addCardToHand(self, player:Player, card:Card) -> None:
        self._player_hands[player].addCard(card)

    def _removeCardFromHand(self, player:Player, card:Card) -> None:
        self._player_hands[player].removeCard(card)

    def getCompletedTricks(self) -> list:
        return self._completed_tricks

    def getPlayerBids(self) -> dict:
        return self._player_bids
    
    def _setPlayerBid(self, player:Player, bid:int) -> None:
        self._player_bids[player] = bid

    def getTrumpCard(self) -> Card:
        return self._trump_card

    def _updateCurrentPlayer(self, game:Game) -> None:
        current_player_index = game.findPlayer(self._current_player)
        if current_player_index == len(game.getPlayers()) - 1: self._setCurrentPlayer(game.getPlayers()[0])
        else: self._setCurrentPlayer(game.getPlayers()[current_player_index + 1])
    
    def _dealCards(self, game:Game) -> None:
        for player in game.getPlayers():
            self._player_hands[player] = CardSet()
            for trick_index in range(self._total_tricks_available):
                self._addCardToHand(player, self._shuffled_deck[self._deck_top_pointer])
                self._deck_top_pointer -= 1
        self._trump_card = self._shuffled_deck[self._deck_top_pointer]
        self._deck_top_pointer -= 1
        if self._trump_card.isWizard(): self._trump_card = Card(self._dealer.setTrumpSuit(), Value.NULL)
    
    def _playBiddingPhase(self, game:Game) -> None:
        submitted_bids = 0
        while submitted_bids < len(game.getPlayers()):
            self._updateCurrentPlayer(game)
            current_bid = self._current_player.makeBid()
            self._player_bids[self._current_player] = Bid(current_bid)
            self._total_tricks_bid += current_bid
            submitted_bids += 1

    def _playGamePhase(self, game:Game) -> None:
        for current_trick in range(self._total_tricks_available):
            trick = Trick(self._trump_card.getSuit())
            total_played_cards = 0
            while total_played_cards < len(game.getPlayers()):
                self._updateCurrentPlayer(game)
                card_played = self._current_player.playCardFromHand()
                trick.playMove(Move(self._current_player, card_played))
                self._removeCardFromHand(self._current_player, card_played)
                total_played_cards += 1
            self._completed_tricks.append(trick)
            trick_winner = trick.getWinningMove().getPlayer()
            self._player_bids[trick_winner].incrementMadeBids()
            self._setCurrentPlayer(game.getPlayers()[game.findPlayer(trick_winner) - 1])

    def playRound(self, game:Game) -> None:
        self._dealCards(game)
        self._playBiddingPhase(game)
        self._playGamePhase(game)