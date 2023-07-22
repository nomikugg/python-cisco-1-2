# Listas
numbers = [4, 8, 15, 16, 23, 42]
print("Contenido de la lista: ", numbers)

numbers[0] = 111
print("Contenido actualizado: ", numbers)


# copiando el valor del quinto elemento al segundo elemento
numbers[1] = numbers[4]
print("Lista con el segundo elemento actualizado: ", numbers)

print("Longitud de la lista: ", len(numbers))

# eleminar un elemento de la lista
del numbers[2]
print("Lista con el elemento eliminado: ", numbers)

# tambien se puede acceder al elemento de la lista con numeros negativos
print("Accediendo al ultimo elemento de la lista: ", numbers[-1])


# Laboratorio
# Fundamentos de las listas

# Esta es una lista existente de números ocultos en el sombrero.
hat_list = [1, 2, 3, 4, 5]

# Paso 1: escribe una línea de código que solicite al usuario
# reemplazar el número de en medio con un número entero ingresado por el usuario.

# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.

# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
numero_ingresado = int(input("Ingrese un numero entero: \n"))
hat_list[2] = numero_ingresado
del hat_list[-1]
print("Longitud de la lista: ", len(hat_list))
print(hat_list)
