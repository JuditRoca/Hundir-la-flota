

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

def disparo_aleatorio(tablero_oponente):
    import random
    import numpy as np
    while True:
        fila_random = np.random.randint(0, 9)
        columna_random = np.random.randint(0, 9)
        casilla = ((fila_random,columna_random))
        if tablero_oponente[casilla] == "O":
            tablero_oponente[casilla] = "X"
            print("Tocado")
        else:
            tablero_oponente[casilla] = "-"
            print("Has dado en agua, cambio de turno")
        return

def disparar(casilla, tablero_oponente):
    import variables as vr
    while True:
        
        if tablero_oponente[casilla] == "O":
            tablero_oponente[casilla] = "X"
            print("Tocado")
        else:
            tablero_oponente[casilla] = "-"
            print("Has dado en agua, cambio de turno")
            
    return tablero_oponente
    
def jugar(turno_actual):
    import variables as vr
    while True:
        print("Turno de ", turno_actual)
        if turno_actual == vr.jugador:
            fila= int(input("Que fila deseas atacar?"))
            columna = int(input("Que columna deseas atacar?"))
            tablero_oponente = vr.tablero_maquina
            casilla = fila, columna  
            disparar(casilla, tablero_oponente)
        