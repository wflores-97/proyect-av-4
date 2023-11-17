import os

def crear_laberinto(laberinto_str):
    return [list(fila) for fila in laberinto_str.split("\n")]

def limpiar_pantalla():
        _ = os.system('cls')

def mostrar_laberinto(laberinto):
    for fila in laberinto:
        print("".join(fila))

def main_loop(laberinto, posicion_inicial, posicion_final):
    px, py = posicion_inicial

    while (px, py) != posicion_final:
        laberinto[px][py] = 'P'
        limpiar_pantalla()
        mostrar_laberinto(laberinto)

        # Leer la tecla del usuario
        direccion = input("Ingrese la dirección (arriba, abajo, izquierda, derecha): ")

        # Calcular la nueva posición tentativa
        nueva_px, nueva_py = px, py

        if direccion == "arriba" and px > 0 and laberinto[px - 1][py] != '#':
            nueva_px -= 1
        elif direccion == "abajo" and px < len(laberinto) - 1 and laberinto[px + 1][py] != '#':
            nueva_px += 1
        elif direccion == "izquierda" and py > 0 and laberinto[px][py - 1] != '#':
            nueva_py -= 1
        elif direccion == "derecha" and py < len(laberinto[0]) - 1 and laberinto[px][py + 1] != '#':
            nueva_py += 1

        # Actualizar la posición y restaurar la posición anterior
        laberinto[px][py] = '.'
        px, py = nueva_px, nueva_py

if __name__ == "__main__":
    laberinto_str = """..###################
    ....#...............#
    #.#.#####.#########.#
    #.#...........#.#.#.#
    #.#####.#.###.#.#.#.#
    #...#.#.#.#.....#...#
    #.#.#.#######.#.#####
    #.#...#.....#.#...#.#
    #####.#####.#.#.###.#
    #.#.#.#.......#...#.#
    #.#.#.#######.#####.#
    #...#...#...#.#.#...#
    ###.#.#####.#.#.###.#
    #.#...#.......#.....#
    #.#.#.###.#.#.###.#.#
    #...#.#...#.#.....#.#
    ###.#######.###.###.#
    #.#.#.#.#.#...#.#...#
    #.#.#.#.#.#.#.#.#.#.#
    #.....#.....#.#.#.#.#
    ###################.."""

    laberinto = crear_laberinto(laberinto_str)
    posicion_inicial = (0, 0)
    posicion_final = (len(laberinto) - 1, len(laberinto[0]) - 1)

    main_loop(laberinto, posicion_inicial, posicion_final)


import os
import random

class Juego:
    def __init__(self, mapa, posicion_inicial, posicion_final):
        self.mapa = mapa
        self.posicion_inicial = posicion_inicial
        self.posicion_final = posicion_final

    def mostrar_mapa(self):
        for fila in self.mapa:
            print(fila)

    def mover(self, direccion):
        # Lógica para moverse en la dirección proporcionada
        pass

    def verificar_victoria(self):
        # Lógica para verificar si el jugador ha alcanzado la posición final
        pass

# Subclase JuegoArchivo que hereda de Juego
class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas):
        # Seleccionar un archivo aleatorio de la carpeta de mapas
        nombre_archivo = random.choice(os.listdir(path_a_mapas))
        path_completo = os.path.join(path_a_mapas, nombre_archivo)

        # Llamar al constructor de la clase base (Juego) con los datos del archivo
        super().__init__(*self.leer_mapa_desde_archivo(path_completo))

    def leer_mapa_desde_archivo(self, path_archivo):
        with open(path_archivo, 'r') as archivo:
            # Leer las dimensiones del mapa y las coordenadas iniciales y finales
            dimensiones = archivo.readline().strip().split(',')
            filas, columnas = int(dimensiones[0]), int(dimensiones[1])
            inicio = archivo.readline().strip().split(',')
            fin = archivo.readline().strip().split(',')

            # Leer las filas del mapa
            mapa = [archivo.readline().strip() for _ in range(filas)]

        return mapa, (int(inicio[0]), int(inicio[1])), (int(fin[0]), int(fin[1]))

# Uso de las clases en el main
if __name__ == "__main__":
    # Crear una instancia de JuegoArchivo con la carpeta de mapas como argumento
    juego_archivo = JuegoArchivo("carpeta_de_mapas")

    # Acceder a los atributos de la instancia
    print("Mapa:")
    juego_archivo.mostrar_mapa()
    print("Posición Inicial:", juego_archivo.posicion_inicial)
    print("Posición Final:", juego_archivo.posicion_final)
