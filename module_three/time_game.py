import time
# Escribe un bucle for que cuente hasta cinco.
# Cuerpo del bucle: imprime el número de iteración del bucle y la palabra "Mississippi".
# Cuerpo del bucle, emplea : time.sleep(1)
for sec in range(5):
    print("Mississippi")
    time.sleep(1)

print("Listos o no. Ahi voy!")
# Escribe una función print con el mensaje final.


# break - ejemplo

print("La instrucción break:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro del bucle.", i)
print("Fuera del bucle.")


# continue - ejemplo

print("\nLa instrucción continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle.", i)
print("Fuera del bucle.")


largest_number = -99999999
counter = 0

while True:
    number = int(
        input("Ingresa un número o escribe -1 para finalizar el programa: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("El número más grande es", largest_number)
else:
    print("No has ingresado ningún número.")

# Otro ejemplo de continue
largest_number = -99999999
counter = 0

number = int(
    input("Ingresa un número o escribe -1 para finalizar el programa: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(
        input("Ingresa un número o escribe -1 para finalizar el programa: "))

if counter:
    print("El número más grande es", largest_number)
else:
    print("No has ingresado ningún número.")


# Otro ejemplo de bucles
palabra = input("Ingresa la palabra secreta: \n")
while True:
    if palabra == "chupacabra":
        break
    palabra = input("Ingresa la palabra secreta: \n")
print("Has salido del bucle con exito!")


# Devorador de vocales, Ejercicio
# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable user_word.
user_word = input("Ingresa una palbra: \n")
word_without_wovels = ""
for letter in user_word:
    if letter in "aeiou":
        continue
    word_without_wovels += letter
print(word_without_wovels)
# Completa el cuerpo del bucle for.


i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)


i = 5
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)


for i in range(5):
    print(i)
else:
    print("else:", i)
# curiosoooooooooooooo


i = 111
for i in range(2, 1):
    print(i)
else:
    print("else:", i)
# no entra al bucle por el tema de rango, pero se muestra el else.


bloques = int(input("Introduzca el número de bloques disponibles: "))

altura = 0

utilizados = 0
por_fila = 1

while True:
    utilizados += por_fila
    if utilizados > bloques:
        break

    altura += 1
    por_fila += 1


print("La altura de la pirámide es de: ", altura)


# Hipotesis de Collatz
c0 = int(input("Ingresa un numero entero: \n"))
pasos = 0
while c0 != 1:
    if c0 % 2 == 0:
        c0 /= 2
        print(int(c0))
        pasos += 1
    else:
        c0 = 3 * c0 + 1
        print(int(c0))
        pasos += 1
print("\nPassos = " + str(pasos))

# QUIZ

# pregunta 1
for i in range(0, 15):
    if i % 2 == 1:
        print(i)
# Línea de código. # Línea de código.


# Pregunta 2
# Crea un bucle while que cuente de 0 a 10, e imprima números impares en la pantalla.
x = 0
while x < 11:
    if x % 2 == 1:
        print(x)
    x += 1
    # Línea de código. # Línea de código. # Línea de código.


# Pregunta 3: Crea un programa con un bucle for y una sentencia break. El programa debe iterar sobre los caracteres en una dirección de correo electrónico, salir del bucle cuando llegue al símbolo @ e imprimir la parte antes de @ en una línea.
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")


# Pregunta 4: Crea un programa con un bucle for y una sentenciacontinue. El programa debe iterar sobre una cadena de dígitos, reemplazar cada 0 con x, e imprimir la cadena modificada en la pantalla.
for digit in "0165031806510":
    if digit == "0":
        # digit = "x"
        # print(digit, end="")
        print("x", end="")
        continue
    print(digit, end="")

# Pregunta 5
n = 3

while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n)


# pregunta 6
n = range(4)

for num in n:
    print(num - 1)
else:
    print(num)


# pregunta 7
for i in range(0, 6, 3):
    print(i)


# investigar
# La negación a nivel de bits es así:


# bitneg = ~i

# Puede ser un poco sorprendente: el valor de la variable bitneg es -16. Esto puede parecer extraño, pero no lo es en absoluto. Si deseas obtener más información, debes consultar el sistema de números binarios y las reglas que rigen los números de complemento de dos.


# Desplazamiento a la derecha e izquierda de bits en python
var = 17
var_right = var >> 1
var_left = var << 2
print(var, var_left, var_right)
# Dato interesante: el desplazamiento a la derecha es equivalente a la división por 2, mientras que el desplazamiento a la izquierda es equivalente a la multiplicación por 2.
# 17 >> 1 → 17 // 2 (17 dividido entre 2 a la potencia de 1) → 8 (desplazarse hacia la derecha en un bit equivale a la división entera entre dos)
# 17 << 2 → 17 * 4 (17 multiplicado por 2 a la potencia de 2) → 68 (desplazarse hacia la izquierda dos bits es lo mismo que multiplicar números enteros por cuatro)


# Quiz
# Pregunta 1
x = 1
y = 0

z = ((x == y) and (x == y)) or not (x == y)
print(not (z))
