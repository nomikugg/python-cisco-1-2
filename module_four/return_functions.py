# Funciones que retornan un valor o no


#   RETURN sin una expresion
def happy_new_year(wishes=True):
    print("Tres...")
    print("Dos...")
    print("Uno...")
    if not wishes:
        return

    print("¡Feliz año nuevo!")


happy_new_year()


def happy_new_year(wishes=False):
    print("Tres...")
    print("Dos...")
    print("Uno...")
    if not wishes:
        return

    print("¡Feliz año nuevo!")


happy_new_year()


# RETURN con una expresion
def boring_function():
    return 123


x = boring_function()

print("La función boring_function ha devuelto su resultado. Es:", x)


# Hay que tener en cuenta que el valor devuelto por la función puede ser ignorado. Por ejemplo:
def boring_function():
    print("'Modo aburrimiento' ON.")
    return 123


print("¡Esta lección es interesante!")
boring_function()
print("Esta lección es aburrida...")

# Imprimira
# ¡Esta lección es interesante!
# 'Modo aburrimiento' ON.
# Esta lección es aburrida...


# NONE
print(None + 2)
# Esto dara error, ya que None no es un numero, es un tipo de dato que no tiene valor.


# cuando se le asigna a una variable (o se devuelve como el resultado de una función)
# cuando se compara con una variable para diagnosticar su estado interno.

value = None
if value is None:
    print("Lo siento, no contienes ningún valor")


def strange_function(n):
    if (n % 2 == 0):
        return True


print(strange_function(2))
print(strange_function(1))  # AQUI devuleve NONE


# PODEMOS mandar listas a las funciones?
# SI
def list_sum(lst):
    s = 0

    for elem in lst:
        s += elem

    return s


print(list_sum([5, 4, 3]))


# ERROR, esto dara error ya que no es una lista. y no se puede iterar
print(list_sum(5))


# Una lista como el resultado de una funcion
def strange_list_fun(n):
    strange_list = []

    for i in range(0, n):
        strange_list.insert(0, i)

    return strange_list


print(strange_list_fun(5))


# LABORATORIO
# Path: module_four\lab_return_functions.py
