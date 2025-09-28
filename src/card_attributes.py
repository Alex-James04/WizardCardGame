from enum import Enum

# Enum class storing card suits
class Suit(Enum):
    NULL = "null"
    HEARTS = "hearts"
    DIAMONDS = "diamonds"
    SPADES = "spades"
    CLUBS = "clubs"

# Enum class storing card values
class Value(Enum):
    NULL = 0
    JESTER = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14
    WIZARD = 15