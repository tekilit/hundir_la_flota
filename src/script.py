import random
import numpy as np


def barcos_a_tablero(num_barcos, eslora):


    while num_barcos > 0:

    # 'N' - 'S' - 'E' - 'O'
        orient = random.choice(['N', 'S', 'E', 'O'])

    # Posicion inicial del barco
        current_pos = np.random.randint(10, size=2)

        fila = current_pos[0]
        col = current_pos[1]
        num_barcos = num_barcos


        # Recogemos las 4 posiciones colindantes a current_pos
        coors_posiN = tablero[fila:fila - eslora:-1, col]
        coors_posiE = tablero[fila, col: col + eslora]
        coors_posiS = tablero[fila:fila + eslora, col]
        coors_posiO = tablero[fila, col: col - eslora:-1]

    # Comprobamos si esas posiciones son validas
    # Orientacion Norte
        if orient == 'N' and 0 <= fila - eslora < 10  and 'O' not in coors_posiN:
            tablero[fila:fila - eslora:-1, col] = 'O'
            num_barcos = num_barcos -1


    # Orientacion Este
        elif orient == 'E' and 0 <= col + eslora < 10  and 'O' not in coors_posiE:
            tablero[fila, col: col + eslora] = 'O'
            num_barcos = num_barcos -1


    # Orientacion Sur
        elif orient == 'S' and 0 <= fila + eslora < 10  and 'O' not in coors_posiS:
            tablero[fila:fila + eslora, col] = 'O'
            num_barcos = num_barcos -1


        # Orientacion Oeste
        elif orient == 'O' and 0 <= col - eslora < 10 and   'O' not in coors_posiO:
            tablero[fila, col: col - eslora:-1] = 'O'
            num_barcos = num_barcos -1

    # No cumple con las dimensiones del tablero, o hay un barco ahi
    # Probamos con otra coordenada
        else:
            continue
    return tablero
    
tablero =np.full((10, 10), " ")
def tablero_barcos_jugador():

    barcos_3e = barcos_a_tablero(2,3)
    barcos_4e = barcos_a_tablero(4,1)
    barcos_2e = barcos_a_tablero(3,2)
    barcos_1e = barcos_a_tablero(1,4)
    
    return tablero

    
jugador_barcos = tablero_barcos_jugador()



tablero =np.full((10, 10), " ")
def tablero_barcos_maquina():

        barcos_3e = barcos_a_tablero(2,3)
        barcos_4e = barcos_a_tablero(4,1)
        barcos_2e = barcos_a_tablero(3,2)
        barcos_1e = barcos_a_tablero(1,4)

        return tablero

maquina_barcos = tablero_barcos_maquina()



#Aqui levanta todos los tableros
tablero =np.full((10, 10), " ")


tablero_disparos_jugador = np.full((10,10), " ")
print("""                  """)
print("""
┌┬┐┌─┐┌┐ ┬  ┌─┐┬─┐┌─┐  ┌┐ ┌─┐┬─┐┌─┐┌─┐┌─┐   ┬┬ ┬┌─┐┌─┐┌┬┐┌─┐┬─┐
 │ ├─┤├┴┐│  ├┤ ├┬┘│ │  ├┴┐├─┤├┬┘│  │ │└─┐   ││ ││ ┬├─┤ │││ │├┬┘
 ┴ ┴ ┴└─┘┴─┘└─┘┴└─└─┘  └─┘┴ ┴┴└─└─┘└─┘└─┘  └┘└─┘└─┘┴ ┴─┴┘└─┘┴└─ """ )
print("""                  """)
print("------------------------------------------")
print("              BARCOS JUGADOR")
print("------------------------------------------")
print(jugador_barcos)
print("------------------------------------------")
print("             TABLERO ATAQUE JUGADOR")
print("------------------------------------------")
print(tablero_disparos_jugador)


tablero =np.full((10, 10), " ")



tablero_disparos_maquina =  np.full((10,10), " ")
print("""                  """)
print("""
┌┬┐┌─┐┌┐ ┬  ┌─┐┬─┐┌─┐  ┌┐ ┌─┐┬─┐┌─┐┌─┐┌─┐  ┌┬┐┌─┐┌─┐ ┬ ┬┬┌┐┌┌─┐
 │ ├─┤├┴┐│  ├┤ ├┬┘│ │  ├┴┐├─┤├┬┘│  │ │└─┐  │││├─┤│─┼┐│ │││││├─┤
 ┴ ┴ ┴└─┘┴─┘└─┘┴└─└─┘  └─┘┴ ┴┴└─└─┘└─┘└─┘  ┴ ┴┴ ┴└─┘└└─┘┴┘└┘┴ ┴ """)
print("""                  """)
print("------------------------------------------")
print("              BARCOS MAQUINA")
print("------------------------------------------")
print(maquina_barcos)
print("------------------------------------------")
print("             TABLERO ATAQUE MAQUINA")
print("------------------------------------------")
print(tablero_disparos_maquina)