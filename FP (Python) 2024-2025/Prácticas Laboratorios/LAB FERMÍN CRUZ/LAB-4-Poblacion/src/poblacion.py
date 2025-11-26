from matplotlib import pyplot as plt

#Importamos la namedtuple para poder usarla:
from collections import namedtuple
#Definimos la namedtuple con las variables que tenemos:
RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')

#Importamos el csv para poder leerlo:
import csv
#Definimos la función lee_poblaciones y le asignamos una ruta_fichero para que sea de forma genérica esta ruta, ej:
#   cuando llamemos a la funcion lee_ficheros debemos de indicarle entre paréntesis la ruta del fichero que
#   queramos leer:
def lee_poblaciones(ruta_fichero):
    with open(ruta_fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
#Ahora creamos una lista vacía para que la vayamos rellenando según los datos que le introduzcamos:
        lista = []
#Ahora creamos un bucle for para que dentro del fichero, la columna año y censo la convierta
#   de texto (str) a número entero (int):
        for pais, codigo, año, censo in lector:
            año = int(año)
            censo = int(censo)
#Ahora definimos la tupla según los parámetros indicados anteriormente con sus respectivos nombres:
            tupla = RegistroPoblacion(pais, codigo, año, censo)
#Ahora sólo queda añadir a la lista VACÍA los valores fila a fila del fichero de texto con formato tupla (namedtuple)
            lista.append(tupla)


def calcula_paises(poblaciones):
#Creamos un conjunto vacío (ya que no queremos que se repitan los nombres), los conjuntos eliminan
#   los valores repetidos en una misma lista) donde almacenar las tuplas:
    conjunto = set()
#Realizamos un bucle for para leer linea a linea cada país de las poblaciones y lo guarde en e,
#   si usaramos for e in conjunto: NO LEERÍAMOS NADA, ya que el conjunto creado esta vacío.
    for e in poblaciones:
#Añadimos al "conjunto" el tipo de e, en este caso el país:
        conjunto.add(e.pais)
#Ahora obtenemos una lista ordenada alfabéticamente con los elementos del conjunto gracias al método "sorted":
    return sorted(conjunto)

        #Si me pidieran una lista sin más (sin ordenar):
        #   return list(conjunto)


def filtra_por_pais(poblaciones, nombre_o_codigo):
#De nuevo, creamos una lista_2 vacía donde se añadirán las tuplas que vayamos creando:
    lista_2 = []
#Añadimos un bucle for para que recorra todos los elementos de poblaciones y lo guarde en p:
    for p in poblaciones:
#Añadimos las condiciones necesarias: si el país almacenado en p (p.pais) es igual a su nombre o a su código,
#   Ó al revés, que el código almacenado en p (p.codigo) es igual a su nombre o a su código, devuelva una tupla
#   con el país con su año o su censo (código):
        if p.pais == nombre_o_codigo or p.codigo == nombre_o_codigo:
            tupla_2 = (p.año, p.censo)
            lista_2.append(tupla_2)   
    return lista_2


