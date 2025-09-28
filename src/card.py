from card_attributes import Suit, Value

# Card class comprised of a suit and a value
class Card:
    
    # Constructor
    def __init__(self, suit:Suit=Suit.NULL, value:Value=Value.NULL) -> None:
        self._suit = suit
        self._value = value

    # Get card suit
    def getSuit(self) -> Suit:
        return self._suit
    
    # Get card value
    def getValue(self) -> Value:
        return self._value
    
    # Check if card is a jester
    def isJester(self) -> bool:
        return self._value is Value.JESTER
    
    # Check if card is a wizard
    def isWizard(self) -> bool:
        return self._value is Value.WIZARD