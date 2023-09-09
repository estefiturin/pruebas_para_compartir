# Funciones auxiliares
def llenarDiccionario(palabra):
    """Llena un diccionario con el conteo de letras de una palabra."""
    diccionario_palabra = {}
    for letra in palabra:
        if letra in diccionario_palabra:
            diccionario_palabra[letra] += 1
        else:
            diccionario_palabra[letra] = 1
    return diccionario_palabra

def palabrasCompartidas(diccionario1, diccionario2):
    """Verifica las palabras compartidas entre dos diccionarios y las almacena en uno nuevo."""
    compartidas = {clave: diccionario1[clave] for clave in diccionario1 if clave in diccionario2 and diccionario1[clave] == diccionario2[clave]}
    return compartidas

def reemplazarPuntuacion(texto):
    """Reemplaza todos los signos de puntuación en la oración. Solo lo uso en determinados casos"""
    diccionario_puntuacion = {k: '' for k in ',!;?¿.\''}
    for i, j in diccionario_puntuacion.items():
        texto = texto.replace(i, j)
    return texto

def limpiarTexto(texto):
    # Convierte toda la oración
    oracion_limpia = reemplazarPuntuacion(texto.lower())
    oracion_limpia = oracion_limpia.split()
    # Elimina palabras repetidas usando set() ya que no cuentan como anagramas.
    # Utilizo la función sorted() para recuperar el orden de la oración basado en su índice.
    oracion_limpia = sorted(set(oracion_limpia), key=lambda x: oracion_limpia.index(x))
    # Convierte la cadena en una lista dividiéndola y almacena diccionarios de palabras en otra lista. ¡Una lista de diccionarios!
    lista_oracion = [llenarDiccionario(palabra) for palabra in oracion_limpia]
    return oracion_limpia, lista_oracion

### Dificultad Avanzada
def cualesSonAnagramas(oracion):
    """Función que devuelve una lista anidada de palabras que son anagramas entre sí."""
    # Llamo a la función limpiarTexto.
    oracion_limpia, lista_oracion = limpiarTexto(oracion)
    # Crea una lista vacía para almacenar una lista de valores booleanos.
    # El propósito de esto es verificar si hay al menos un anagrama en la oración.
    lista_compartida = []
    #Almaceno apalabras en lista compartida
    for i in range(len(lista_oracion)):
        lista_compartida_individual = []
        for j in range(i + 1, len(lista_oracion)):
            x = lista_oracion[i]
            y = lista_oracion[j]
            palabras_compartidas = palabrasCompartidas(x, y)
            # Compruebo la longitud de las palabras compartidas entre dos palabras y también verifica que no estén vacías ya que reemplazamos las palabras almacenadas por cadenas vacías.
            if len(palabras_compartidas) == len(x) == len(y) and oracion_limpia[i] != oracion_limpia[j]:
                lista_compartida_individual.append(oracion_limpia[j])
                oracion_limpia[j] = ""
        # Después de verificar toda la lista con nuestra palabra "i", comprobamos si la lista_compartida_individual no está vacía. Si no lo está, colocamos la palabra actual "i" como el primer elemento de la lista e insertamos la lista_compartida_individual en la lista principal.
        if lista_compartida_individual != []:
            lista_compartida_individual.insert(0, oracion_limpia[i])
            lista_compartida.append(lista_compartida_individual)
    # Después de agregar nuestra lista_compartida_individual, comprobamos si la lista compartida está vacía (en caso de que no encontremos anagramas).
    if lista_compartida == []:
        lista_compartida.append([])
    return lista_compartida

# Ingreso de la frase por el usuario
frase = input("Ingrese una frase para verificar los anagramas: ")
resultado = cualesSonAnagramas(frase)

if resultado != [[]]:
    print("Las palabras anagramas en la frase son:")
    for grupo in resultado:
        print(", ".join(grupo))
else:
    print("No se encontraron anagramas en la frase ingresada.")

