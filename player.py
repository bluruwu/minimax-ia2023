class Player:
    def __init__(self, position) -> None:
        self.position=position
        self.coins=0
    
    def giveCoin(self,coinValue):
        self.coins+=coinValue
    
    def movePlayer(self,newPosition):
        self.position=newPosition

    def getPosition(self):
        return self.position
    
    def getCoins(self):
        return self.coins
    
