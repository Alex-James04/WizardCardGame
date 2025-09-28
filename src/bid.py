# Bid class that tracks a player's number of bid and made tricks
class Bid:

    # Constructor
    def __init__(self, goal:int) -> None:
        self._goal = goal
        self._made = 0

    # Get the player's goal tricks
    def getGoal(self) -> int:
        return self._goal
    
    # Get the player's made tricks
    def getMade(self) -> int:
        return self._made

    # Increment the player's made bids - used in gameplay when a player wins a trick
    def incrementMadeTricks(self) -> None:
        self._made += 1

    # Check if the player is under their bid
    def isUnder(self) -> int:
        return self._goal > self._made

    # Check if the player is exactly on their bid
    def isMet(self) -> int:
        return self._goal == self._made
    
    # Check if the player is over their bid
    def isOver(self) -> int:
        return self._goal < self._made