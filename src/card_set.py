from card import Card
from random import shuffle

class CardSet:

    def __init__(self, cards:set) -> None:
        self._cards = cards

    def getCards(self) -> set:
        return self._cards
    
    def setCards(self, cards:set) -> None:
        self._cards = cards
    
    def getSize(self):
        return len(self._cards)
    
    def addCard(self, card:Card) -> None:
        self._cards.add(card)

    def addCards(self, cards:set) -> None:
        for card in cards: self.addCard(card)

    def removeCard(self, card:Card) -> bool:
        if card not in self._cards: return False
        self._cards.remove(card)
        return True
    
    def removeCards(self, cards:set) -> bool:
        allCardsRemoved = True
        for card in cards: 
            if not self.removeCard(card): allCardsRemoved = False
        return allCardsRemoved
    
    def shuffleCards(self) -> list:
        card_list = list(self._cards)
        shuffle(card_list)
        return card_list

    def clearSet(self) -> None:
        self._cards = set()

    def contains(self, card:Card) -> bool:
        return card in self._cards

    def isEmpty(self) -> bool:
        return self._cards == set()