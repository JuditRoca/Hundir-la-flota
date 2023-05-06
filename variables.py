import variables as vr
import new_funciones as fn
disparos_iniciales = 10
jugador = "Jugador"
maquina = "Maquina"

tablero_jugador = fn.crear_tablero(10)
tablero_maquina = fn.crear_tablero(10)

vidas_jugador = 20
vidas_maquina = 20
#BARCOS JUGADOR
barco_1_jugador = fn.crear_barco_random(1,10)
barco_2_jugador = fn.crear_barco_random(1,10)
barco_3_jugador = fn.crear_barco_random(1,10)
barco_4_jugador = fn.crear_barco_random(1,10)
barco_5_jugador = fn.crear_barco_random(2,10)
barco_6_jugador = fn.crear_barco_random(2,10)
barco_7_jugador = fn.crear_barco_random(2,10)
barco_8_jugador = fn.crear_barco_random(3,10)
barco_9_jugador = fn.crear_barco_random(3,10)
barco_10_jugador = fn.crear_barco_random(4,10)


barcos_jugador = [barco_1_jugador, barco_2_jugador, barco_3_jugador, barco_4_jugador, barco_5_jugador, barco_6_jugador, barco_7_jugador, barco_8_jugador, barco_9_jugador, barco_10_jugador]


#BARCOS MAQUINA
barco_1_maquina = fn.crear_barco_random(1,10)
barco_2_maquina = fn.crear_barco_random(1,10)
barco_3_maquina = fn.crear_barco_random(1,10)
barco_4_maquina = fn.crear_barco_random(1,10)
barco_5_maquina = fn.crear_barco_random(2,10)
barco_6_maquina = fn.crear_barco_random(2,10)
barco_7_maquina = fn.crear_barco_random(2,10)
barco_8_maquina = fn.crear_barco_random(3,10)
barco_9_maquina = fn.crear_barco_random(3,10)
barco_10_maquina = fn.crear_barco_random(4,10)

lista_maquina = [barco_1_maquina, barco_2_maquina, barco_3_maquina, barco_4_maquina, barco_5_maquina, barco_6_maquina, barco_7_maquina, barco_8_maquina, barco_10_maquina]