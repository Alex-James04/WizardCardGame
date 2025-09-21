from card_attributes import Suit, Value
from card import Card
from card_set import CardSet
from player import Player
from game import Game
from trick import Trick
from move import Move
from bid import Bid

class Round:

    def __init__(self, game:Game, shuffled_deck:list, dealer:Player, total_tricks_avilable:int) -> None:
        self._game = game
        self._shuffled_deck = shuffled_deck
        self._deck_top_pointer = len(self._shuffled_deck)-1
        self._dealer = dealer
        self._total_tricks_available = total_tricks_avilable
        self._total_tricks_bid = 0
        self._player_hands = {}
        self._completed_tricks = []
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
    
    def _dealCards(self) -> None:
        for player in self._game.getPlayers():
            if player not in self._player_hands.keys(): self._player_hands[player] = CardSet()
            for trick_index in range(self._total_tricks_available):
                self._player_hands[player].addCard(self._shuffled_deck[self._deck_top_pointer])
                self._deck_top_pointer -= 1
        self._trump_card = self._shuffled_deck[self._deck_top_pointer]
        self._deck_top_pointer -= 1
        if self._trump_card.isWizard(): self._trump_card = Card(self._dealer.setTrumpSuit(), Value.NULL)
    
    def _playBiddingPhase(self) -> None:
        submitted_bids = 0
        while submitted_bids < len(self._game.getPlayers()):
            current_player = self._game.getNextPlayer()
            current_bid = current_player.makeBid()
            self._player_bids[current_player] = Bid(current_bid)
            self._total_tricks_bid += current_bid
            submitted_bids += 1

    def _playGamePhase(self) -> None:
        for current_trick in range(self._total_tricks_available):
            trick = Trick(self._trump_card.getSuit())
            played_cards = 0
            while played_cards < len(self._game.getPlayers()):
                current_player = self._game.getNextPlayer()
                trick.playMove(Move(current_player.playCardFromHand(), current_player))
                played_cards += 1
            self._completed_tricks.append(trick)
            trick_winner = trick.getWinningMove().getPlayer()
            self._player_bids[trick_winner].incrementMadeBids()
            self._game.setPlayerPointer(self._game.getPlayerIndex(trick_winner) - 1)

    def playRound(self) -> None:
        self._dealCards()
        self._playBiddingPhase()
        self._playGamePhase()