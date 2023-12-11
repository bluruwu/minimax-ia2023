class Player:
    def __init__(self, position) -> None:
        self.position=position
        self.coins=0
        self.tookcoin = False
        self.special_coins = 0
        self.normal_coins = 0
    
    def giveCoin(self,coinValue):
        self.coins+=coinValue
    
    def movePlayer(self,newPosition):
        self.position=newPosition

    def getPosition(self):
        return self.position
    
    def getCoins(self):
        return self.coins
    
    def getSpecialCoins(self):
        return self.special_coins
    
    def getNormalCoins(self):
        return self.normal_coins

    
