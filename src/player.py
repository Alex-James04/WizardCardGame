from card_attributes import Suit
from card import Card

class Player:

    def __init__(self) -> None:
        pass

    def setTrumpSuit(self) -> Suit:
        return Suit.NULL
    
    def makeBid(self) -> int:
        return 0
    
    def playCardFromHand(self) -> Card:
        return Card()