Proyecto Hundir la flota ⛴️ 💣 💥
Realizado por:

Noya Fernández del Cotero
Silvia Quintana


Este documento recoge el primer proyecto para el bootcamp de Data science.
Vamos a usar numpy , funciones, objetos , condicionales y bucles en python.
¿Cómo funciona el juego?


Creamos dos jugadores: tú y la máquina


En un tablero de 10 x 10 vamos a colocar nuestra flota de barcos

4 barcos de 1 posición de eslora
3 barcos de 2 posiciones de eslora
2 barcos de 3 posiciones de eslora
1 barco de 4 posiciones de eslora

El juego comienza cuando , jugador y maquina colocan sus flotas en el tablero de manera aleatoria.

Los barcos solo se pueden colocar horizontal o verticalemnte ( en nuetra version no hay diagonales)
El juego consiste en : Disparar , comprobar el estado de la flota y responder al ataque disparando , hasta que hundamos toda la flota del adversario.

El jugador elige las coordinadas de ataque ( x ,y) , la maquina atacará aleatoriamente .
Si aciertas en disparo , repites turno , si fallas cambia el turno.

El juego se acaba en el momento que todos los barcos están hundidos .