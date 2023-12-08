from node import Node
from typing import List
def generateResponse(game,difficulty):
    heuristica=0
    queue=[]
    depth=1
    currentNode=Node(game,None)
    queue.append(currentNode)
    expandedNodes=[]
    currentGame=game
    if(difficulty=='easy'):
        return generateEasyResponse(game)
    while(len(queue)!=0):
        expandedNodes.append(queue[0])
        queue.pop(0)
        ##si la profundidad es menor a 4
        if(currentNode.getDepth()<=4):
            posibleMovements=currentGame._showAIMovements()
            for n in range(len(posibleMovements)):
                newNode=currentNode.expandir(posibleMovements[n])
                ##Aqui debe ir una funcion que determina si la heuristica del nodo debe ser mayor o menos que la que hay acumulada
                podar=False
                if(not podar):
                    queue.add(n,newNode)
                else:
                    ##Sale inmediatamente de la iteracion
                    break
                # Añadir a la queue
        
    ###Funciones auxiliares
    def minmax(queue,type):
        if(type=='min'):
            return min(queue)
        elif (type=='max'):
            return max(queue)
        else:
            return print('Se debe ingresar un parametro "min"/"max"')

    return [0,0]

def max(arrayNode:List[Node]):
    arrayNode.sort(key=lambda x:x.heuristica)
    return arrayNode[0].heuristica

def min(arrayNode:List[Node]):
    arrayNode.sort(key=lambda x:x.heuristica,reverse=True)
    return arrayNode[0].heuristica


def generateEasyResponse(game):
    heuristica=0
    queue=[]

    currentNode=Node(game,None)
    queue.append(currentNode)
    currentGame=game
    posibleMovements=currentGame._showAIMovements()
    for n in range(len(posibleMovements)):
            newNode=currentNode.expandir(posibleMovements[n])
            ##Aqui debe ir una funcion que determina si la heuristica del nodo debe ser mayor o menos que la que hay acumulada
            tempH=newNode.calcularHeuristica()
            if(tempH>=heuristica):
                heuristica=tempH
                queue.add(n,newNode)
            else:
                ##Sale inmediatamente de la iteracion
                break
    queue.pop(0)
    response=max(queue)

    
    return response