# Pregunta 2. Que es lo que ocurre cuando se invoca una función antes de ser definida? Ejemplo:

hi()


def hi():
    print("hi!")


# Pregunta 3  Qué es lo que ocurrirá cuando se ejecute el siguiente código?
def hi():
    print("hi")


hi(5)  # error, la funcion no recibe parametros
