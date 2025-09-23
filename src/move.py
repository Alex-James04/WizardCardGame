from card import Card

class Move:

    def __init__(self, player_index:int=-1, card:Card=Card()) -> None:
        self._player_index = player_index
        self._card = card

    def getPlayerIndex(self) -> int:
        return self._player_index
    
    def getCard(self) -> Card:
        return self._card