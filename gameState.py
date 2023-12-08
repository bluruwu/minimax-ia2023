from player import Player
import copy
class GameState:
    #4 CPU
    #2 User
    def __init__(self, matriz,playerPosition,aiPosition):
        self.coinPointsLeft=24
        self.player=Player(playerPosition)
        self.ai=Player(aiPosition)
        self.matriz = matriz
        self.blocked_movements = []
        self.whoWon='NotYet'
        self.tookcoin = False
        self

    def calculateWhoWon(self):
        player=self.player.getCoins()
        ai=self.ai.getCoins()
        if(ai>player):
            return 'JUGADOR DOS'
        elif(player>ai):
            return 'JUGADOR UNO'
        else:
            return 'EMPATE'
         
    
    def movePlayer(self,newPosition):
        if((self.matriz[newPosition[0]][newPosition[1]]==1) or (self.matriz[newPosition[0]][newPosition[1]]==3)):
           self.player.giveCoin(self.matriz[newPosition[0]][newPosition[1]])
           self.coinPointsLeft-=self.matriz[newPosition[0]][newPosition[1]]
           if(self.coinPointsLeft==0):
               self.whoWon=self.calculateWhoWon()
        oldPosition=self.player.getPosition()
        self.matriz[oldPosition[0]][oldPosition[1]]=0
        self.player.movePlayer(newPosition)
        self.matriz[newPosition[0]][newPosition[1]]=2

    def _moveAIPlayer(self,newPosition):

        ##newPosition=generateResponse(copy.copy(self.matriz),copy.copy(self.player),copy.copy(self.ai),self._showAIMovements())
        if((self.matriz[newPosition[0]][newPosition[1]]==1) or (self.matriz[newPosition[0]][newPosition[1]]==3)):
            self.ai.giveCoin(self.matriz[newPosition[0]][newPosition[1]])
            self.coinPointsLeft-=self.matriz[newPosition[0]][newPosition[1]]
            if(self.coinPointsLeft==0):
                self.whoWon=self.calculateWhoWon()
        oldPosition=self.ai.getPosition()
        self.matriz[oldPosition[0]][oldPosition[1]]=0
        self.ai.movePlayer(newPosition)
        self.matriz[newPosition[0]][newPosition[1]]=4

    def showPlayerMovements(self):
        ##Posibles movimientos en L
        patterns=[[-1,-2],[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2]]
        movements=[]
        position=self.player.getPosition()
        ai_position = list(self.ai.getPosition())
        for n in patterns:
            newPosition=[position[0]+n[0],position[1]+n[1]]
            if((newPosition[0]>=0 and newPosition[1]>=0) and (newPosition[0]<=7 and newPosition[1]<=7) and newPosition!=ai_position):
                movements.append(newPosition)
        return movements
    
    def _showAIMovements(self):
        patterns=[[-1,-2],[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2]]
        movements=[]
        position=self.ai.getPosition()
        player_position= list(self.player.getPosition())
        for n in patterns:
            newPosition=[position[0]+n[0],position[1]+n[1]]
            if((newPosition[0]>=0 and newPosition[1]>=0) and (newPosition[0]<=7 and newPosition[1]<=7) and newPosition!=player_position):
                movements.append(newPosition)
        return movements
    
    def getPlayer(self):
        return copy.copy(self.player)
    
    def getAI(self):
        return copy.copy(self.ai)
    
    def getMap(self):
        return copy.copy(self.matriz)
    
    def willigetcoin(self, newPosition):
        if((self.matriz[newPosition[0]][newPosition[1]]==1) or (self.matriz[newPosition[0]][newPosition[1]]==3)):
            self.tookcoin= True
        else:
            self.tookcoin = False


    

