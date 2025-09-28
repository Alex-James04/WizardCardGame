from card import Card

# Class storing a player-card pair for when a player makes a move on their turn
class Move:

    # Constructor
    def __init__(self, player_index:int=-1, card:Card=Card()) -> None:
        self._player_index = player_index
        self._card = card

    # Get the player's index in the main player list
    def getPlayerIndex(self) -> int:
        return self._player_index
    
    # Get the card played
    def getCard(self) -> Card:
        return self._card