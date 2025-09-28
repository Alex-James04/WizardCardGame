from card_attributes import Suit, Value
from card import Card
from card_set import CardSet
from move import Move

# Class representing a single trick in a round - dynamically updated as players make their moves until the final player has played
class Trick:

    # Constructor
    def __init__(self, trump_suit:Suit=Suit.NULL) -> None:
        self._trump_suit = trump_suit
        self._lead_suit = Suit.NULL
        self._move_log = []
        self._winning_move = Move()
        self._cards_played = CardSet(set())

    # Get the suit of the trump card of the current trick
    def getTrumpSuit(self) -> Suit:
        return self._trump_suit
    
    # Get the suit of the lead card of the current trick
    def getLeadSuit(self) -> Suit:
        return self._lead_suit
    
    # Private function that takes in a card played in the trick and updates the lead suit for the trick if the card was either the first card played or the first non-Jester card following a led Jester
    def _updateLeadSuit(self, card:Card) -> None:
        if self._lead_suit == Suit.NULL:
            if not self._cards_played.isEmpty() and self._move_log[0].getCard().isWizard(): return
            self._lead_suit = card.getSuit()

    # Get the list of moves made so far in the trick ordered starting with the earliest made move
    def getMoveLog(self) -> list:
        return self._move_log

    # Get the move that is currently winning the trick
    def getWinningMove(self) -> Move:
        return self._winning_move
    
    # Private function that takes in a move made in the trick and updates which card played in the trick is currently winning
    def _updateWinningMove(self, move:Move) -> None:

        # If the card played is the first played then it is currently winning
        if self._cards_played.isEmpty(): 
            self._winning_move = move
            return
        
        # Attributes of the currently winning card and the card being played currently
        winning_suit = self._winning_move.getCard().getSuit()
        winning_value = self._winning_move.getCard().getValue()
        current_suit = move.getCard().getSuit()
        current_value = move.getCard().getValue()

        # List of guard cases where the currently winning card remains the winning card
        if winning_value == Value.WIZARD: return
        if current_value == Value.JESTER: return
        if winning_suit == current_suit and winning_value.value >= current_value.value: return
        if winning_suit == self._trump_suit and current_value != Value.WIZARD: return
        if winning_suit == self._lead_suit and current_value != Value.WIZARD and current_suit != self._trump_suit: return

        # Update the winning move to be the move currnelty being played
        self._winning_move = move

    # Get the collection of all cards played in the trick so far
    def getCardsPlayed(self) -> CardSet:
        return self._cards_played
    
    # Function used in rounds to update the state of the trick when a player makes a move
    def playMove(self, player_index:int, card:Card) -> None:
        move = Move(player_index, card)
        self._updateLeadSuit(card)
        self._updateWinningMove(move)
        self._cards_played.addCard(card)
        self._move_log.append(move)