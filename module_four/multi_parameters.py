# Ejemplos de IMC
# Indice de Masa Corporal
# IMC = peso / altura^2
def bmi(weight, height):
    return weight / height ** 2


print(bmi(52.5, 1.65))


def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
            weight < 20 or weight > 200:  # La \ se usa para hacer un salto y continuar en la siguiente linea, es opcional y util para cuando la linea es muy larga
        return None

    return weight / height ** 2


print(bmi(352.5, 1.65))


# Escribimos dos funciones sencillas para convertir unidades del sistema inglés al sistema métrico. Comencemos con las pulgadas.

# Es bien conocido que 1 lb = 0.45359237 kg. Esto lo emplearemos en nuestra nueva función.

def lb_to_kg(lb):
    return lb * 0.45359237


print(lb_to_kg(1))


# Haremos lo mismo ahora con los pies y pulgadas: 1 ft = 0.3048 m, y 1 in = 2.54 cm = 0.0254 m.
def ft_and_inch_to_m(ft, inch=0.0):
    return ft * 0.3048 + inch * 0.0254


print(ft_and_inch_to_m(1, 1))
print(ft_and_inch_to_m(6, 0))


# Finalmente probamos si todo funciona bien.
# Cuál es el IMC de una persona que tiene 5'7" de altura y un peso de 176 lbs?
print(bmi(lb_to_kg(176), ft_and_inch_to_m(5, 7)))


# Funciones con triangulos
def is_a_triangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True


print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))


# una version mas corta
def is_a_triangle(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True


print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))


# Aun mas compacta
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))


# Con valores interactivos
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


a = float(input('Ingresa la longitud del primer lado: '))
b = float(input('Ingresa la longitud del segundo lado: '))
c = float(input('Ingresa la longitud del tercer lado: '))

if is_a_triangle(a, b, c):
    print('Si, si puede ser un triángulo.')
else:
    print('No, no puede ser un triángulo.')


# Ahora con un triangulo recatngulo

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
    if b > a and b > c:
        return b ** 2 == a ** 2 + c ** 2


def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)


print(area_of_triangle(1., 1., 2. ** .5))

print(is_a_right_triangle(5, 3, 4))
print(is_a_right_triangle(1, 3, 4))
print(is_a_right_triangle(4, 5, 3))


##################### FACTORIALES #############################
# 0! = 1 (¡Si!, es verdad) 1! = 1 2! = 1 * 2 3! = 1 * 2 * 3 4! = 1 * 2 * 3 * 4 : : n! = 1 * 2 ** 3 * 4 * ... * n-1 * n


def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1

    product = 1
    for i in range(2, n + 1):
        product *= i
    return product


for n in range(1, 6):  # probando
    print(n, factorial_function(n))


################## FIBONACCI#####################
# Son una secuencia de números enteros los cuales siguen una regla sencilla:

# el primer elemento de la secuencia es igual a uno (Fib1 = 1)
# el segundo elemento también es igual a uno (Fib2 = 1)
# cada número después de ellos son la suman de los dos números anteriores (Fibi = Fibi-1 + Fibi-2)
# Aquí están algunos de los primeros números en la serie Fibonacci:

# fib_1 = 1 fib_2 = 1 fib_3 = 1 + 1 = 2 fib_4 = 1 + 2 = 3 fib_5 = 2 + 3 = 5 fib_6 = 3 + 5 = 8 fib_7 = 5 + 8 = 13

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum


for n in range(1, 10):  # probando
    print(n, "->", fib(n))


################## RECURSIVIDAD#####################
######## Fibonacci recursivo################
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)

########### Factorial recursivo################


def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)


print(factorial_function(5))
######## QUIZ###############
# Pregunta 1


def factorial(n):
    return n * factorial(n - 1)


print(factorial(4))
# ERROR, entra en un bucle infinito


# PRegunta 2


def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)


print(fun(25))
# 56
