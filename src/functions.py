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

def ataca_jugador():
            x = int(input( """introduce número del 1 al 10 de fila que quieres disparar, ¡Suerte!! """))
            y = int(input("""introduce número del 1 al 10 de columna que quieres disparar, ¡Suerte!! """))
            # tocados_jugador = 4

            coordenadas_disparo = x, y
 
            print(coordenadas_disparo)
            if (x < 0 or x > 10) or (y < 0 or y > 10):
                print(x)
                print(y)
                print("Número introducido erróneo, te recuerdo que solo pueden ser números del 1 al 10")
                ataca_jugador()
            elif coordenadas_disparo and maquina_barcos[x-1, y-1] == 'O':
                maquina_barcos[x-1][y-1] = 'X'
                tablero_disparos_jugador[x-1][y-1] = 'X'
                print(tablero_disparos_jugador[x-1][y-1])
        
                # tocados_jugador -= tocados_jugador
                # print(tocados_jugador)
                print(f"""Enhorabuena has TOCADO BARCO!!!, está ha sido tú última coordenada {coordenadas_disparo},
                    fila: {x} y columna: {y} te recomiendo que introduzcas la más cercana por si hay suerte de nuevo!! """)
                print("------------------------------------------")
                print("             TURNO JUGADOR")
                print("             TABLERO ATAQUE JUGADOR")
                print("------------------------------------------")
                print(tablero_disparos_jugador, flush=True)
                print("------------------------------------------")
                # tocados_jugador -= tocados_jugador
                # print(tocados_jugador)
                if "Tocado!!":
                    ataca_jugador()
                # jugador dispara y comprueba si hay agua, toca agua y marca '-' en su tablero
                # return "Tocado!!"
            elif coordenadas_disparo and maquina_barcos[x-1, y-1] == ' ':
                maquina_barcos[x-1][y-1] = '-'
                tablero_disparos_jugador[x-1][y-1] = '_'

                print("agua")
                print("------------------------------------------")
                print("             TURNO JUGADOR")
                print("             TABLERO ATAQUE JUGADOR")
                print("------------------------------------------")
                print(tablero_disparos_jugador, flush=True)
                print("------------------------------------------")

                if "agua":
                    print("Turno de jugador")
                    ataca_maquina()
                    # si introduce cordenadas repetidas te avisa, y te informa cual
                    # return "Agua!!"
            elif coordenadas_disparo and maquina_barcos[x-1, y-1] == 'X' or coordenadas_disparo and maquina_barcos[x-1, y-1] == '-':
                print(f"""vaya parece que ya has atacado esta coordenada antes {coordenadas_disparo},
                    fila: {x} y columna: {y}, por favor, introduce nuevas coordenadas""")
                print("------------------------------------------")
                print("             TURNO JUGADOR")
                print("             TABLERO ATAQUE JUGADOR")
                print("------------------------------------------")
                print(tablero_disparos_jugador, flush=True)
                print("------------------------------------------")

                ataca_jugador()
                

def ataca_maquina():
    cordenadas_disparo_aleatoria= np.random.randint(0,10, size=2)
    x_maquina = cordenadas_disparo_aleatoria[0]
    y_maquina = cordenadas_disparo_aleatoria[1]
    cordenadas_disparo_maquina = x_maquina, y_maquina
    print(cordenadas_disparo_maquina )

#jugador dispara y comprueba si hay barco, toca barco y marca 'X'en el tablero de barcos maquina y en el de disparos del jugador, 
#actualiza contador de barcos de maquina -1
    if cordenadas_disparo_maquina and jugador_barcos[x_maquina][y_maquina] == 'O':
        jugador_barcos[x_maquina][y_maquina]= 'X'
        tablero_disparos_maquina[x_maquina][y_maquina] = 'X'
        print("------------------------------------------")
        print("             TURNO MAQUINA")
        print("             TABLERO ATAQUE MAQUINA")
        print("------------------------------------------")
        print(tablero_disparos_maquina, flush=True)
        tocados_maquina -= tocados_maquina
        print(tocados_maquina)
        
        if "Tocado barco!! " :
            print("------------------------------------------")
            print("             TURNO MAQUINA")
            print("             TABLERO ATAQUE MAQUINA")
            print("------------------------------------------")
            print(tablero_disparos_maquina, flush=True)
            ataca_maquina()
   
#jugador dispara y comprueba si hay agua, toca agua y marca '-' en su tablero
    elif cordenadas_disparo_maquina and jugador_barcos[x_maquina][y_maquina] == ' ':
        jugador_barcos[x_maquina][y_maquina] = '-'
        tablero_disparos_maquina[x_maquina][y_maquina] = '_'
        print("------------------------------------------")
        print("             TURNO MAQUINA")
        print("             TABLERO ATAQUE MAQUINA")
        print("------------------------------------------")
        print(tablero_disparos_maquina, flush=True)
        print("agua")
        if "agua":
            ataca_jugador()
        
    elif cordenadas_disparo_maquina and jugador_barcos[x_maquina,y_maquina] == 'X' or cordenadas_disparo_maquina and jugador_barcos[x_maquina,y_maquina] == '-':
        #print(f"vaya parece que ya has atacado esta coordenada {cordenadas_disparo_maquina}, fila: {x_maquina} y columna: {y_maquina}, introduce nuevas coordenadas")
        ataca_maquina()
    
    elif maquina_barcos["O" in maquina_barcos]== False:
        game_over =  "O" in maquina_barcos
        print("HAS GANADO, NO QUEDAN BARCOS POR DERRIBAR")
        return game_over