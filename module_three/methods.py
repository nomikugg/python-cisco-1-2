# Metodos y funciones en python
# un Metodo se comporta como una funcion pero su invocacion y uso es diferente.
# Un metodo es una funcion que pertenece a un objeto y se invoca a traves de ese objeto.


# Agregando elementos a una list: append() y  insert()
# append() agrega un elemento al final de la lista

# list.append(value)

# El metodo insert() agrega un elemento en la posicion indicada, no solo al final

# list.insert(location, value)

numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4)

print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)
print(len(numbers))
print(numbers)

#

# Se puede crear una lista vacia, por ejemplo

my_list = []  # Creando una lista vacía.

for i in range(5):
    my_list.append(i + 1)

print(my_list)


my_list = []  # Creando una lista vacía.
for i in range(5):
    my_list.insert(0, i + 1)
    print(my_list)


# Haciendo uso de las listas
# El bucle for es una estructura de control que permite repetir un bloque de instrucciones.


my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]
    my_list.insert(0, i + 1)
    print(my_list)
print(total)

# Segundo aspecto del bucle for
my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i

print(total)


# Intercambio de valores de dos variables

variable_1 = 1
variable_2 = 2

variable_1, variable_2 = variable_2, variable_1
print(variable_1, variable_2)

# Ahora en una lista

my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)


# Ahora con una lista mas larga necestitamos hacer uso de un bucle for
my_list = [10, 1, 8, 3, 5, 4, 3]
length = len(my_list)
for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)


# LABORATORIO: Los fundamentos de las listas. Los beatles
# paso 1
beatles = []

print("Paso 1:", beatles)

# paso 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")


print("Paso 2:", beatles)

# paso 3
for i in range(2):
    beatles.append(input("Ingrese un nuevo miembro de la banda: "))

print("Paso 3:", beatles)

# paso 4
del beatles[3]
del beatles[3]
print("Paso 4:", beatles)

# paso 5
beatles.insert(0, "Ringo Starr")
print("Paso 5:", beatles)


# probando la longitud de la lista
print("Los Fav", len(beatles))


# QUIZ
# Pregunta 1
lst = [1, 2, 3, 4, 5]
lst.insert(1, 6)
del lst[0]
lst.append(1)

print(lst)


# Pregunta 2
lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0

for number in lst:
    add += number
    lst_2.append(add)

print(lst_2)


# Pregunta 3
lst = []
del lst
print(lst)


# Pregunta 4
lst = [1, [2, 3], 4]
print(lst[1])
print(len(lst))
