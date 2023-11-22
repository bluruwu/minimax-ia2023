import tkinter as tk

class EstadoJuego:
    #5 CPU
    #6 User
    def __init__(self, matriz):
        self.matriz = matriz


def leer_juego():
    with open('games/game.txt', 'r') as juego:
        lineas = juego.readlines()
    matriz = [list(map(int, linea.split())) for linea in lineas]
    return EstadoJuego(matriz)

def jugar(tablero):
    print(tablero.matriz)

def actualizar_interfaz(tablero):
    for i in range(8):
        for j in range(8):
            label = tk.Label(root, text=str(tablero.matriz[i][j]), borderwidth=1, relief="solid", width=5, height=2)
            label.grid(row=i, column=j)

if __name__ == "__main__":
    tablero = leer_juego()
    root = tk.Tk()
    root.title ("Yoshi's battle")
    jugar(tablero)
    actualizar_interfaz(tablero)
    root.mainloop()

