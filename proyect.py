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
