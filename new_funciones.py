

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
        tablero[casilla] = "B"

def disparo_aleatorio(tablero_oponente):
    import random
    import numpy as np
    fila_random = np.random.randint(0, 9)
    columna_random = np.random.randint(0, 9)
    casilla = ((fila_random,columna_random))
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
    función para disparar. Modificamos tablero según barco o agua.
    """
    import variables as vr
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
    funcion para enseñar el tablero con los disparos que hemos hecho.
    """
    import variables as vr
    tablero_modificado = tablero.copy()
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] == "B":
                tablero_modificado[i][j] = " "
            elif tablero[i][j] == "M":
                tablero_modificado[i][j] == "M"
            elif tablero[i][j] == "X":
                tablero_modificado[i][j] == "X"
            elif tablero[i][j]== " ":
                tablero_modificado[i][j] = " "   
    return tablero_modificado


def jugar(turno_actual):
    import variables as vr
    while True:
        print ("Turno de", turno_actual)
        
        if turno_actual == vr.jugador:
            print("Tablero maquina:")
            print(show_tablero(vr.tablero_maquina))
        else:
            print("Tablero jugador:")
            print(vr.tablero_jugador)

        if turno_actual == vr.jugador:
            
            fila = int(input("A que fila deseas disparar?"))
            columna = int(input("A que columna deseas disparar?"))
            casilla = (fila, columna)
            resultado = disparar(casilla, vr.tablero_maquina)

            if resultado == True:
                vr.vidas_maquina -= 1
                if vr.vidas_maquina == 0:
                    print("Has hundido toda la flota!")
                    break
            elif resultado == False:
                turno_actual = vr.maquina   
        else:
            resultado = disparo_aleatorio(vr.tablero_jugador)

            if resultado == True:
                print("Tu barco ha sido tocado!")
                vr.vidas_jugador -= 1
                if vr.vidas_jugador == 0:
                    print("Has perdido, todos tus barcos han sido hundidos.")
                    break
            elif resultado == False:
                turno_actual = vr.jugador

        

       

    
        