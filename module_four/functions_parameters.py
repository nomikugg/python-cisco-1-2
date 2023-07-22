# Funciones con parametros

# def function(parameter):
###
#     # Cuerpo de la funcion
# Un parámetro es una variable, pero existen dos factores que hacen a un parámetro diferente:

# los parámetros solo existen dentro de las funciones en donde han sido definidos, y el único lugar donde un parámetro puede ser definido es entre los paréntesis después del nombre de la función, donde se encuentra la palabra clave reservada def;
# la asignación de un valor a un parámetro de una función se hace en el momento en que la función se manda llamar o se invoca, especificando el argumento correspondiente.


# Una funcion con dos parametros
def message(what, number):
    print("Ingresa", what, "número", number)


message("teléfono", 11)
message("precio", 5)
message("número", "number")


# Paso de parámetros posicionales
def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)


introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")


# Paso de argumentos de Palabra Clave
def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)


introduction(first_name="James", last_name="Bond")
introduction(last_name="Skywalker", first_name="Luke")


# Mezclando argumentos posicionales y de palabras clave

# Solo argumentos posicionales
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)


adding(1, 2, 3)


# Con palabras clave
adding(c=1, a=2, b=3)


# Ahora combinado
adding(3, c=1, b=2)


# Tener cuidado.
# Al contrario del anterior ejemplo, este código no funcionará: generara un error
adding(3, a=1, b=2)  # se le esta asignando dos veces un valor al parámetro a:


# Funciones parametrizadas - más detalles
def introduction(first_name, last_name="Smith"):
    print("Hola, mi nombre es", first_name, last_name)
# En este ejemplo el parametro de apellido tiene un valor por defecto si es que no se pasa el valor por parametro.


introduction("Jorge", "Pérez")
introduction("Enrique")
introduction(first_name="Guillermo")


# o de esta manera
def introduction(first_name="Juan", last_name="González"):
    print("Hola, mi nombre es", first_name, last_name)


introduction()


#

######################
def hi_all(name_1, name_2):
    print("Hola,", name_2)
    print("Hola,", name_1)


hi_all("Sebastián", "Konrad")


####################
def address(street, city, postal_code):
    print("Tu dirección es:", street, "St.,", city, postal_code)


s = input("Calle: ")
p_c = input("Código Postal: ")
c = input("Ciudad: ")
address(s, c, p_c)


# Es importante recordar que primero se especifican los argumentos posicionales y después los de palabras clave. Es por esa razón que si se intenta ejecutar el siguiente código:
def subtra(a, b):
    print(a - b)

# subtra(5, b=2) # salida: 3
# subtra(a=5, 2) # Syntax Error
