class EstadoJuego:
    def __init__(self, matriz):
        self.matriz = matriz


def leer_juego():
    with open('logic/game.txt', 'r') as juego:
        lineas = juego.readlines()
    matriz = [list(map(int, linea.split())) for linea in lineas]
    return EstadoJuego(matriz)

def jugar(tablero):
    print(tablero.matriz)


if __name__ == "__main__":
    tablero = leer_juego()
    jugar(tablero)