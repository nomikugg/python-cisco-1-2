# Pregunta 1
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[0]

print(list_3)
# imprime ['C']


# pregunta 2
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2

print(list_3)
# Imprime ['B', 'C']
# porque al eliminar list_2, no se elimina list_3, ya que list_3 es una copia de list_2, no de list_1 y list_2 es una copia de list_1 y list_3 es una copia de list_2 y no de list_1 por lo tanto no se elimina list_3 al eliminar list_2 y al eliminar list_1 se elimina list_2 y list_3 porque son copias de list_1 y list_2 respectivamente.


# Pregunta 3
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[:]

print(list_3)
# Imprime vacio, []


# preunta 4
list_1 = ["A", "B", "C"]
list_2 = list_1[:]
list_3 = list_2[:]

del list_1[0]
del list_2[0]

print(list_3)


# pregunta 5
my_list = [1, 2, "in", True, "ABC"]

print(1 in my_list)  # output True
print("A" not in my_list)  # output True
print(3 not in my_list)  # output True
print(False in my_list)  # output False
