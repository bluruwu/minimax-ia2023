from player import Player
import copy
class GameState:
    #4 CPU
    #2 User
    def __init__(self, matriz,playerPosition,aiPosition):
        self.coinPointsLeft=24
        self.specialCoinsLeft= 4
        self.normalCoinsLeft= 12
        self.player=Player(playerPosition)
        self.ai=Player(aiPosition)
        self.matriz = matriz
        self.blocked_movements = []
        self.whoWon='NotYet'
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
        if((self.matriz[newPosition[0]][newPosition[1]])==1):
            self.normalCoinsLeft-=1
            self.player.normal_coins+=1
        elif ((self.matriz[newPosition[0]][newPosition[1]])==3):
            self.specialCoinsLeft-=1
            self.player.special_coins+=1
    
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
        if((self.matriz[newPosition[0]][newPosition[1]])==1):
            self.normalCoinsLeft-=1
            self.ai.normal_coins+=1

        elif ((self.matriz[newPosition[0]][newPosition[1]])==3):
            self.specialCoinsLeft-=1
            self.ai.special_coins+=1

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
        movements = filter(lambda x: x not in self.blocked_movements, movements)
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
        movements = filter(lambda x: x not in self.blocked_movements, movements)
        return movements
    
    def getPlayerPosition(self):
        return self.player.getPosition()
    
    def getAIPosition(self):
        return self.ai.getPosition()

    def willigetcoin(self, newPosition, user):
        if((self.matriz[newPosition[0]][newPosition[1]]==1) or (self.matriz[newPosition[0]][newPosition[1]]==3)):
            user.tookcoin= True
        else:
            user.tookcoin = False


    

