from PIL import ImageTk
from tkinter import IntVar
import tkinter as tk
import tkinter.font as tkFont
import random
from gameState import GameState
import copy
from response import generateResponse
from tkinter import simpledialog
from tkinter import messagebox
difficulty = None
selected_difficulty = None
def read_game():
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
        #Blocked Mov
        5 : ImageTk.PhotoImage(file="media/blockedmov.png")
    }
    return img_dict

def calculate_index(movement):
    row, col = movement
    index = row * 8 + col
    return index

def moveAI(board, boxes, newPosition, cpu_coins):
    img_dict = load_images()
    oldPosition = board.ai.getPosition()
    oldIndex = calculate_index(oldPosition)
    newIndex = calculate_index(newPosition)
    #was i in a coin position?
    if(board.ai.tookcoin):
        #show that the movement is now blocked because i took a coin
        boxes[oldIndex].configure(image=img_dict[5])
        boxes[oldIndex].img = img_dict[5]
        #Now this position is blocked
        board.blocked_movements.append(oldPosition)
    else:
        #just show blank image cause it wasnt in coin
        boxes[oldIndex].configure(image=img_dict[0])
        boxes[oldIndex].img = img_dict[0]
    board.willigetcoin(newPosition, board.ai)
    boxes[newIndex].configure(image=img_dict[4])
    boxes[newIndex].img = img_dict[4]
    board._moveAIPlayer(newPosition)
    #Update ai coins visually
    cpu_coins.set(f"Cpu: {board.ai.getCoins()}")


def movePlayer(newPosition, board, boxes, user_coins):
    img_dict = load_images() #Load Images
    oldPosition = board.player.getPosition() 
    #get index of positions in the boxes array
    oldIndex = calculate_index(oldPosition)
    newIndex = calculate_index(newPosition)
    #was i in a coin position?
    if(board.player.tookcoin):
        #show that the movement is now blocked because i took a coin
        boxes[oldIndex].configure(image=img_dict[5])
        boxes[oldIndex].img = img_dict[5]
        #Now this position is blocked
        board.blocked_movements.append(oldPosition)
    else:
        #just show blank image cause i wasnt in coin
        boxes[oldIndex].configure(image=img_dict[0])
        boxes[oldIndex].img = img_dict[0]
    #Am i going to get a coin in this new position?
    board.willigetcoin(newPosition, board.player)
    #put player image in new position
    boxes[newIndex].configure(image=img_dict[2])
    boxes[newIndex].img = img_dict[2]
    board.movePlayer(newPosition)
    #Update user coins visually
    user_coins.set(f"Tú: {board.player.getCoins()}")
    #Next move
    update(board, boxes, user_coins, cpu_coins)
    

def update(board, boxes, user_coins, cpu_coins):   
    #MOVE AI
    #Generate best move
    _ , positionAI = generateResponse(copy.deepcopy(board),difficulty)
    moveAI(board, boxes, positionAI, cpu_coins)

    for box in boxes:
        box.unbind("<Button-1>") 
    #all possible movements
    allmovements = board.showPlayerMovements()
    for movement in allmovements:
        index = calculate_index(movement)
        boxes[index].bind("<Button-1>", lambda event, newPosition = movement: movePlayer(newPosition, board, boxes, user_coins))            


def selectDifficulty():
    global difficulty, selected_difficulty
    difficulty_str = simpledialog.askstring("Dificultad", "Selecciona la dificultad (1: Fácil, 2: Normal, 3: Difícil):")
    
    if difficulty_str is not None:
        try:
            difficulty = int(difficulty_str)
            if 1 <= difficulty <= 3:
                franja = tk.Frame(root, bg="lightgray", height=207)
                franja.config(width=415)
                franja.place(relx=0.5, rely=0.44, anchor="center")
                
                if difficulty == 1:
                    button_text = "Easy"
                    difficulty_value = 2
                if difficulty == 2:
                    button_text = "Normal"
                    difficulty_value = 4
                elif difficulty == 3:
                    button_text = "Hard"
                    difficulty_value = 6


                
                    
                changeDifficulty(franja, difficulty_value)
                
                
                global selected_difficulty
                selected_difficulty = difficulty
                franja.destroy()
                print(difficulty)
            else:
                # Handle other difficulty values as needed
                    button_text = "Unknown"
                    difficulty_value = None
                    print("ERRORRRRR")
                    messagebox.showwarning("Advertencia", "Valor de dificultad no reconocido. Se ha establecido como desconocido.")
 
        except ValueError:
            # Handle the case where the input is not a valid integer
            print("Por favor, ingresa un número válido.")
#Set grid interface
def board_interface(board, frame):
    box_labels = []
    img_dict = load_images()
    for i in range(8):
        for j in range(8):
            numero = board.matriz[i][j]
            imagen = img_dict[numero]
            label = tk.Label(frame, image=imagen, borderwidth=1, relief="solid",)
            label.img = img_dict[numero]
            label.grid(row=i, column=j)
            box_labels.append(label) 
    return box_labels

def points(frame, board):
    font_size = tkFont.Font(size=14)
    #Title of frame
    title = tk.Label(frame, text="Puntuación --->", font=tkFont.Font(size=30))
    title.grid(column=0, row=0, rowspan=2, sticky="w")
    #Listen player getCoins()
    user_coins = IntVar()
    user = tk.Label(frame, textvariable=user_coins, font=font_size)
    user_coins.set(f"Tú: {board.player.getCoins()}")
    user.grid(sticky="e", column=1, row=1, padx=(80,0))
    #Listen AI getCoins()
    cpu_coins = IntVar()
    cpu = tk.Label(frame, textvariable=cpu_coins, font=font_size)
    cpu_coins.set(f"Cpu: {board.ai.getCoins()}")
    cpu.grid(sticky="e", column=1, row=0, padx=(80,0))
    return user_coins, cpu_coins

def changeDifficulty(franja,number):
    global difficulty
    difficulty = number
    franja.destroy()

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
    root.columnconfigure(0, weight=1)
    #Select difficulty
    selectDifficulty()
    #Points
    frame_points = tk.Frame(root)
    frame_points.pack(side="bottom", fill="both")
    #Play
    boxes = board_interface(board, frame_board)
    user_coins, cpu_coins = points(frame_points, board)
    update(board, boxes, user_coins, cpu_coins)

    root.mainloop()












