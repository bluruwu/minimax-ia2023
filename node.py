from gameState import GameState
import copy

class Node:
    def __init__(self,game : GameState,father,depth=0,nodeType='max') -> None:
        self.depth=depth
        self.path=[]
        self.father=father
        self.gameState=game
        self.heuristica=None
        self.nodeType=nodeType
        
    def calcularHeuristica(self):
        ai_special = self.gameState.ai.getSpecialCoins()
        ai_normal = self.gameState.ai.getNormalCoins()
        player_special = self.gameState.player.getSpecialCoins()
        player_normal = self.gameState.player.getNormalCoins()
        heuristic_value = (ai_special * 3 + ai_normal) - (player_special * 3 + player_normal)
        self.setHeuristica(heuristic_value)
        return heuristic_value
    
    def setHeuristica(self,number):
        self.heuristica=number

    def getDepth(self):
        return self.depth
    
    def expandir(self,newPosition):
        FutureGame=copy.deepcopy(self.gameState)
        if(self.nodeType=='min'):
            FutureGame.movePlayer(newPosition)  
        else:
            FutureGame._moveAIPlayer(newPosition)  

        if self.nodeType=='max':
            newNodeType='min'
        else:
            newNodeType='max'
        hijo=Node(FutureGame,self,self.depth+1,newNodeType)
        return hijo
    