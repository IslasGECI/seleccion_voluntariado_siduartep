def generar_codigo(nombre_ave):
    """"
    Este algoritmo recibe el nombre de un ave en formato cadena de texto (STRING) y lo convierte en un código de acuerdo con las siguientes reglas:
    """
    #Establecemos que el input esté en mayúsculas, reemplazamos los guiones con un guión y espacio porque es importante mantener el formato de guión y del mismo modo es importante crear la separación para terminar así con una separación de palabras
    palabras = nombre_ave.upper().replace('-','- ').split()

    # Regla 1: Si el nombre consta de una sola palabra, formamos el código de las letras iniciales, hasta cuatro.
    if len(palabras) == 1:
        codigo = palabras[0][:4]

    # Regla 2: Si hay dos palabras en el nombre, componemos el código de las dos primeras letras de cada palabra.
    elif len(palabras) == 2:
        codigo = palabras[0][:2] + palabras[1][:2]

    # Regla 3: Para los nombres de tres palabras donde solo las dos últimas palabras se unen con guión, el código usa las primeras dos letras de la primera palabra y la primera letra de cada una de las dos últimas palabras.
    elif len(palabras) == 3 and '-' in palabras[1]:
        codigo = palabras[0][:2] + palabras[1][0] + palabras[2][0]

    # Regla 4: Para otros nombres con tres palabras, el código toma una letra de cada una de las dos primeras palabras y dos de la última palabra.
    elif len(palabras) == 3:
        codigo = palabras[0][0] + palabras[1][0] + palabras[2][:2]

    # Regla 5: Para nombres de cuatro palabras, el código toma una letra de cada palabra.
    elif len(palabras) == 4:
        codigo = palabras[0][0] + palabras[1][0] + palabras[2][0] + palabras[3][0]

    return codigo
