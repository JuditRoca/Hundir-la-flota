
class Barco:
    def __init__(self, tamaño=1, tablero=10):
        """
        Inicializa una instancia de la clase Barco.

        Args:
            tamaño (int): Tamaño del barco.
            tablero (int): Tamaño del tablero.
        """
        self.tamaño = tamaño
        self.tablero = tablero

    def barco_rand(self):
        """
        Genera las coordenadas aleatorias para ubicar el barco en el tablero.

        Returns:
            list: Lista de coordenadas del barco.
        """
        import random
        barco_random = []
        fila_random = random.randint(0,9)
        columna_random = random.randint(0,9)
        barco_random.append((fila_random,columna_random))
        orient = random.choice(["N","S","E","O"])

        while len(barco_random) < self.tamaño:
            if orient == "O":
                columna_random = columna_random - 1 
            elif orient == "E":
                columna_random = columna_random + 1
            elif orient == "N":
                fila_random = fila_random - 1
            elif orient == "S":
                fila_random = fila_random + 1

            if fila_random not in range(self.tablero) or columna_random not in range(self.tablero):
                fila_random = random.randint(0,9)
                columna_random = random.randint(0,9)
                barco_random = []
                barco_random.append((fila_random,columna_random))
            else:
                barco_random.append((fila_random,columna_random))

            # print(barco_random)
        return barco_random
