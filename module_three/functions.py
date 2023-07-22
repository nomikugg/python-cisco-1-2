import time
print("Hola", end=" ")
print("Mundo")


# sep

print("Hola", "Mundo", "Palabra", sep="=")


print("Mi", "nombre", "es", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")
print("nada")


# combina end y sep
print("Programming", "Essentials", "in", sep="***", end="...")
print("Python")

# Ejercicio de flecha

###################
print("Version original:")
###################
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
###################
print("sin muchas invocaciones de print()")
###################
print("    *\n   * *\n  *   *\n *     *\n***   ***")
print("  *   *\n  *   *\n  *****")
###################
print("El doble de dimensiones:")
###################
print("        *")
print("       * *")
print("      *   *")
print("     *     *")
print("    *       *")
print("   *         *")
print("  *           *")
print(" *             *")
print("******     ******")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *******")
###################
print("Mostrar dos flechas")
###################
print("        *        "*2)
print("       * *       "*2)
print("      *   *      "*2)
print("     *     *     "*2)
print("    *       *    "*2)
print("   *         *   "*2)
print("  *           *  "*2)
print(" *             * "*2)
print("******     ******"*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *******     "*2)


# practica de saltos de linea

print('Greg\'s book.')
print("'Greg's book.'")
print('"Greg\'s book."')
print("Greg\'s book.")
# print('"Greg's book."')
print("\"Greg's book.\"")
print("Greg's book.")


print(0o123)

print(0x123)


print('"Estoy"')
print('\"\"aprendiento\"\"')
print('"""Python"""')

print("Hola", "Mundo")

'''
Prioridad	Operador
1	**
2	+, - (nota: los operadores unarios a la derecha del operador exponencial enlazan con mayor fuerza.)	unario
3	*, /, //, %
4	+, -                                   binario
'''

# nuevo orden
# 1 **
# 2 %
# 3 //
# 4 /
# 5 *
# 6 -
# 7 +
# 8 unario + y -
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)


# creando variables

john = 3
mary = 5
adam = 6
print(john, mary, adam, sep=",")
total_apples = john + mary + adam
print("Numero total de manzanas", total_apples)


# conversion millas a kilometros, y kilometros a millas
kilometers = 12.25
miles = 7.38
# 1 milla = 1.61 km
miles_to_kilometers = (miles * 1.61)
kilometers_to_miles = kilometers / 1.61

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")


x = 0
# Codifica tus datos de prueba aquí.
x = float(x)
# Escribe tu código aquí.
y = 3*x**3 - 2*x**2 + 3*x - 1
print("y =", y)


x = 1
# Codifica tus datos de prueba aquí.
x = float(x)
# Escribe tu código aquí.
y = 3*x**3 - 2*x**2 + 3*x - 1
print("y =", y)


x = -1
# Codifica tus datos de prueba aquí.
x = float(x)
# Escribe tu código aquí.
y = 3*x**3 - 2*x**2 + 3*x - 1
print("y =", y)


# impresion de una rectangulo
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

# impresion de un triangulo
print("   /\\")
print("  /  \\")
print(" /    \\")
print("/      \\")
print("-" * 10)
print("\\      /")
print(" \\    /")
print("  \\  /")
print("   \\/")
print("   " + "*" * 10)
print("  *" + " " * 8 + "*")
print(" *" + " " * 10 + "*")
print("*" + " " * 12 + "*")
print("*" + " " * 12 + "*")
print(" *" + " " * 10 + "*")
print("  *" + " " * 8 + "*")
print("   " + "*" * 10)
print("   " + "*" * 10)
print("  *" + " " * 8 + "*")
print(" *" + " " * 10 + "*")
print("*" + " " * 12 + "*")
print("*" + " " * 12 + "*")

x = float(input("Ingresa el valor para x: "))

# Escribe tu código aquí.
y = 1 / (x + (1 / (x + 1 / (x + 1/x))))
print("y =", y)


# conversion de horas, minutos y duracion de un evento
hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# Escribe tu código aquí.
# horas 0..23
# minutos 0..59
# entrada de duracion del evento en minutos
if hour < 0 or hour > 23:
    print("Hora de inicio incorrecta")
else:
    if mins < 0 or mins > 59:
        print("Minutos de inicio incorrectos")
    else:
        if dura < 0:
            print("Duracion del evento incorrecta, no se aceptan negativos")
        else:
            hour = (hour + (mins + dura) // 60) % 24
            mins = (mins + dura) % 60
            print("El evento terminara a las: " + str(hour) + ":" + str(mins))


# Prioridad	Operador
# 1	+, -	unario
# 2	**
# 3	*, /, //, %
# 4	+, -	binario
# 5	<, <=, >, >=
# 6	==, !=

numero = int(input("Ingresa un numero entero:"))
print(numero >= 100)


# espatifilio
nombre = input("Ingresa la cadena: ")
if nombre == "Espatifilo":
    print("¡Espatifilo es la mejor planta de todas")
elif nombre == "ESPATIFILO":
    print("Si, ¡El Espatifilo es la mejor planta de todos los tiempos!")
elif nombre == "espatifilo":
    print("No, ¡quiero un gran Espatifilo!")
else:
    print("¡Espatifilo! ¡No " + nombre + "!")


# calculadora de impuestos
income = float(input("Introduce el ingreso anual: "))

if income < 85528:
    tax = income * 0.18 - 556.02

else:
    # el impuesto era igual a 14,839 pesos y 2 centavos, más el 32% del excedente sobre 85,528 pesos.
    tax = 14839.02 + (income - 85528) * 0.32


if tax < 0:
    tax = 0.0
print

tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")


# anio bisiesto

year = int(input("Introduce un año: "))

if year < 1582:
    print("No esta dentro del período del calendario Gregoriano")
elif (year % 4) != 0:
    #  Escribe el bloque if-elif-elif-else aquí.
    print("Es un anio comun")
elif (year % 100) != 0:
    print("Es un anio bisiesto")
elif year % 400 != 0:
    print("Es un anio comun")
else:
    print("Es un anio bisiesto")


# bucles while.
# Almacena el actual número más grande aquí.
largest_number = -999999999

# Ingresa el primer valor.
number = int(input("Introduce un número o escribe -1 para detener: "))

# Si el número no es igual a -1, continuaremos
while number != -1:
    # ¿Es el número más grande que el valor de largest_number?
    if number > largest_number:
        # Sí si, se actualiza largest_number.
        largest_number = number
    # Ingresa el siguiente número.
    number = int(input("Introduce un número o escribe -1 para detener: "))

# Imprime el número más grande.
print("El número más grande es:", largest_number)


# otro ejemplo de bucles while
# Un programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares.
# El programa termina cuando se ingresa un cero.

odd_numbers = 0
even_numbers = 0

# Lee el primer número.
number = int(input("Introduce un número o escribe 0 para detener: "))

# 0 termina la ejecución.
while number != 0:
    # Verificar si el número es impar.
    if number % 2 == 1:
        # Incrementar el contador de números impares odd_numbers.
        odd_numbers += 1
    else:
        # Incrementar el contador de números pares even_numbers.
        even_numbers += 1
    # Leer el siguiente número.
    number = int(input("Introduce un número o escribe 0 para detener: "))

# Imprimir resultados.
print("Conteo de números impares:", odd_numbers)
print("Conteo de números pares:", even_numbers)


# bucles, Ejercicio de mago
secret_number = 777

print(
    """
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")
num = int(input("Ingresa un numero entero: "))
while num != secret_number:
    print("Ja ja, estas atrapado en mi bucle... ")
    num = int(input("Ingresa un nuevo numero para salir del bucle: "))
print("\n\nBien hecho muggle, Eres libre ahora!!")


# Bucles FOR
for i in range(2, 8):
    print("El valor de i es", i)

for i in range(2, 8, 3):
    print("El valor de i es", i)


# for i in range(1, 1):
#     print("El valor de i es", i)
# da error

# for i in range(2, 1):
#     print("El valor de i es", i)
# tambien da error

power = 1
for expo in range(16):
    print("2 a la potencia de", expo, "es", power)
    power *= 2

# Escribe un bucle for que cuente hasta cinco.
# Cuerpo del bucle: imprime el número de iteración del bucle y la palabra "Mississippi".
# Cuerpo del bucle, emplea : time.sleep(1)
for sec in range(5):
    print("Mississippi")
    time.sleep(1)

print("Listos o no. Ahi voy!")
# Escribe una función print con el mensaje final.
