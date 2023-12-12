from gameState import GameState
import copy
import math

def sigmoid(x):
    return 1/(1 + math.exp(-x))  

def normalize(value, min_value, max_value):
    return (value - min_value) / (max_value - min_value)

class Node:
    def __init__(self,game : GameState,father,depth=0,nodeType='max') -> None:
        self.depth=depth
        self.path=[]
        self.father=father
        self.gameState=game
        self.heuristica=None
        self.nodeType=nodeType

    def calcularHeuristica(self):
        iapoints = self.gameState.ai.getCoins()
        playerpoints = self.gameState.player.getCoins()
        heuristic_value = sigmoid((iapoints - playerpoints) + (0.5/ self.depth+1))
        normalized_heuristic = normalize(heuristic_value, 0, 1)
        self.setHeuristica(normalized_heuristic)
        return normalized_heuristic
    
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
    