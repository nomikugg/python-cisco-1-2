school_class = {}

while True:
    name = input("Ingresa el nombre del estudiante: ")
    if name == '':
        break

    score = int(input("Ingresa la calificación del estudiante (0-10): "))
    if score not in range(0, 11):
        break

    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)

for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)
# Imaginemos el siguiente problema:

# necesitas un programa para calcular los promedios de tus alumnos;
# el programa pide el nombre del alumno seguido de su calificación;
# los nombres son ingresados en cualquier orden;
# el ingresar un nombre vacío finaliza el ingreso de los datos (Nota 1: ingresar una puntuación vacía generará la excepción ValueError, pero no te preocupes por eso ahora, verás cómo manejar tales casos cuando hablemos de excepciones en el segundo parte de la serie del curso Fundamentos de Python)
# una lista con todos los nombre y el promedio de cada alumno debe ser mostrada al final.


# línea 1: crea un diccionario vacío para ingresar los datos; el nombre del alumno es empleado como clave, mientras que todas las calificaciones asociadas son almacenadas en una tupla (la tupla puede ser el valor de un diccionario, esto no es un problema)
# línea 3: se ingresa a un bucle "infinito" (no te preocupes, saldrémos de el en el momento indicado)
# línea 4: se lee el nombre del alumno aquí;
# línea 5-6: si el nombre es una cadena vacía (), salimos del bucle;
# línea 8: se pide la calificación del estudiante (un valor entero en el rango del 0-10)
# línea 9-10: si la puntuación ingresada no está dentro del rango de 0 a 10, se abandona el bucle;
# línea 12-13: si el nombre del estudiante ya se encuentra en el diccionario, se alarga la tupla asociada con la nueva calificación (observa el operador +=)
# línea 14-15: si el estudiante es nuevo (desconocido para el diccionario), se crea una entrada nueva, su valor es una tupla de un solo elemento la cual contiene la calificación ingresada;
# línea 17: se itera a través de los nombres ordenados de los estudiantes;
# línea 18-19: inicializa los datos necesarios para calcular el promedio (sum y counter).
# línea 20-22: se itera a través de la tupla, tomado todas las calificaciones subsecuentes y actualizando la suma junto con el contador.
# línea 23: se calcula e imprime el promedio del alumno junto con su nombre.


# REPASO

my_tuple = (1, 2, True, "una cadena", (3, 4), [5, 6], None)
print(my_tuple)

my_list = [1, 2, True, "una cadena", (3, 4), [5, 6], None]
print(my_list)


# EXTRA

# Se puede crear una tupla con la funcion TUPLE de python
my_tuple = tuple((1, 2, "cadena"))
print(my_tuple)

my_list = [2, 4, 6]
print(my_list)  # salida: [2, 4, 6]
print(type(my_list))  # salida: <class 'list'>
tup = tuple(my_list)
print(tup)  # salida: (2, 4, 6)
print(type(tup))  # salida: <class 'tuple'>


# TAMBIEN se puede hacer uso de la funcion LIST
tup = 1, 2, 3,
my_list = list(tup)
print(type(my_list))  # salida: <class 'list'>


# DICCIONARIOS
# SE puede hacer uso del metodo GET
pol_esp_dictionary = {
    "kwiat": "flor",
    "woda": "agua",
    "gleba": "tierra"
}

item_1 = pol_esp_dictionary["gleba"]  # Ejemplo 1
print(item_1)  # salida: tierra

item_2 = pol_esp_dictionary.get("woda")  # Ejemplo 2
print(item_2)  # salida: agua


# PARA verificar si una clave existe en el diccionario
pol_esp_dictionary = {
    "zamek": "castillo",
    "woda": "agua",
    "gleba": "tierra"
}

if "zamek" in pol_esp_dictionary:
    print("Si")
else:
    print("No")


# PARA hacer una COPIA hacemos uso del metodo COPY
pol_esp_dictionary = {
    "zamek": "castillo",
    "woda": "agua",
    "gleba": "tierra"
}

copy_dictionary = pol_esp_dictionary.copy()
print(copy_dictionary)


# QUIZ

# pregunta 2

tup = 1, 2, 3
a, b, c = tup
# a, b, c = (1, 2, 3). se desepaquetara en las variables a, b, y c
print(a * b * c)
print(a)
print(type(b))


# Pregunta 3
tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)  # Escribe tu código aquí.
# cuenta cuantos numero 2 hay en la tupla
print(duplicates)  # salida: 4


# Pregunta 4, union de dos diccionarios
d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):  # recorre los dos diccionarios
    d3.update(item)

print(d3)


# Pregunta 5
my_list = ["car", "Ford", "flower", "Tulip"]

t = tuple(my_list)  # Escribe tu código aquí. Convierte la lista en tupla
print(t)


# pregunta 6
colors = (("green", "#008000"), ("blue", "#0000FF"))  # Tupla de Tuplas

# Escribe tu código aquí. Convierte la tupla en diccionario
colors_dictionary = dict(colors)

print(colors_dictionary)


# Pregunta 7:
my_dictionary = {"A": 1, "B": 2}
copy_my_dictionary = my_dictionary.copy()
my_dictionary.clear()

print(copy_my_dictionary)
print(my_dictionary)


# pregunta 8
colors = {
    "blanco": (255, 255, 255),
    "gris": (128, 128, 128),
    "rojo": (255, 0, 0),
    "verde": (0, 128, 0)
}

for col, rgb in colors.items():
    print(col, ":", rgb)
