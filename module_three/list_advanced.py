# Listas de listas

import random
squares = [x ** 2 for x in range(10)]
print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

twos = [2 ** i for i in range(8)]
print(twos)
# [1, 2, 4, 8, 16, 32, 64, 128]
# otro ejemplo


# Este ejemplo es una combinacion de dos listas
# crea  una lista de numeros del 0 al 19
# y muestra los numeros impares
squares = [x for x in range(20)]
odds = [x for x in squares if x % 2 != 0]
print(odds)


# Arreglos de dos dimensiones
# Ejemplo
# board = [[EMPTY for i in range(8)] for j in range(8)]
board = [[i for i in range(8)] for j in range(8)]
# print(board)
# Creando un tablero de ajedrez
# board = []

# agregamos las torres al tablero de ajedrez en las posiciones 0,0 y 0,7 y 7,0 y 7,7 respectivamente
board[0][0] = 'ROOK'
board[0][7] = 'ROOK'
board[7][0] = 'ROOK'
board[7][7] = 'ROOK'
# agregamos un caballo
board[4][2] = "KNIGHT"
print(board)


# Profundicemos en la naturaleza multidimensional de las listas. Para encontrar cualquier elemento de una lista bidimensional, debes usar dos coordenadas:

# Una vertical (número de fila).
# Una horizontal (número de columna).


# Imagina que desarrollas una pieza de software para una estación meteorológica automática. El dispositivo registra la temperatura del aire cada hora y lo hace durante todo el mes. Esto te da un total de 24 × 31 = 744 valores. Intentemos diseñar una lista capaz de almacenar todos estos resultados.

# Primero, debes decidir qué tipo de datos sería adecuado para esta aplicación. En este caso, sería mejor un float, ya que este termómetro puede medir la temperatura con una precisión de 0.1 ℃.

# Luego tomarás la decisión arbitraria de que las filas registrarán las lecturas cada hora exactamente (por lo que la fila tendrá 24 elementos) y cada una de las filas se asignará a un día del mes (supongamos que cada mes tiene 31 días, por lo que necesita 31 filas). Aquí está el par apropiado de comprensiones (h es para las horas, d para el día):
temps = [[0.0 for h in range(24)] for d in range(31)]
print(temps)
temps_list = [[random.uniform(12.0, 32.0).__round__(2)
              for i in range(24)] for j in range(31)]
print(temps_list)
# random_ls = []
# print(random.uniform(12.0, 32.0))

highest = -100.0

for day in temps_list:
    for temp in day:
        if temp > highest:
            highest = temp

print("La temperatura más alta fue:", highest)


hot_days = 0

for day in temps_list:
    if day[11] > 20.0:
        hot_days += 1

print(hot_days, "fueron los días calurosos.")
