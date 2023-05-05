import new_funciones as fn 
import variables as vr

print("Bienvenido a hundir la flota! Comienza el juego.")

print("Este es tu tablero" , vr.tablero_jugador)


print("Vamos a colocar tus barcos:")

fn.colocar_barco(vr.barco_1_jugador, vr.tablero_jugador)
fn.colocar_barco(vr.barco_2_jugador, vr.tablero_jugador)
fn.colocar_barco(vr.barco_3_jugador, vr.tablero_jugador)
fn.colocar_barco(vr.barco_4_jugador, vr.tablero_jugador)
fn.colocar_barco(vr.barco_5_jugador, vr.tablero_jugador)
fn.colocar_barco(vr.barco_6_jugador, vr.tablero_jugador)
fn.colocar_barco(vr.barco_7_jugador, vr.tablero_jugador)

print(vr.tablero_jugador)







