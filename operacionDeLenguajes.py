"""
Realizara varias operaciones dentro de un contexto relacionado con lenguajes formales, alfabetos definidos e ingreso
de cadena
"""

def buscar(principio, lenguaje, cardenalidad, longitud, w, nivel):
    '''Función recursiva que buscará una palabra en un lenguaje definido por el usuario. Los sig. son parametros:
    :param principio: La posicion inicial desde donde se buscará la palabra en 'w'
    :param lenguaje: una lista de palabras que definen un 'lenguaje'
    :param cardenalidad: lista de enteros que representa las longitudes de cada palabra en el 'lenguaje'
    :param longitud: cantidad de palabras en el lenguaje
    :param w: la palabra que se busca en el lenguaje
    :param nivel: contador que lleva la cuenta la profundidad de la busqueda
    :return:
    '''
    pertenece = nivel
    # iterar sobre las palabras de lenguaje
    for i in range(longitud):
        # si alguna 'w' comienza con alguna de ellas
        if w.find(lenguaje[i], principio) == principio:
            pertenece += 1
            # verificar si la palabra completa se enccontro
            if principio + cardenalidad[i] == len(w):
                # si se encontro completa devuelve 'pertenece'
                return pertenece
            #Si no, hace una llamada a la funcion de forma recursiva con otro valores: 'principio' y ' pertecene'
            next_level = buscar(principio + cardenalidad[i], lenguaje, cardenalidad, longitud, w, pertenece)
            if next_level > -1:
                return next_level
            else:
                pertenece -= 1
    # si no se encuentra la palabra en ninguna iteración
    return -1


def operacion_w1_w2(w1, w2):
    '''La funcion toma dos palabras, y realizar con ellas una serie de operaciones
    :param w1:
    :param w2:
    :return: resultado

    El resultado se obtiene de realizar operaciones de concatenación, inversa y potenciación
    '''
    concatenacion = w1 + w2
    inversa = concatenacion[::-1]
    resultado = inversa * 2
    return resultado


def main():
    '''

    :return:
    '''

    # el usuario ingresa un alfabeto
    sigma = input("Ingresa el alfabeto separado por espacios:\nEjemplo 'a b c s'\nΣ: ")

    # el usuario ingresa un lenguaje
    l = input("Ingresa el lenguaje separado por comas\nEjemplo 'aa,ca,de,ga,fa'\nL = ")

    # se verifica que todos los caracteres esten en 'sigma' y que todas las palabras en l tengan una long. de 2 o 3 caracteres

    '''
    la variable 's' es una variable de iteracion en esta comprensión de lista, se estará iterando a traves de las palabras 
    obtenidas al dividir la cadena 'l' por comas usando l.split(','), en cada iteración una palabra se almacena en la 
    variable 's'. 
    '''
    if all((len(s) == 2 or len(s) == 3) and all(c in sigma for c in s) for s in l.split(',')):
        # divido 'l' en palabras individuales
        l_separado = l.split(',')
        # creo copia de l_separado
        lenguaje = l_separado.copy()
        # contiene la longitud de cada palabra en l_separado
        cardenalidad = [len(s) for s in l_separado]
        # calcular la longitud del lenguaje, osea la cantidad de la palabras en el lenguaje
        longitud = len(lenguaje)

        # el usuario ingresa dos palabras
        w1 = input("Ingresa la primera palabra:\nw1 = ")
        w2 = input("Ingresa la segunda palabra:\nw2 = ")

        # llamo la funcioj buscar para verificar que w1 y w2 se hayan creado a partir del lenguaje.
        # si pertenecen su resultado se guardara en la variable definida.
        pertenece_w1 = buscar(0, lenguaje, cardenalidad, longitud, w1, 0)
        pertenece_w2 = buscar(0, lenguaje, cardenalidad, longitud, w2, 0)

        # Si el nivel de pertenencia es mayor a -1 es porque pertenecen al lenguaje.
        if pertenece_w1 > -1 and pertenece_w2 > -1:
            print(f"w1 pertenece a L{pertenece_w1}")
            print(f"w2 pertenece a L{pertenece_w2}")
            # Se llama a la funcion que realizará la operacion
            resultado = operacion_w1_w2(w1, w2)
            # imprimir
            print(f"[(w1.w2)^(-1)]^2 = {resultado}")
        else:
            # error, las palabras no forman parte del lenguaje
            print("Una o ambas palabras no pertenecen al lenguaje.")
    else:
        ## eerror al introducir el lenguaje
        print("El lenguaje ingresado no cumple con los requisitos (longitud 2 y caracteres del alfabeto).")


if __name__ == "__main__":
    main()






