def buscar(principio, lenguaje, cardenalidad, longitud, w, nivel):
    pertenece = nivel
    for i in range(longitud):
        if w.find(lenguaje[i], principio) == principio:
            pertenece += 1
            if principio + cardenalidad[i] == len(w):
                return pertenece
            next_level = buscar(principio + cardenalidad[i], lenguaje, cardenalidad, longitud, w, pertenece)
            if next_level > -1:
                return next_level
            else:
                pertenece -= 1
    return -1


def operacion_w1_w2(w1, w2):
    concatenacion = w1 + w2
    inversa = concatenacion[::-1]
    resultado = inversa * 2
    return resultado


def main():
    sigma = input("Ingresa el alfabeto separado por espacios:\nEjemplo 'a b c s'\nΣ: ")

    l = input("Ingresa el lenguaje separado por comas\nEjemplo 'aa,ca,de,ga,fa'\nL = ")

    if all(len(s) == 2 and all(c in sigma for c in s) for s in l.split(',')):
        l_separado = l.split(',')
        lenguaje = l_separado.copy()
        cardenalidad = [len(s) for s in l_separado]
        longitud = len(lenguaje)

        w1 = input("Ingresa la primera palabra:\nw1 = ")
        w2 = input("Ingresa la segunda palabra:\nw2 = ")

        pertenece_w1 = buscar(0, lenguaje, cardenalidad, longitud, w1, 0)
        pertenece_w2 = buscar(0, lenguaje, cardenalidad, longitud, w2, 0)

        if pertenece_w1 > -1 and pertenece_w2 > -1:
            print(f"w1 pertenece a L{pertenece_w1}")
            print(f"w2 pertenece a L{pertenece_w2}")
            resultado = operacion_w1_w2(w1, w2)
            print(f"[(w1.w2)^(-1)]^2 = {resultado}")
        else:
            print("Una o ambas palabras no pertenecen al lenguaje.")
    else:
        print("El lenguaje ingresado no cumple con los requisitos (longitud 2 y caracteres del alfabeto).")


if __name__ == "__main__":
    main()






