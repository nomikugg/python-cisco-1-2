# LAB   Un año bisiesto: escribiendo tus propias funciones
def is_year_leap(year):
    if (year % 4) != 0:
        return False
    elif (year % 100) != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")


# 2    LAB   Cuántos días: escribiendo y usando tus propias funciones


# Tu tarea es escribir y probar una función que toma dos argumentos (un año y un mes) y devuelve el número de días del mes/año dado (mientras que solo febrero es sensible al valor year, tu función debería ser universal).

# La parte inicial de la función está lista. Ahora, haz que la función devuelva None si los argumentos no tienen sentido.

# Por supuesto, puedes (y debes) utilizar la función previamente escrita y probada (LAB 4.3.1.6). Puede ser muy útil. Te recomendamos que utilices una lista con los meses. Puedes crearla dentro de la función - este truco acortará significativamente el código.

# Hemos preparado un código de prueba. Amplíalo para incluir más casos de prueba.


def is_year_leap(year):
    if (year % 4) != 0:
        return False
    elif (year % 100) != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def days_in_month(year, month):
    if is_year_leap(year):
        month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return month_days[month - 1]
    elif not is_year_leap(year):
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return month_days[month - 1]
    else:
        return None
    # if year < 1582 or month < 1 or month > 12:
    #     return None
    # days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # res  = days[month - 1]
    # if month == 2 and is_year_leap(year):
    #     res = 29
    # return res


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")


# LABORATORIO: 3
# LAB   Día del año: escribiendo y usando tus propias funciones

# Tu tarea es escribir y probar una función que toma tres argumentos (un año, un mes y un día del mes) y devuelve el día correspondiente del año, o devuelve None si cualquiera de los argumentos no es válido.

# Debes utilizar las funciones previamente escritas y probadas. Agrega algunos casos de prueba al código. Esta prueba es solo el comienzo.

def is_year_leap(year):
    if (year % 4) != 0:
        return False
    elif (year % 100) != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def days_in_month(year, month):
    if is_year_leap(year):
        month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return month_days[month - 1]
    elif not is_year_leap(year):
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return month_days[month - 1]
    else:
        return None


def day_of_year(year, month, day):
    if year < 1582 or month < 1 or month > 12 or day < 1 or day > 31:
        return None
    if day > days_in_month(year, month):
        return None
    res = 0
    for m in range(1, month):
        md = days_in_month(year, m)
        res += md
    res += day
    return res


print(day_of_year(2000, 12, 31))
print(day_of_year(2000, 2, 29))


# LABORATORIO 4
# Numeros primos y como encontrarlos
# Un número primo es un número natural mayor que 1 que no tiene divisores más que 1 y él mismo.
def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    elif num > 2 and num % 2 == 0:
        return False
    else:
        for i in range(3, num):
            if num % i == 0:
                return False
        return True


for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()


# LAB 5  Conversión del consumo de combustible

# El consumo de combustible de un automóvil se puede expresar de muchas maneras diferentes. Por ejemplo, en Europa, se muestra como la cantidad de combustible consumido por cada 100 kilómetros.

# En los EE. UU., se muestra como la cantidad de millas recorridas por un automóvil con un galón de combustible.

# Tu tarea es escribir un par de funciones que conviertan l/100km a mpg (milas por galón), y viceversa.

# Las funciones:

# se llaman liters_100km_to_miles_gallon y miles_gallon_to_liters_100km respectivamente;
# toman un argumento (el valor correspondiente a sus nombres)
# Complementa el código en el editor y ejecuta tu código y verifica si tu salida es la misma que la nuestra.

# Aquí hay información para ayudarte:

# 1 milla = 1609.344 metros.
# 1 galón = 3.785411784 litros.

# litros/100km  = 1km/1000 m. * 1609.344 m/1 milla * 1 galon/3.785411784 litros
# millas/galon = ((1km/1000 m.) * 1609.344 m ) / 3.785411784
def liters_100km_to_miles_gallon(liters):
    return (100000 * 3.785411784) / (liters * 1609.344)


def miles_gallon_to_liters_100km(miles):
    return 100000 / (miles * 1609.344 / 3.785411784)


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))


# QUIZ

# pregunta 1
def hi():
    return
    print("¡Hola!")


hi()


# Pregunta 2
def is_int(data):
    if type(data) == int:
        return True
    elif type(data) == float:
        return False


print(is_int(5))
print(is_int(5.0))
print(is_int("5"))


# Pregunta 3
def even_num_lst(ran):
    lst = []
    for num in range(ran):
        if num % 2 == 0:
            lst.append(num)
    return lst


print(even_num_lst(11))


# pregunta 4
def list_updater(lst):
    upd_list = []
    for elem in lst:
        elem **= 2
        upd_list.append(elem)
    return upd_list


foo = [1, 2, 3, 4, 5]
print(list_updater(foo))


# Pregunta 5
