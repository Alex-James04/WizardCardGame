class Bid:

    def __init__(self, goal:int) -> None:
        self._goal = goal
        self._made = 0

    def getGoal(self) -> int:
        return self._goal
    
    def getMade(self) -> int:
        return self._made

    def incrementMadeBids(self) -> None:
        self._made += 1

    def isUnder(self) -> int:
        return self._goal > self._made

    def isMet(self) -> int:
        return self._goal == self._made
    
    def isOver(self) -> int:
        return self._goal < self._made