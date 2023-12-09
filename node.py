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
        #h(x)=(puntosrestantes + puntosIA)/3
        h=(self.gameState.coinPointsLeft+self.gameState.ai.getCoins())/3
        return h
    
    def setHeuristica(self,number):
        self.heuristica=number

    def getDepth(self):
        return self.depth
    
    def expandir(self,newPosition):
        FutureGame=copy.copy(self.gameState)
        ##if(user==True):
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
    