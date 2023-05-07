import variables as vr
import new_funciones as fn
import clases as cl
disparos_iniciales = 10
jugador = "Jugador"
maquina = "Maquina"

tablero_jugador = fn.crear_tablero(10)
tablero_maquina = fn.crear_tablero(10)

vidas_jugador = 20
vidas_maquina = 20
#BARCOS JUGADOR
b1_jgr = cl.lancha()
b2_jgr = cl.lancha()
b3_jgr = cl.lancha()
b4_jgr = cl.lancha()
b5_jgr = cl.catamaran()
b6_jgr= cl.catamaran()
b7_jgr= cl.catamaran()
b8_jgr = cl.rapido()
b9_jgr = cl.rapido()
b10_jgr = cl.portacontenedores()

barcos_jugador = [fn.barco_rand(b1_jgr.tamaño, b1_jgr.tablero), fn.barco_rand(b2_jgr.tamaño, b2_jgr.tablero), fn.barco_rand(b3_jgr.tamaño, b3_jgr.tablero), fn.barco_rand(b4_jgr.tamaño, b4_jgr.tablero), fn.barco_rand(b5_jgr.tamaño, b5_jgr.tablero), fn.barco_rand(b6_jgr.tamaño, b6_jgr.tablero), fn.barco_rand(b7_jgr.tamaño, b7_jgr.tablero), fn.barco_rand(b8_jgr.tamaño, b8_jgr.tablero), fn.barco_rand(b9_jgr.tamaño, b9_jgr.tablero), fn.barco_rand(b10_jgr.tamaño, b10_jgr.tablero)]

#BARCOS MAQUINA
barco_1_maq = fn.barco_rand(1,10)  #1ºbarco 1 eslora
barco_2_maq = fn.barco_rand(1,10)
barco_3_maq = fn.barco_rand(1,10)
barco_4_maq = fn.barco_rand(1,10)
barco_5_maq = fn.barco_rand(2,10)  #1º barco 2 esloras
barco_6_maq = fn.barco_rand(2,10)   
barco_7_maq = fn.barco_rand(2,10)
barco_8_maq = fn.barco_rand(3,10)  #1º barco 3 esloras
barco_9_maq = fn.barco_rand(3,10)
barco_10_maq = fn.barco_rand(4,10)  #barco 4 esloras

lista_maquina = [barco_1_maq, barco_2_maq, barco_3_maq, barco_4_maq, barco_5_maq, barco_6_maq, barco_7_maq, barco_8_maq, barco_10_maq]