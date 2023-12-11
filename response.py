from node import Node

def generateResponse(game,difficulty):
    result=minimax(Node(game,None),difficulty,-10000000,10000000,True)
    return result


def minimax(node:Node, depth,alpha,beta,maximizing):
    if(depth==0 or node.gameState.coinPointsLeft==0):
        heuristica = node.calcularHeuristica()
        node.setHeuristica(heuristica)
        return heuristica, None
    if maximizing:
        maxEval=float('-inf')
        best_move = None
        # print("**************************nuevos movs")
        posibleMovements=node.gameState._showAIMovements()
        for n in posibleMovements:
            eval, _=minimax(node.expandir(n),depth-1,alpha,beta,False)
            # print("--------------------")
            # print("eval", eval)
            # print("max eval", maxEval)
            if eval > maxEval:
                maxEval = eval
                best_move = n
            alpha=max_heuristic(alpha,eval)
            if(beta<=alpha):
                break
        return maxEval, best_move
    else:
        minEval=float('inf')
        posibleMovements=node.gameState.showPlayerMovements()
        best_move = None
        for n in posibleMovements:
            eval, _=minimax(node.expandir(n),depth-1,alpha,beta,True)
            if eval < minEval:
                minEval = eval
                best_move = n
            beta=min_heuristic(beta,eval)
            if (beta<=alpha):
                break
        return minEval, best_move



def max_heuristic(heuristica1,heuristica2):
    return max(heuristica1, heuristica2)
    
def min_heuristic(heuristica1,heuristica2):
    return min(heuristica1,heuristica2)