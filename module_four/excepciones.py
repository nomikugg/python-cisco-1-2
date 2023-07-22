# EL pan diario de cada programador

# Excepciones
# Path: module_four\excepciones.py
value = 5
print(type(value) is int)

# Esto sirve para verificar si un  numero es entero, o float, o string, etc

# LA RAMA TRY-EXCEPT
# En realidad, la regla dice: "es mejor manejar un error cuando ocurre que tratar de evitarlo".
# Esto significa que el código que puede causar un error debe estar en la rama try del código.
# La rama except debe contener el código que se ejecutará en caso de que ocurra un error.


# La excepción confirma la regla
try:
    value = int(input('Ingresa un número natural: '))
    print('El recíproco de', value, 'es', 1/value)
except:
    print('No se que hacer con', value)


# uNA FORMA MEJORADA DE MANEJAR LAS EXCEPCIONES
try:
    value = int(input('Ingresa un número natural: '))
    print('El recíproco de', value, 'es', 1/value)
except ValueError:
    print('No se que hacer con', value)
except ZeroDivisionError:
    print('La división entre cero no está permitida en nuestro Universo.')


# La excepcion predeterminada y como usarla
try:
    value = int(input('Ingresa un número natural: '))
    print('El recíproco de', value, 'es', 1/value)
except ValueError:
    ('No se que hacer con.')
except ZeroDivisionError:
    print('La división entre cero no está permitida en nuestro Universo.')
except:
    print('Ha sucedido algo extraño, ¡lo siento!')


# ######################TIPOS de excepciones
###################  ZeroDivisionError ###############
# Esta aparece cuando intentas forzar a Python a realizar cualquier operación que provoque una división en la que el divisor es cero o no se puede distinguir de cero. Toma en cuenta que hay más de un operador de Python que puede hacer que se genere esta excepción. ¿Puedes adivinarlos todos?

# Si, estos son: /, //, y %.

############## ValueError ###############
# Espera esta excepción cuando estás manejando valores que pueden usarse de manera inapropiada en algún contexto. En general, esta excepción se genera cuando una función (como int() o float()) recibe un argumento de un tipo adecuado, pero su valor es inaceptable.

######### TypeError #############
# Esta excepción aparece cuando intentas aplicar un dato cuyo tipo no se puede aceptar en el contexto actual. Mira el ejemplo:

# short_list = [1]
# one_value = short_list[0.5]


########### AttributeError #############
# Esta excepción llega - entre otras ocasiones - cuando intentas activar un método que no existe en un elemento con el que se está tratando. Por ejemplo:


# short_list = [1]
# short_list.append(2)
# short_list.depend(3) ### el error se producirá aquí


####### SyntaxError ###########
# Esta excepción se genera cuando el control llega a una línea de código que viola la gramática de Python. Puede sonar extraño, pero algunos errores de este tipo no se pueden identificar sin ejecutar primero el código. Este tipo de comportamiento es típico de los lenguajes interpretados - el intérprete siempre trabaja con prisa y no tiene tiempo para escanear todo el código fuente. Se conforma con comprobar el código que se está ejecutando en el momento. Muy pronto se te presentará un ejemplo de esta categoría.

# Es una mala idea manejar este tipo de excepciones en tus programas. Deberías producir código sin errores de sintaxis, en lugar de enmascarar las fallas que has causado.


### pregunta 6 : PRUEBAAAAAAAAAA N####

def fun(x):
    x += 1
    return x


x = 2
x = fun(x + 1)
print(x)


# PREGUNTA 7
dictionary = {}
my_list = ['a', 'b', 'c', 'd']

for i in range(len(my_list) - 1):
    dictionary[my_list[i]] = (my_list[i], )

for i in sorted(dictionary.keys()):
    k = dictionary[i]
    print(k[0])


# pregunta 8
def func(a, b):
    return a ** a


print(func(2))


# pregunta 9
def func_1(a):
    return a ** a


def func_2(a):
    return func_1(a) * func_1(a)


print(func_2(2))


# pregunta 12
def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return


print(fun(fun(2)) + 1)


# pregunta 13
def fun(x):
    global y
    y = x * x
    return y


fun(2)
print(y)


# pregunta 14
def any():
    print(var + 1, end='')


var = 1
any()
print(var)


# pregunta 16
my_list = ['Mary', 'had', 'a', 'little', 'lamb']


def my_list(my_list):
    del my_list[3]
    my_list[3] = 'ram'


print(my_list(my_list))


# pregunta 17
def fun(x, y, z):
    return x + 2 * y + 3 * z


print(fun(0, z=1, y=3))


# pregunta 18
def fun(inp=2, out=3):
    return inp * out


print(fun(out=2))


# pregunta 19
dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dictionary['one']

for k in range(len(dictionary)):
    v = dictionary[v]
    # print(v)

print(v)


# pregunta 20
tup = (1, 2, 4, 8)
tup = tup[1:-1]
tup = tup[0]
print(tup)


# pregunta 22
try:
    value = input("Ingresa un valor: ")
    print(value/value)
except ValueError, ZeroDivisionError
    print("Entrada incorrecta...")
# except ZeroDivisionError:
#     print("Entrada errónea...")
except TypeError:
    print("Entrada muy errónea...")
except:
    print("¡Buuu!")
