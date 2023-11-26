from player import Player
from response import generateResponse
import copy
class GameState:
    #4 CPU
    #2 User
    def __init__(self, matriz,playerPosition,iaPosition):
        self.coinPointsLeft=24
        self.player=Player(playerPosition)
        self.ia=Player(iaPosition)
        self.matriz = matriz
        self.whoWon='NotYet'
        self

    def calculateWhoWon(self):
        player=self.player.getCoins()
        ia=self.ia.getCoins()
        if(ia>player):
            return 'JUGADOR DOS'
        elif(player>ia):
            return 'JUGADOR UNO'
        else:
            return 'EMPATE'
         
    
    def movePlayer(self,newPosition):
        if((self.matriz[newPosition[0]][newPosition[1]]==1) or (self.matriz[newPosition[0]][newPosition[1]]==3)):
           self.player.giveCoin(self.matriz[newPosition[0]][newPosition[1]])
           self.coinsleft-=self.matriz[newPosition[0]][newPosition[1]]
           if(self.coinPointsLeft==0):
               self.whoWon=self.calculateWhoWon()


        oldPosition=self.player.getPosition()
        self.matriz[oldPosition[0]][oldPosition[1]]=0
        self.player.movePlayer(newPosition)
        self.matriz[newPosition[0]][newPosition[1]]=2
        self._moveIAPlayer()

    def _moveIAPlayer(self):
        ##Aqui pone a la IA a cocinar su jugada nasty
        newPosition=generateResponse(copy.copy(self.matriz),copy.copy(self.player),copy.copy(self.ia),self._showIAMovements())
        if((self.matriz[newPosition[0]][newPosition[1]]==1) or (self.matriz[newPosition[0]][newPosition[1]]==3)):
           self.ia.giveCoin(self.matriz[newPosition[0]][newPosition[1]])
           self.coinsleft-=self.matriz[newPosition[0]][newPosition[1]]
           if(self.coinPointsLeft==0):
               self.whoWon=self.calculateWhoWon()
        oldPosition=self.ia.getPosition()
        self.matriz[oldPosition[0]][oldPosition[1]]=0
        self.ia.movePlayer(newPosition)
        self.matriz[newPosition[0]][newPosition[1]]=4

    def showPlayerMovements(self):
        ##Posibles movimientos en L
        patterns=[[-2,-1],[-2,1],[2,1],[2,-1]]
        movements=[]
        position=self.player.getPosition()
        for n in patterns:
            newPosition=[position[0]+n[0],position[1]+n[1]]
            if((newPosition[0]>=0 and newPosition[1]>=0) and (newPosition[0]<=7 and newPosition[1]<=7)):
                movements.append(newPosition)
        return movements
    



    ##Not sure if the methods below will be necessary
    def _showIAMovements(self):
        patterns=[[-2,-1],[-2,1],[2,1],[2,-1]]
        movements=[]
        position=self.player.getPosition()
        for n in patterns:
            newPosition=[position[0]+n[0],position[1]+n[1]]
            if((newPosition[0]>=0 and newPosition[1]>=0) and (newPosition[0]<=7 and newPosition[1]<=7)):
                movements.append(newPosition)
        return movements
    
    def getPlayer(self):
        return copy.copy(self.player)
    
    def getIA(self):
        return copy.copy(self.ia)
    
    def getMap(self):
        return copy.copy(self.matriz)
    

