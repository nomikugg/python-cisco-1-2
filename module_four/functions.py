# Funciones

# Un ejemplo basico de como funciona una funcion
def message():
    # 3 Una vez leida la funcion, vuelve a la linea de donde habia quedado.
    print("Ingresar valor: ")


# Empieza aqui
print("Inicia aqui.")  # 1
message()  # 2 Llamada a la funcion, va a leer la funcion
print("Termina aqui.")  # 4

# Los numeros indican el orden en el que se ejecuan las lineas de codigo


# Existen dos consideraciones muy importantes, la primera de ella es:

# No se debe invocar una función antes de que se haya definido.

# Recuerda - Python lee el código de arriba hacia abajo. No va a adelantarse en el código para determinar si la función invocada está definida más adelante, (el lugar "correcto" para definirla es "antes de ser invocada".)

# Se ha insertado un error en el siguiente código - ¿puedes notar la diferencia?
print("Inicia aqui.")
message()
print("Termina aqui.")


def message():
    print("Ingresar valor: ")


# Esta otra manera es otra forma de hacerlo.
print("Comienza aqui.")


def message():
    print("Ingresar valor: ")


message()

print("Termina aqui.")


# Y esta es la manera correcta de hacerlo.


def message():
    print("Ingresar valor: ")


message()
a = int(input())
message()
b = int(input())
message()
c = int(input())
