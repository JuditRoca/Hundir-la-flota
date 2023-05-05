import random
import variables as vr



      
def hacer_tablero(tamaño):
    import numpy as np
    return np.full((tamaño,tamaño), " ")

def colocar_barco(barco, tablero):
    for casilla in barco:
        tablero[casilla] = "O"
    return tablero

def disparar(casilla, tablero):
    import variables as vr
    while "O" in tablero:
        casilla = input("Donde deseas disparar?")
        if tablero[casilla] == "O":
            tablero[casilla] = "X"
            print("Tocado")
        else:
            tablero[casilla] = "-"
            print("Has dado en agua, cambio de turno")
        return 

