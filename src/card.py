from card_attributes import Suit, Value

class Card:
    
    def __init__(self, suit:Suit=Suit.NULL, value:Value=Value.NULL) -> None:
        self._suit = suit
        self._value = value

    def getSuit(self) -> Suit:
        return self._suit
    
    def getValue(self) -> Value:
        return self._value
    
    def isJester(self) -> bool:
        return self._value is Value.JESTER
    
    def isWizard(self) -> bool:
        return self._value is Value.WIZARD