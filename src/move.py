from card import Card
from player import Player

class Move:

    def __init__(self, player:Player=Player(), card:Card=Card()) -> None:
        self._player = player
        self._card = card

    def getPlayer(self) -> Player:
        return self._player
    
    def getCard(self) -> Card:
        return self._card