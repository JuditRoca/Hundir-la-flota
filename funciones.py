import numpy as np
import random
import variables as vr

import numpy as np
import random

def crear_tablero(tamaño):
    """
    Crea un tablero vacío del tamaño especificado.

    Args:
        tamaño (int): Tamaño del tablero.

    Returns:
        np.array: Tablero vacío.
    """
    return np.full((tamaño, tamaño), " ")

def barco_rand(eslora, tamaño):
    """
    Genera las coordenadas aleatorias para ubicar un barco en el tablero.

    Args:
        eslora (int): Longitud del barco.
        tamaño (int): Tamaño del tablero.

    Returns:
        list: Lista de coordenadas del barco.
    """
    barco_random = []
    fila_random = random.randint(0, 9)
    columna_random = random.randint(0, 9)
    barco_random.append((fila_random, columna_random))
    orient = random.choice(["N", "S", "E", "O"])

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
            fila_random = random.randint(0, 9)
            columna_random = random.randint(0, 9)
            barco_random = []
            barco_random.append((fila_random, columna_random))
        else:
            barco_random.append((fila_random, columna_random))

    return barco_random

def colocar_barco(barco, tablero):
    """
    Coloca un barco en el tablero modificando las casillas correspondientes.

    Args:
        barco (list): Lista de coordenadas del barco.
        tablero (np.array): Tablero de juego.
    """
    for casilla in barco:
        tablero[casilla] = "B"

def disparo_aleatorio(tablero_oponente):
    """
    Realiza un disparo aleatorio en el tablero del oponente.

    Args:
        tablero_oponente (np.array): Tablero del oponente.

    Returns:
        bool: True si se tocó un barco, False si se dio en el agua.
    """
    fila_random = np.random.randint(0, 9)
    columna_random = np.random.randint(0, 9)
    casilla = ((fila_random, columna_random))

    if tablero_oponente[casilla] == "B":
        tablero_oponente[casilla] = "X"
        print("Tocado")
        return True
    elif tablero_oponente[casilla] == " ":
        tablero_oponente[casilla] = "M"
        print("Has dado en agua, cambio de turno")
        return False

def disparar(casilla, tablero_oponente):
    """
    Realiza un disparo en una casilla específica del tablero del oponente.

    Args:
        casilla (tuple): Coordenadas de la casilla.
        tablero_oponente (np.array): Tablero del oponente.

    Returns:
        bool: True si se tocó un barco, False si se dio en el agua.
    """
    if tablero_oponente[casilla] == "B":
        tablero_oponente[casilla] = "X"
        print("Has tocado barco! Vuelves a disparar.")
        return True
    else:
        tablero_oponente[casilla] = "M"
        print("Has dado en mar, cambiamos de turno")
        return False

def show_tablero(tablero):
    """
    Modifica el tablero para mostrar los disparos realizados.

    Args:
        tablero (np.array): Tablero de juego.

    Returns:
        np.array: Tablero modificado.
    """
    tablero_modificado = tablero.copy()
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] == "B":
                tablero_modificado[i][j] = " "
            elif tablero[i][j] == "M":
                tablero_modificado[i][j] == "M"
            elif tablero[i][j] == "X":
                tablero_modificado[i][j] == "X"
            elif tablero[i][j] == " ":
                tablero_modificado[i][j] = " "
    return tablero_modificado

def jugar(turno_actual):
    """
    Lógica principal del juego Hundir la Flota.

    Args:
        turno_actual (str): Jugador actual.

    Returns:
        str: Mensaje de victoria o derrota.
    """
    while True:
        print("Turno de", turno_actual)

        if turno_actual == vr.jugador:
            print("Tablero maquina:")
            print(show_tablero(vr.tablero_maquina))
            print("A la maquina le queda", vr.vidas_maquina, "vidas.")
        else:
            print("Tablero jugador:")
            print(vr.tablero_jugador)
            print("Al jugador le queda", vr.vidas_jugador, "vidas.")

        if turno_actual == vr.jugador:
            fila = int(input("A qué fila deseas disparar?"))
            columna = int(input("A qué columna deseas disparar?"))
            casilla = (fila, columna)
            resultado = disparar(casilla, vr.tablero_maquina)

            if resultado:
                vr.vidas_maquina -= 1
                if vr.vidas_maquina == 0:
                    return "Has hundido toda la flota!"
            else:
                turno_actual = vr.maquina
        else:
            resultado = disparo_aleatorio(vr.tablero_jugador)

            if resultado:
                print("Tu barco ha sido tocado!")
                vr.vidas_jugador -= 1
                if vr.vidas_jugador == 0:
                    return "Has perdido, todos tus barcos han sido hundidos."
            else:
                turno_actual = vr.jugador


        

       

    
        