from card_attributes import Value
from card import Card
from card_set import CardSet
from trick import Trick
from bid import Bid
from game_state import GameState

# Class representing a round in a game - dynamically updated as tricks are played out until all tricks have been played/won
class Round:

    # Constructor
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

    # Get the list of players in the game
    def getPlayers(self) -> list:
        return self._players

    # Private class to get the shuffled deck of cards - private to avoid players from being able to reverse-engineer what cards each player has
    def _getShuffledDeck(self) -> list:
        return self._shuffled_deck
    
    # Get the index in the list of players of the dealer of the current round
    def getDealerIndex(self) -> int:
        return self._dealer_index
    
    # Get the index of the player currently making a move in the round
    def getCurrentPlayerIndex(self) -> int:
        return self._current_player_index
    
    # Private method to set the index of the player currently making a move in the round
    def _setCurrentPlayerIndex(self, index:int) -> None:
        self._current_player_index = index

    # Private method that increments the index of the player currently making a move in the round - treats player list a circular list
    def _updateCurrentPlayerIndex(self) -> None:
        if self._current_player_index == len(self._players) - 1: self._setCurrentPlayerIndex(0)
        else: self._setCurrentPlayerIndex(self._current_player_index + 1)
    
    # Get the total number of potentially winnable tricks in the round
    def getTotalTricksAvailable(self) -> int:
        return self._total_tricks_available
    
    # Get the value of the pointer to the top of the deck
    def getDeckTopPointer(self) -> int:
        return self._deck_top_pointer
    
    # Get the total number of tricks bid by players
    def getTotalTricksBid(self) -> int:
        return self._total_tricks_bid
    
    # Get a list of tricks completed in the round so far ordered from earliest trick to most recent trick 
    def getTrickLog(self) -> list:
        return self._trick_log

    # Get a list of all bids made by players in the current round - bids indexed by the same order as the list of all players in the game
    def getPlayerBids(self) -> list:
        return self._player_bids
    
    # Get the bid made by a specific player (by index) in the current round
    def getPlayerBid(self, player_index:int) -> Bid:
        return self._player_bids[player_index]
    
    # Private method to set the bid of a specific player (by index)
    def _setPlayerBid(self, player_index:int, bid:int) -> None:
        self._player_bids[player_index] = bid

    # Get the trump card for the current round
    def getTrumpCard(self) -> Card:
        return self._trump_card
    
    # Private method to get a list of hands for each player - private to avoid players being able to access other players' hands
    def _getPlayerHands(self) -> list:
        return self._player_hands
    
    # Private method to get the hand of a specific player (by index)
    def _getPlayerHand(self, player_index:int) -> CardSet:
        return self._player_hands[player_index]
    
    # Private method to add a card to the hand of a specific player (by index)
    def _addCardToHand(self, player_index:int, card:Card) -> None:
        self._player_hands[player_index].addCard(card)

    # Private method to remove a specific card from the hand of a specific player (by index)
    def _removeCardFromHand(self, player_index:int, card:Card) -> None:
        self._player_hands[player_index].removeCard(card)
    
    # Private method that handles dealing cards to players at the start of the round
    def _dealCards(self, current_state:GameState) -> None:

        # Nested loops to deal the proper number of cards to each player - technically not the way cards are dealt in real life but works in simulation because each card dealt is random
        for player_index in range(len(self._players)):
            self._player_hands.append(CardSet(set()))
            for trick_index in range(self._total_tricks_available):
                self._addCardToHand(player_index, self._shuffled_deck[self._deck_top_pointer])
                self._deck_top_pointer -= 1

        # Handle trump card - if it's the last round of the game then set there to be no trump card otherwise decrement deck top pointer
        if self._deck_top_pointer < 0: self._trump_card = Card()
        else:
            self._trump_card = self._shuffled_deck[self._deck_top_pointer]
            self._deck_top_pointer -= 1

        # If the flipped trump card is a Wizard then set the round-level attributes of the game state and prompt the dealer to choose the trump suit
        if self._trump_card.isWizard(): 
            current_state.setRoundAttributes(self._current_player_index, self._total_tricks_available, self._total_tricks_bid, self._trick_log, self._player_bids, self._trump_card, self._getPlayerHand(self._current_player_index))
            self._trump_card = Card(self._players[self._dealer_index].setTrumpSuit(current_state), Value.NULL)
    
    # Private method that handles getting bids from all players
    def _playBiddingPhase(self, current_state:GameState) -> None:

        # Loop to get bids from all players
        submitted_bids = 0
        while submitted_bids < len(self._players):

            # Update current player being prompted using circular list update
            self._updateCurrentPlayerIndex()

            # Set round-level attributes of the game and prompt the current player to make a bid
            current_state.setRoundAttributes(self._current_player_index, self._total_tricks_available, self._total_tricks_bid, self._trick_log, self._player_bids, self._trump_card, self._getPlayerHand(self._current_player_index))
            current_bid = self._players[self._current_player_index].makeBid(current_state)

            # Add the current player's bid to the list of bids and update the total tricks taken/number of players bid
            self._player_bids.append(Bid(current_bid))
            self._total_tricks_bid += current_bid
            submitted_bids += 1

    # Private method that handles getting cards from players over the course of the round
    def _playGamePhase(self, current_state:GameState) -> None:

        # Loop to play all tricks in the round
        for trick_index in range(self._total_tricks_available):

            # Create a new trick for the current trick
            trick = Trick(self._trump_card.getSuit())

            # Nested loop to get moves from all players for the current trick
            total_played_cards = 0
            while total_played_cards < len(self._players):

                # Update current player being prompted using circular list update
                self._updateCurrentPlayerIndex()

                # Set round-level and trick-level attributes of the game and prompt the current player to play a move
                current_state.setRoundAttributes(self._current_player_index, self._total_tricks_available, self._total_tricks_bid, self._trick_log, self._player_bids, self._trump_card, self._getPlayerHand(self._current_player_index))
                current_state.setTrickAttributes(trick.getLeadSuit(), trick.getMoveLog(), trick.getWinningMove(), trick.getCardsPlayed())
                card_played = self._players[self._current_player_index].playCardFromHand(current_state)

                # Update trick with player index and card played and remove played card from the current player's hand
                trick.playMove(self._current_player_index, card_played)
                self._removeCardFromHand(self._current_player_index, card_played)

                # Update total cards played
                total_played_cards += 1

            # Update the list of completed tricks and the number of tricks won by the winner of the current trick
            self._trick_log.append(trick)
            trick_winner_index = trick.getWinningMove().getPlayerIndex()
            self._player_bids[trick_winner_index].incrementMadeTricks()

            # Update current player for the next trick - set to player before winner of the current trick so that the next trick starts with the winner when updating the currnt player 
            self._setCurrentPlayerIndex(trick_winner_index - 1)

    # Function used in games to simulate a full round of the game given the current state/initialization
    def playRound(self, current_state:GameState) -> None:
        self._dealCards(current_state)
        self._playBiddingPhase(current_state)
        self._playGamePhase(current_state)