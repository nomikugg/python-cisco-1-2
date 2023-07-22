# En esta seccion, se explica cual es el alcance de las funciones
# Por ejemplo
def scope_test():
    x = 123


scope_test()
print(x)  # no es accesible fuera de la funcion

# Esto dara error, ya que la variable x no esta definida fuera de la funcion.


# En este caso la variable creado fuera de la funcion es accesible dentro de la funcion, se conoce su valor

def my_function():
    print("¿Conozco a la variable?", var)


var = 1
my_function()
print(var)


# Ahora veamos un ejemplo de como se puede modificar una variable global dentro de una funcion
def my_function():
    var = 2
    print("¿Conozco a la variable?", var)


var = 1
my_function()
var = 5  # se puede modificar la variable global dentro la funcion pero no es una buena practica
print(var)


# Funciones y alcances: la palabra clave global
# La palabra clave global se puede usar para modificar una variable global dentro de una funcion
# Un ejemplo
def my_function():
    global var
    var = 2
    print("¿Conozco a aquella variable?", var)


var = 1
my_function()
print(var)


# Cómo interactúa la función con sus argumentos
def my_function(n):
    print("Yo recibí", n)
    n += 1
    print("Ahora tengo", n)


var = 1
my_function(var)
print(var)


def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    my_list_1 = [0, 1]
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)


# Otro ejemplo
def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0]  # Presta atención a esta línea.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)


# Intentémoslo:

# si el argumento es una lista, el cambiar el valor del parámetro correspondiente no afecta la lista (recuerda: las variables que contienen listas son almacenadas de manera diferente que las escalares)
# pero si se modifica la lista identificada por el parámetro (nota: ¡la lista, no el parámetro!), la lista reflejará el cambio.


### QUIZ##########
# Pregunta 2
a = 1


def fun():
    a = 2
    print(a)


fun()
print(a)
# 2
# 1

# pregunta 3
a = 1


def fun():
    global a
    a = 2
    print(a)


fun()
a = 3
print(a)
# 2
# 3

# Pregunta 4
a = 1


def fun():
    global a
    a = 2
    print(a)


a = 3
fun()
print(a)
# 2
# 2
