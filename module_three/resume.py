# En resumen todo lo visto sobre listas

cubed = [num ** 3 for num in range(5)]
print(cubed)  # output: [0, 1, 8, 27, 64]


# Una tabla de cuatro columnas y cuatro filas: un arreglo bidimensional (4x4)

table = [[":(", ":)", ":(", ":)"], [":)", ":(", ":)", ":)"], [
    ":(", ":)", ":)", ":("], [":)", ":)", ":)", ":("]]

print(table)
print(table[0][0])  # output: ':('
print(table[0][3])  # output: ':)'


# 3
# Puedes anidar tantas listas en las listas como desee y, por lo tanto, crear listas n-dimensionales, por ejemplo, arreglos de tres, cuatro o incluso sesenta y cuatro dimensiones. Por ejemplo:
# Cubo - un arreglo tridimensional (3x3x3)

cube = [[[':(', 'x', 'x'], [':)', 'x', 'x'], [':(', 'x', 'x']],
        [[':)', 'x', 'x'], [':(', 'x', 'x'], [':)', 'x', 'x']],
        [[':(', 'x', 'x'], [':)', 'x', 'x'], [':)', 'x', 'x']]]

print(cube)
print(cube[0][0][0])  # output: ':('
print(cube[2][2][0])  # output: ':)'


for i in range(1):
    print("#")
else:
    print("#")


# Repasar esta pregunta

var = 1
while var < 10:
    print("#")
    var = var << 1

# Tambien repasar esta pregunta
z = 10
y = 0
x = y < z and z > y or y > z and z < y
print(x)


# Otra pregunta a repasar
a = 1
b = 0
c = a & b
d = a | b
e = a ^ b

print(c + d + e)


# Otro ejemplo
my_list = [i for i in range(-1, 2)]
print(my_list)


#################
t = [[3-i for i in range(3)] for j in range(3)]
print(t)


# HACKERRANK
x = int(input("|ingrese x"))
y = int(input("ingrese y: "))
z = int(input("ingrese z: "))
n = int(input("|ingrese n: "))
print([[i, j, k] for i in range(x+1) for j in range(y+1)
      for k in range(z+1) if (i+j+k) != n])
