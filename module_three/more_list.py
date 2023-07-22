# Algunos ejemplos mas de listas y rebanadas
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)


# # Otra forma de hacerlo
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list:
    if i > largest:
        largest = i

print(largest)


# Usando rebanada
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list[1:]:
    if i > largest:
        largest = i

print(largest)


# Para encontrar un numero en una lista
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Elemento encontrado en el índice", i)
else:
    print("ausente")


# Supongamos que has elegido los siguientes números en la lotería: 3, 7, 11, 42, 34, 49.

# Los números que han salido sorteados son: 5, 11, 9, 42, 3, y 49.

# La pregunta es: ¿A cuántos números le has atinado?
drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print("Le atinaste a " + str(hits) + " numeros.")


# LABORATORIO
# # Path: list_lab.py
