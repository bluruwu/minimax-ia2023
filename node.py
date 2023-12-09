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
        
    ##Calcula pero no le asigna al nodo!!!
    def calcularHeuristica(self):
        special_coins = self.gameState.specialCoinsLeft
        normal_coins = self.gameState.normalCoinsLeft
        ai_coins = self.gameState.ai.getCoins()
        print(f"Monedas:  {special_coins} Normales {normal_coins} Ai {ai_coins}")
        heuristic_value = special_coins + normal_coins + ai_coins
        self.setHeuristica(heuristic_value)
        return heuristic_value
    
    def setHeuristica(self,number):
        self.heuristica=number

    def getDepth(self):
        return self.depth
    
    def expandir(self,newPosition):
        FutureGame=copy.copy(self.gameState)
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
    