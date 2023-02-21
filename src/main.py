
import functions as fn
import numpy as np


  
jugador_barcos = fn.tablero_barcos_jugador()


maquina_barcos = fn.tablero_barcos_maquina()


if fn.ataca_jugador() == False:
    print("Enhorabuena jugador has ganado")
    tablero =np.full((10, 10), " ")
    maquina_barcos = tablero
elif fn.ataca_maquina() == False:
    tablero =np.full((10, 10), " ")
    print("Enhorabuena maquina has ganado")
    jugador_barcos = tablero
