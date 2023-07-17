import funciones as fn 
import variables as vr
2
print("Bienvenido a hundir la flota! Comienza el juego.")
print("El primer turno es del jugador. \n Debes escoger la fila y columna en la que deseas disparar. Si tocas barco vuelves a tener turno, \nsi fallas  das en agua, pasamos el turno a la maquina. Suerte!")


for barco in vr.lista_maquina:
    tablero = fn.colocar_barco(barco, vr.tablero_maquina)

print("Vamos a colocar tus barcos:")
for barco in vr.barcos_jugador:
    tablero = fn.colocar_barco(barco, vr.tablero_jugador)

print(vr.tablero_jugador)

fn.jugar(vr.jugador)
