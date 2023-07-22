my_list = [8, 10, 6, 2, 4]  # lista a ordenar
swapped = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.

while swapped:
    swapped = False  # no hay intercambios hasta ahora
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # ¡ocurrió el intercambio!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)


# Ahora con un codigo mas interactivo, con numero ingresados por teclado
my_list = []
swapped = True
num = int(input("¿Cuántos elementos deseas ordenar?: "))

for i in range(num):
    val = float(input("Ingresa un elemento de la lista: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nOrdenada:")
print(my_list)


# Sin embargo, python ya contiene sus propios metodos de ordenamiento, como el metodo sort()

my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)


# Tambienn podemos ordenar listas de cadenas
# Tambien existe un metodo para invertis la lista, reverse()
lst = [5, 3, 1, 2, 4]
print(lst)

lst.reverse()
print(lst)  # output: [4, 2, 1, 3, 5]


# QUIZ

# pregunta 1
lst = ["D", "F", "A", "Z"]
lst.sort()

print(lst)


# Pregunta 2
a = 3
b = 1
c = 2

lst = [a, c, b]
lst.sort()

print(lst)
# la salida es [1, 2, 3]


# Pregunta 3
a = "A"
b = "B"
c = "C"
d = " "
# e = 1, sort() no puede ordenar cadenas y numeros al mismo tiempo
e = "$"
lst = [a, b, c, d, e]
lst.reverse()

print(lst)

# Curiosidad
# ¿Qué sucede si intentas ordenar una lista que contiene cadenas y números? ¿Puedes predecir el resultado?
lst.sort()
print(lst)
