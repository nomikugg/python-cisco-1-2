# Las tuplas son datos o valores inmutables. a diferencia de las lista estas no se pueden modificar
# un Ejemplo
tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125

print(tuple_1)
print(tuple_2)


empty_tuple = ()


# tambien debe de haber una coma al final para distinguir de un valor escalar
one_element_tuple_1 = (1, )
one_element_tuple_2 = 1.,  # con una coma al final para distinguir de un valor escalar


# Si se desea leer una tupla lo podemos hacer al igual que con las listas
my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print(elem)
# La salida seria
# 1
# 1000
# (10, 100, 1000)
# (1, 10)
# 1
# 10
# 100
# 1000

# my_tuple = (1, 10, 100, 1000)

# my_tuple.append(10000)
# del my_tuple[0]
# my_tuple[1] = -10


# Todos los demas metodos de las listas se aplica para las tuplas
my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)

############
var = 123

t1 = (1, )
t2 = (2, )
t3 = (3, var)

t1, t2, t3 = t2, t3, t1

print(t1, t2, t3)
# Pueden intercambiar los valores entre Tuplas
