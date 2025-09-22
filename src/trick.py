from card_attributes import Suit, Value
from card import Card
from card_set import CardSet
from move import Move

class Trick:

    def __init__(self, trump_suit:Suit=Suit.NULL) -> None:
        self._trump_suit = trump_suit
        self._lead_suit = Suit.NULL
        self._move_log = []
        self._winning_move = Move()
        self._cards_played = CardSet()

    def getTrumpSuit(self) -> Suit:
        return self._trump_suit
    
    def getLeadSuit(self) -> Suit:
        return self._lead_suit
    
    def _updateLeadSuit(self, card:Card) -> None:
        if self._lead_suit == Suit.NULL:
            if not self._cards_played.isEmpty() and self._move_log[0].getCard().isWizard(): return
            self._lead_suit = card.getSuit()

    def getMoveLog(self) -> list:
        return self._move_log
    
    def _updateMoveLog(self, move: Move) -> None:
        self._move_log.append(move)

    def getWinningMove(self) -> Move:
        return self._winning_move
    
    def _updateWinningMove(self, move:Move) -> None:
        if self._cards_played.isEmpty(): 
            self._winning_move = move
            return
        winning_suit = self._winning_move.getCard().getSuit()
        winning_value = self._winning_move.getCard().getValue()
        current_suit = move.getCard().getSuit()
        current_value = move.getCard().getValue()
        if winning_value == Value.WIZARD: return
        if current_value == Value.JESTER: return
        if winning_suit == current_suit and winning_value.value >= current_value.value: return
        if winning_suit == self._trump_suit and current_value != Value.WIZARD: return
        if winning_suit == self._lead_suit and current_value != Value.WIZARD and current_suit != self._trump_suit: return
        self._winning_move = move

    def getCardsPlayed(self) -> CardSet:
        return self._cards_played
    
    def _updateCardsPlayed(self, card:Card) -> None:
        self._cards_played.addCard(card)
    
    def playMove(self, move:Move) -> None:
        self._updateLeadSuit(move.getCard())
        self._updateWinningMove(move)
        self._updateMoveLog(move)
        self._updateCardsPlayed(move.getCard())