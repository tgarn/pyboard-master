class marble:
    def __init__(self, startingPosition, number):
        self.position = startingPosition
        self.marbleNumber = number
    def updatePosition(self, updatedPosition):
        self.position = updatedPosition
    
    def getPosition(self):
        return self.position