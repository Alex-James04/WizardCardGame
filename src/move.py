from card import Card
from player import Player

class Move:

    def __init__(self, card:Card=Card(), player:Player=Player()) -> None:
        self._card = card
        self._player = player

    def getCard(self) -> Card:
        return self._card

    def getPlayer(self) -> Player:
        return self._player