from card_attributes import Suit, Value
from card import Card
from card_set import CardSet
from game_state import GameState

# Class serving as interface for player strategies - add logic to each function to control what a player does when prompted with various actions during the game
class Player:

    # Constructor (do not change)
    def __init__(self) -> None:
        pass

    # Function that should return a suit to serve as the trump suit - called during the game when a Wizard is flipped as the trump suit and the dealer picks the trump suit
    def setTrumpSuit(self, game_state:GameState) -> Suit:
        return Suit.SPADES
    
    # Function that should return a number to serve as the bid for the number of tricks to win in the round - called during the game when the cards are dealt and it is the player's turn to bid
    def makeBid(self, game_state:GameState) -> int:
        return 0
    
    # Function that should return a card to be played on a players turn - the logic for following the lead suit if in hand/playing a Wizard/Jester to avoid following the lead suit needs to be added here
    def playCardFromHand(self, game_state:GameState) -> Card:
        return list(game_state.getHand().getCards())[0]