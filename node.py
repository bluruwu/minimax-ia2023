from gameState import GameState
from player import Player
import copy
class Node:
    def __init__(self,game : GameState,father ,pos) -> None:
        self.path=[]
        self.father=father
        self.gameState=game
        self.heuristica=self.calcularHeuristica()
        self.accumulatedcost=0
        

    def calcularHeuristica(self):
        #h(x)=(puntosrestantes + puntosIA)/3
        h=(self.gameState.coinPointsLeft+self.gameState.ia.getCoins())/3
        return h
    
    def expandir(self,newPosition,user:bool):
        ##who especifica si en el escenario mueve el usuario o la IA que ser
        hijoMapa=copy.copy(self.gameState)
        hijoPlayer=self.gameState.getPlayer()
        hijoIA=self.gameState.getIA()

        if(user==True):
            oldPosition=hijoPlayer.getPosition()
            hijoMapa[oldPosition[0]][oldPosition[1]]=0
            hijoPlayer.movePlayer(newPosition)
            hijoMapa[newPosition[0]][newPosition[1]]=2

        else:
            oldPosition=hijoIA.getPosition()
            hijoMapa[oldPosition[0]][oldPosition[1]]=0
            hijoIA.movePlayer(newPosition)
            hijoMapa[newPosition[0]][newPosition[1]]=2
            

        hijo=GameState(hijoMapa,hijoPlayer.getPosition(),hijoIA.getPosition())
        

        return hijo
    