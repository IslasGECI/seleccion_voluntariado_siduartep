ERROR_DE_TIPO = "EROR: Necesito string"
ERROR_DE_STRING_VACIO = "EROR: string vacío"


def generar_codigo(nombre_ave=""):
    if not isinstance(nombre_ave, str):
        raise ValueError(ERROR_DE_TIPO)
    nombre_ave = nombre_ave.strip()
    if nombre_ave == "":
        raise ValueError(ERROR_DE_STRING_VACIO)
    palabras = nombre_ave.upper().replace("-", "- ").split()
    if len(palabras) == 1:
        codigo = palabras[0][:4]
    elif len(palabras) == 2:
        codigo = palabras[0][:2] + palabras[1][:2]
    elif all(
        [
            len(palabras) == 3,
            "-" in palabras[1],
            "-" not in palabras[0],
            "-" not in palabras[2],
        ]
    ):
        codigo = palabras[0][:2] + palabras[1][0] + palabras[2][0]
    elif len(palabras) == 3:
        codigo = palabras[0][0] + palabras[1][0] + palabras[2][:2]
    elif len(palabras) == 4:
        codigo = palabras[0][0] + palabras[1][0] + palabras[2][0] + palabras[3][0]
    return codigo
