from node import Node
def generateResponse(game,player,ia,posibleMovements):
    priorityQueue=[]
    queuetwo=[]
    ##diseñar euristica
    currentNode=Node(game,None)
    priorityQueue.push(currentNode)
    while(priorityQueue):
        movs=currentNode.gameState._showIAMovements
        for n in movs:
            futureGame=currentNode.expandir(n,False)
            newNode=Node(futureGame,currentNode)
            priorityQueue.append(newNode)
        
        
    


    coordinates=[0,0]
    return coordinates