# pregunta 1


# pregunta 5
def function_1(a):
    return None


def function_2(a):
    return function_1(a) * function_1(a)


print(function_2(2))


# Pregunta 7
# def func(a, b):
#     return b ** a


# print(func(b=2, 2))

# pregunta 8
z = 0
y = 10
x = y < z and z > y or y < z and z < y
print(x)

# in = 4
# print(in)

# pregunta 10
my_list = [x * x for x in range(5)]


def fun(lst):
    del lst[lst[2]]
    return lst


print(fun(my_list))


# pregunta 11
x = 1
y = 2
x, y, z = x, x, y
z, y, z = x, y, z

print(x, y, z)


# pregunta 12
a = 1
b = 0
a = a ^ b
b = a ^ b
a = a ^ b

print(a, b)


# pregunta 13
def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return 2


print(fun(fun(2)))


# pregunta 14
nums = [1, 2, 3]
vals = nums
del vals[:]
print(nums)
print(vals)


# pregunta 15
x = int(input("Ingrese un número:"))
y = int(input("Ingrese otro número:"))
x = x % y
x = x % y
y = y % x
print(y)


# pregunta 17
print("a", "b", "c", sep="sep")


# pregunta 18
x = 1 // 5 + 1 / 5
print(x)


# pregunta 20
x = float(input("Ingrese un número:"))
y = float(input("Ingrese otro número:"))
print(y ** (1 / x))

# pregunta 21
dct = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dct['three']

for k in range(len(dct)):
    v = dct[v]

print(v)

# pregunta 22
lst = [i for i in range(-1, -2)]
print(lst)

# pregunta 24


def fun(x, y):
    if x == y:
        return x
    else:
        return fun(x, y-1)


print(fun(0, 3))

# preunta 25
i = 0
while i < i + 2:
    i += 1
    print("*")
else:
    print("*")
# cuidado bucle infinito


# pregunta 26
tup = (1, 2, 4, 8)
tup = tup[-2:-1]
tup = tup[-1]
print(tup)


# pregunta 27
dd = {"1": "0", "0": "1"}
for x in dd.vals():
    print(x, end="")


# pregunta 28
dct = {}
dct['1'] = (1, 2)
dct['2'] = (2, 1)

for x in dct.keys():
    print(dct[x][1], end="")


# pregunta 29
def fun(inp=2, out=3):
    return inp * out


print(fun(out=2))


# pregunta 30
lst = [[x for x in range(3)] for y in range(3)]

for r in range(3):
    for c in range(3):
        if lst[r][c] % 2 != 0:
            print("#")


# pregunta 31
try:
    value = input("Ingresa un valor: ")
    print(int(value)/len(value))
except ValueError:
    print("Entrada incorrecta...")
except ZeroDivisionError:
    print("Entrada erronea...")
except TypeError:
    print("Entrada muy erronea...")
except:
    print("¡Buuu!")


# pregunta 32
try:
    print(5/0)
    break
except:
    print("Lo siento, algo salió mal...")
except (ValueError, ZeroDivisionError):
    print("Mala suerte...")


# pregunta 33
foo = (1, 2, 3)
print(foo.index(0))

|#pregunta 35
print(hola mundo)
