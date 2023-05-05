

def crear_tablero(tamaño):
    import numpy as np
    return np.full((tamaño, tamaño), " ")

def crear_barco_random(eslora, tamaño):
    import random
    barco_random = []
    fila_random = random.randint(0,9)
    columna_random = random.randint(0,9)
    barco_random.append((fila_random,columna_random))
    orient = random.choice(["N","S","E","O"])

    while len(barco_random) < eslora:
        if orient == "O":
            columna_random = columna_random - 1 
        elif orient == "E":
            columna_random = columna_random + 1
        elif orient == "N":
            fila_random = fila_random - 1
        elif orient == "S":
            fila_random = fila_random + 1

        if fila_random not in range(tamaño) or columna_random not in range(tamaño):
            fila_random = random.randint(0,9)
            columna_random = random.randint(0,9)
            barco_random = []
            barco_random.append((fila_random,columna_random))
        else:
            barco_random.append((fila_random,columna_random))

        # print(barco_random)
    return barco_random


def colocar_barco(barco, tablero):
    for casilla in barco:
        tablero[casilla] = "O"


#def ordenar_barcos(lista_barcos)

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