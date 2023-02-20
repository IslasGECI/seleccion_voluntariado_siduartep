<a href="https://www.islas.org.mx/"><img src="https://www.islas.org.mx/img/logo.svg" align="right" width="256" /></a>
# Selección de voluntario para Ciencia de Datos en GECI, 2023

Para usar este repo como plantilla debemos hacer lo siguiente:

1. Presiona el botón verde que dice _Use this template_
1. Selecciona como dueño a la organización IslasGECI
1. Agrega el nombre del nuevo módulo de python
1. Presiona el botón _Create repository from template_
1. Reemplaza `seleccion_voluntariado_2023` por el nombre del nuevo módulo en:
    - `Makefile`
    - `pyproject.toml`
    - `tests\test_transformations.py`
1. Renombra el archivo `seleccion_voluntariado_2023\transformations.py` al nombre del primer archivo del
   nuevo módulo
1. Cambia la descripción del archivo `seleccion_voluntariado_2023\__init__.py`
1. Renombra el directorio `seleccion_voluntariado_2023` al nombre del nuevo módulo
1. Cambia el `codecov_token` del archivo `Makefile`

Los archivos del nuevo módulo los agregarás en la carpeta que antes se llamaba
`seleccion_voluntariado_2023` y las pruebas en la carpeta `tests`.
