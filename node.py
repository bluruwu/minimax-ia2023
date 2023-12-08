from gameState import GameState
import copy
class Node:
    def __init__(self,game : GameState,father,depth=1,nodeType='max') -> None:
        self.depth=depth
        self.path=[]
        self.father=father
        self.gameState=game
        self.heuristica=self.calcularHeuristica()
        self.accumulatedcost=0
        ##si es un nodo Min o un nodo Max
        self.nodeType=nodeType
        

    def calcularHeuristica(self):
        #h(x)=(puntosrestantes + puntosIA)/3
        h=(self.gameState.coinPointsLeft+self.gameState.ai.getCoins())/3
        return h
    def getDepth(self):
        return self.depth
    def expandir(self,newPosition,user:bool):
        ##who especifica si en el escenario mueve el usuario o la IA que ser
        hijoMapa=copy.copy(self.gameState)
        hijoPlayer=self.gameState.getPlayer()
        hijoIA=self.gameState.getIA()

        ##if(user==True):
        if(self.nodeType=='min'):
            oldPosition=hijoPlayer.getPosition()
            hijoMapa[oldPosition[0]][oldPosition[1]]=0
            hijoPlayer.movePlayer(newPosition)
            hijoMapa[newPosition[0]][newPosition[1]]=2

        else:
            oldPosition=hijoIA.getPosition()
            hijoMapa[oldPosition[0]][oldPosition[1]]=0
            hijoIA.movePlayer(newPosition)
            hijoMapa[newPosition[0]][newPosition[1]]=2
            
        if self.nodeType=='max':
            newNodeType='min'
        else:
            newNodeType='max'
        hijo=Node(GameState(hijoMapa,hijoPlayer.getPosition(),hijoIA.getPosition()),self,self.depth+1,newNodeType)
        

        return hijo
    