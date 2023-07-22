# Los diccionarios son estructuras de datos que permiten almacenar pares clave-valor.
# son mutables y no ordenados
# Se crea con llaves {}
#

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
phone_numbers = {'jefe': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)


print(dictionary['gato'])
print(phone_numbers['Suzy'])


# Buscador de palabras en un diccionario
dictionary = {"gato": "cat", "perro": "chien", "caballo": "cheval"}
words = ['gato', 'león', 'caballo']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "no está en el diccionario")


# EL metodo KEY
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])


# ITEMS
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

for spanish, french in dictionary.items():
    print(spanish, "->", french)


# MODIFICAR, AGREGAR O ELIMINAR ELEMENTOS ##############################
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

dictionary['gato'] = 'minou'
print(dictionary)


# para ordenar la salida
# for key in sorted(dictionary.keys()):


# Funcion VALUES
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

for french in dictionary.values():
    print(french)


# AGREGANDO ELEMENTOS
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

dictionary['cisne'] = 'cygne'
print(dictionary)


# O hacerlo con el metodo update
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

dictionary.update({"pato": "canard"})
print(dictionary)


# ELIMINANDO UNA CLAVE
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

del dictionary['perro']
print(dictionary)


# PARA eliminar el ultimo elemento se usa el metodo popitem()
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

dictionary.popitem()
print(dictionary)  # salida: {'gato': 'chat', 'perro': 'chien'}
