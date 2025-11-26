from typing import NamedTuple
import csv
from datetime import datetime, date
#----------------------------------------------------------------------------------------------------------------------
from parsear_listas import parsea_lista_1
#----------------------------------------------------------------------------------------------------------------------
Pelicula = NamedTuple(
    "Pelicula",
    [("fecha_estreno", date), 
    ("titulo", str), 
    ("director", str), 
    ("generos",list[str]),
    ("duracion", int),
    ("presupuesto", int), 
    ("recaudacion", int), 
    ("reparto", list[str])
    ]
)
#----------------------------------------------------------------------------------------------------------------------
#1:
def lee_peliculas(ruta_fichero: str) -> list[Pelicula]:
    with open(ruta_fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f, delimiter = ';')
        next(lector)
        peliculas = []
        for fecha_estreno, titulo, director, generos, duracion, presupuesto, recaudacion, reparto in lector:
            fecha_estreno = datetime.strptime(fecha_estreno, "%d/%m/%Y").date()
            titulo = str(titulo)
            director = str(director)
            generos = generos.split(',')
            duracion = int(duracion) 
            presupuesto = int(presupuesto)
            recaudacion = int(recaudacion)
            reparto = reparto.split(',')

            tupla = Pelicula(fecha_estreno, titulo, director, generos, duracion, presupuesto, recaudacion, reparto)
            peliculas.append(tupla)
    return peliculas
#----------------------------------------------------------------------------------------------------------------------
#2:
def pelicula_mas_ganancias(peliculas:list[Pelicula], genero:str = None) -> tuple[str, int]:
    peliculas_genero = []

    #Filtrar por género:
    for p in peliculas:
        if genero == None or genero in p.genero:
            peliculas_genero.append( (p.titulo, p.recaudacion - p.presupuesto))

    #Obtener máximo por ganancias:
    maximo = max(peliculas_genero, key = lambda t:t[1])
    return maximo
#----------------------------------------------------------------------------------------------------------------------
#3:
def media_presupuesto_por_genero(peliculas:list[Pelicula]) -> dict[str, int]:
    #Obtener diccionario de media de presupuestos por género
    dic = presupuestos_por_genero(peliculas)

    #Obtener diccionario de media de presupuestos por género
    res = dict()
    for genero, lista_presupuestos in dic.items():
        res[genero] = sum(lista_presupuestos) / len(lista_presupuestos)
    return res

#3 (2):
def presupuestos_por_genero(peliculas: list[Pelicula]) -> dict[str, list[int]]:
    res = dict()
    for p in peliculas:
        for genero in p.generos:
            if genero not in res:
                res[genero] = [p.presupuesto]
            else:
                res[genero].append(p.presupuesto)
    return res