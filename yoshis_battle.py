from PIL import Image, ImageTk
import tkinter as tk
import tkinter.font as tkFont
import random

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
    def __init__(self, matriz):
        self.matriz = matriz


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
    return GameState(matriz)

def load_images():
    img_dict = {
        0 : ImageTk.PhotoImage(file="media/none.png"),
        1 : ImageTk.PhotoImage(file="media/coin.png"),
        2 : ImageTk.PhotoImage(file="media/user.png"),
        3 : ImageTk.PhotoImage(file="media/supercoin.png"),
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

