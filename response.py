from node import Node

def generateResponse(game,difficulty):
    result=minimax(Node(game,None),difficulty,-10000000,10000000,True)
    print(result)
    return result


def minimax(node:Node, depth,alpha,beta,maximizing):
    if(depth==0 or node.gameState.coinPointsLeft==0):
        return node.calcularHeuristica()
    if(maximizing==True):
        maxEval=float('-inf')
        posibleMovements=node.gameState._showAIMovements()
        for n in posibleMovements:
            eval=minimax(node.expandir(n),depth-1,alpha,beta,False)
            maxEval=max(alpha,eval)
            alpha=max(alpha,eval)
            if(beta<=alpha):
                break
        return maxEval
    else:
        minEval=float('inf')
        posibleMovements=node.gameState.showPlayerMovements()
        for n in posibleMovements:
            eval=minimax(node.expandir(n),depth-1,alpha,beta,True)
            minEval=min(minEval,eval)
            beta=min(beta,eval)
            if (beta<=alpha):
                break
        return minEval



def max(heuristica1,heuristica2):
    if(heuristica1>heuristica2):
        return heuristica1
    else:
        return heuristica2
    
def min(heuristica1,heuristica2):
    if(heuristica1<heuristica2):
        return heuristica1
    else:
        return heuristica2