import new_funciones as fn 
import variables as vr

print("Bienvenido a hundir la flota! Comienza el juego.")

for barco in vr.lista_maquina:
    tablero = fn.colocar_barco(barco, vr.tablero_maquina)

print("Vamos a colocar tus barcos:")
for barco in vr.barcos_jugador:
    tablero = fn.colocar_barco(barco, vr.tablero_jugador)

print(vr.tablero_jugador)

fn.jugar(vr.jugador)