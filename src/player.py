from card_attributes import Suit, Value
from card import Card
from card_set import CardSet
from game_state import GameState

class Player:

    def __init__(self) -> None:
        pass

    def setTrumpSuit(self, game_state:GameState) -> Suit:
        return Suit.SPADES
    
    def makeBid(self, game_state:GameState) -> int:
        return 0
    
    def playCardFromHand(self, game_state:GameState) -> Card:
        return list(game_state.getHand().getCards())[0]