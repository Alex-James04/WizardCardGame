from card import Card
from random import shuffle

# Class defining unordered collection of cards (set) 
class CardSet:

    # Constructor - requires passing a set of card objects
    def __init__(self, cards:set) -> None:
        self._cards = cards

    # Get cards as set of card objects
    def getCards(self) -> set:
        return self._cards
    
    # Set cards attribute as set of card objects
    def setCards(self, cards:set) -> None:
        self._cards = cards
    
    # Get number of cards in the set
    def getSize(self) -> int:
        return len(self._cards)
    
    # Add a card to the set
    def addCard(self, card:Card) -> None:
        self._cards.add(card)

    # Add cards to the set
    def addCards(self, cards:set) -> None:
        for card in cards: self.addCard(card)

    # Remove a card from the set
    def removeCard(self, card:Card) -> bool:
        if card not in self._cards: return False
        self._cards.remove(card)
        return True
    
    # Remove cards from the set
    def removeCards(self, cards:set) -> bool:
        allCardsRemoved = True
        for card in cards: 
            if not self.removeCard(card): allCardsRemoved = False
        return allCardsRemoved
    
    # Get a shuffled list of the cards in the set - used for dealing cards to players
    def getShuffledList(self) -> list:
        card_list = list(self._cards)
        shuffle(card_list)
        return card_list

    # Remove all cards from the set
    def clearSet(self) -> None:
        self.setCards(set())

    # Check if a card is in the set of cards
    def contains(self, card:Card) -> bool:
        return card in self._cards

    # Check if the set of cards is empty
    def isEmpty(self) -> bool:
        return self._cards == set()