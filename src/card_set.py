from card import Card

class CardSet:

    def __init__(self, cards:set=set()) -> None:
        self._cards = cards

    def getCards(self) -> set:
        return self._cards
    
    def setCards(self, cards:set=set()) -> None:
        self._cards = cards
    
    def getSize(self):
        return len(self._cards)
    
    def addCard(self, card:Card=Card()) -> None:
        self._cards.add(card)

    def addCards(self, cards:set=set()) -> None:
        for card in cards: self.addCard(card)

    def removeCard(self, card:Card=Card()) -> bool:
        if card not in self._cards: return False
        self._cards.remove(card)
        return True
    
    def removeCards(self, cards:set=set()) -> bool:
        allCardsRemoved = True
        for card in cards: 
            if not self.removeCard(card): allCardsRemoved = False
        return allCardsRemoved

    def clearSet(self) -> None:
        self._cards = set()

    def contains(self, card:Card) -> bool:
        return card in self._cards

    def isEmpty(self) -> bool:
        return not bool(self._cards)