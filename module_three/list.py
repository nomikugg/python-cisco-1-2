list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)
# Podemos observar que imprime [2], esto es porque las listas son mutables, es decir, que se pueden modificar
# en otras palabras esta enlazada a la misma direccion de memoria.


# Para evitar esto podemos hacer uso de la funcion copy() o de los dos puntos :

list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)
# La parte de : produce una lista completamente nueva, que es una copia de la original.
# contiene start:end, donde start es inclusivo y end es exclusivo.


my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)


# Rebanadas con indices negativos.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)


# si estart es negativo imprimira vacio
my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]
print(new_list)
# []

# podemos omitir el valor de start o end.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)

my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list)
# asi como tambien podemos omitir ambos, copiara toda la lista
# si solo tiene start, copiara desde start hasta el final
# si solor tiene end, copiara desde el inicio hasta end


# mas de la funcion DEL
# Tambien puede eliminar rebanadas, mas de un elemento a la vez
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)

# y Aplica las mismas condiciones de start:end

my_list = [10, 8, 6, 4, 2]
del my_list
print(my_list)  # da error
# pero en cambio

my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)  # da vacio
