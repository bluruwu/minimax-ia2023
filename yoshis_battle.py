from PIL import Image, ImageTk
import tkinter as tk
import tkinter.font as tkFont
import random
from player import Player
from response import generateResponse
import copy

free_space = [
    (0, 2), (0, 3), (0, 4), (0, 5),
    (1, 1), (1, 2), (1, 3), (1, 4), (1,5), (1,6),
    (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2,7),
    (3, 0), (3, 1), (3, 2), (3, 5), (3, 6), (3,7),
    (4, 0), (4, 1), (4, 2), (4, 5), (4, 6), (4,7),
    (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5,7),
    (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6),
    (7, 2), (7, 3), (7, 4), (7, 5)
]

class GameState:
    #4 CPU
    #2 User
    def __init__(self, matriz,playerPosition,iaPosition):
        self.coinPointsLeft=24
        self.player=Player(playerPosition)
        self.ia=Player(iaPosition)
        self.matriz = matriz
        self.whoWon='NotYet'

    def calculateWhoWon(self):
        player=self.player.getCoins()
        ia=self.ia.getCoins()
        if(ia>player):
            return 'JUGADOR DOS'
        elif(player>ia):
            return 'JUGADOR UNO'
        else:
            return 'EMPATE'
         
    
    def movePlayer(self,position):
        if((self.matriz[position[0]][position[1]]==1) or (self.matriz[position[0]][position[1]]==3)):
           self.player.giveCoin(self.matriz[position[0]][position[1]])
        self.matriz[position[0]][position[1]]=0
        self.player.movePlayer(position)
        self.matriz[position[0]][position[1]]=2

    def moveIAPlayer(self):
        ##Aqui pone a la IA a cocinar su jugada nasty
        position=generateResponse(copy.copy(self.matriz),copy.copy(self.player),copy.copy(self.ia))
        if((self.matriz[position[0]][position[1]]==1) or (self.matriz[position[0]][position[1]]==3)):
           self.ia.giveCoin(self.matriz[position[0]][position[1]])
           coinsleft-=self.matriz[position[0]][position[1]]
           if(self.coinPointsLeft==0):
               self.whoWon=self.calculateWhoWon()
        self.matriz[position[0]][position[1]]=0
        self.ia.movePlayer(position)
        self.matriz[position[0]][position[1]]=4

    def showPlayerMovements(self):
        ##Posibles movimientos en L
        patterns=[[-2,-1],[-2,1],[2,1],[2,-1]]
        movements=[]
        position=self.player.getPosition()
        for n in patterns:
            newPosition=[position[0]+n[0],position[1]+n[1]]
            if((newPosition[0]>=0 and newPosition[1]>=0) and (newPosition[0]<=7 and newPosition[1]<=7)):
                movements.append(newPosition)
        return movements
    



    ##Not sure if the methods below will be necessary
    def showIAMovements(self):
        movements=[]
        pos=self.ia.getPosition()
        #upleft
        movements[0]=[pos[0]-2,pos[1]-1]
        #upright
        movements[1]=[pos[0]-2,pos[1]+1]
        #dowmright
        movements[2]=[pos[0]+2,pos[1]+1]
        #downleft
        movements[3]=[pos[0]+2,pos[1]-1]
        return movements
    
    def getPlayer(self):
        return copy.copy(self.player)
    
    def getIA(self):
        return copy.copy(self.ia)
    
    def getMap(self):
        return copy.copy(self.matriz)
    




def read_game():
    with open('initGame.txt', 'r') as juego:
        lines = juego.readlines()
    matriz = [list(map(int, line.split())) for line in lines]
    #Place cpu in random place without coins
    cpu_place = random.choice(free_space)
    matriz[cpu_place[0]][cpu_place[1]] = 4
    free_space.remove(cpu_place) # Don't use same place for user
    #Place user in random place without coins
    user_place = random.choice(free_space)
    matriz[user_place[0]][user_place[1]] = 2
    return GameState(matriz,user_place,cpu_place)

def load_images():
    img_dict = {
        #BlankSpace
        0 : ImageTk.PhotoImage(file="media/none.png"),
        #NormalCoin
        1 : ImageTk.PhotoImage(file="media/coin.png"),
        #HumanPlayer
        2 : ImageTk.PhotoImage(file="media/user.png"),
        #SuperCoin
        3 : ImageTk.PhotoImage(file="media/supercoin.png"),
        #IAPlayer
        4 : ImageTk.PhotoImage(file="media/cpu.png"),
    }
    return img_dict

def play(board):
    return 1

def board_interface(board, frame):
    img_dict = load_images()
    for i in range(8):
        for j in range(8):
            numero = board.matriz[i][j]
            imagen = img_dict[numero]
            label = tk.Label(frame, image=imagen, borderwidth=1, relief="solid",)
            label.img = img_dict[numero]
            label.grid(row=i, column=j)

def points(frame):
    font_size = tkFont.Font(size=16)
    tk.Label(frame, text="Puntuación", font=font_size, anchor="w", background="blue", justify="center").pack(fill="both")
    tk.Label(frame, text="aaaaa", font=font_size, anchor="w", background="red", justify="left").pack(fill="both")


if __name__ == "__main__":
    #InitGame
    board = read_game()
    

    #Root interface
    root = tk.Tk()
    root.title ("Yoshi's battle")
    root.resizable(False,False)
    root.iconbitmap("media/user.ico")
    #Frame Grid
    frame_board = tk.Frame(root)
    frame_board.pack()

    #Points
    frame_points = tk.Frame(root)
    frame_points.pack(side="bottom", fill="both")
    #Play
    board_interface(board, frame_board)
    points(frame_points)
    play(board)

    root.mainloop()

