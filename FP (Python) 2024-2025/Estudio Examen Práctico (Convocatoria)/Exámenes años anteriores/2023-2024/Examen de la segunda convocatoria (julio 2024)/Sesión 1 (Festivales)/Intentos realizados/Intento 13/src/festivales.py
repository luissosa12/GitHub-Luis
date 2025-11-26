from typing import NamedTuple, List, Dict, Tuple, Optional, Set 
from datetime import datetime, date, time 
from collections import defaultdict, Counter 
import csv 
  
Artista = NamedTuple("Artista",      
                        [("nombre", str),  
                        ("hora_comienzo", time),  
                        ("cache", int)]) 
 
Festival = NamedTuple("Festival",  
                        [("nombre", str), 
                        ("fecha_comienzo", date), 
                        ("fecha_fin", date), 
                        ("estado", str),                       
                        ("precio", float), 
                        ("entradas_vendidas", int), 
                        ("artistas", List[Artista]), 
                        ("top", bool) 
                    ])

#---------------------------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 1: -> recibe una cadena de texto con la ruta de un fichero csv, y devuelve una lista de
#                tuplas Festival con la información contenida en el fichero. La lista de festivales devuelta debe estar
#                ordenada de manera ascendente por fecha de comienzo de los mismos.
#                (1.25 puntos)
def lee_festivales (ruta_fichero: str) -> List[Festival]: 
    res = []
    with open(ruta_fichero, 'r', encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=',')
        next(lector)

        for nombre, fecha_comienzo, fecha_fin, estado, precio, entradas_vendidas, artistas, top in lector:
            nombre = str(nombre.strip())
            fecha_comienzo = datetime.strptime(fecha_comienzo.strip(), "%Y-%m-%d").date()
            fecha_fin = datetime.strptime(fecha_fin.strip(), "%Y-%m-%d").date()
            estado = str(estado.strip().upper()) #PLANIFICADO, CELEBRADO, CANCELADO
            precio = float(precio.strip())
            entradas_vendidas = int(entradas_vendidas.strip())
            artistas = parsea_list_artistas(artistas.strip())
            top = bool(top.strip().upper() == "SÍ")

            tupla = Festival(nombre, fecha_comienzo, fecha_fin, estado, precio, entradas_vendidas, artistas, top)
            res.append(tupla)

    return sorted(res, key=lambda x:x.fecha_comienzo)

#FUNCIONES AUXILIARES: 
def parsea_artista(cadena: str) -> Artista: 
    if len(cadena.strip()) > 0:
        trozos = cadena.strip().split("_")

        nombre = str(trozos[0].strip())
        hora_comienzo = datetime.strptime(trozos[1].strip(), "%H:%M").time()
        cache = int(trozos[2].strip())

        return Artista(nombre, hora_comienzo, cache)
    else:
        return []
    
def parsea_list_artistas(cadena: str) -> List[Artista]: 
    if len(cadena.strip()) > 0:
        trozos = cadena.strip().split("-")
        return [parsea_artista(trocito) for trocito in trozos]
    else:
        return []
    
#---------------------------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 2: -> esta función devuelve el importe total facturado de los festivales que se han
#                celebrado entre dos fechas dadas. La función recibe una lista de tuplas de tipo Festival y dos fechas,
#                cuyos valores por defecto son None. La función devuelve un número real con el total facturado por los
#                festivales celebrados entre las dos fechas dadas. Si la fecha inicial es None se hace el cálculo sin limitar
#                la fecha mínima de los festivales. Si la fecha final es None se hace el cálculo sin limitar la fecha máxima
#                de los festivales. Para calcular el total facturado por festival hay que multiplicar el número de entradas
#                por el precio de la entrada del festival. Nota: tenga en cuenta que la función debe tomar la facturación
#                de los festivales con estado celebrado en el rango de fechas, es decir, solo se tendrán en cuenta
#                aquellos festivales que empiezan y acaban dentro del rango de fechas.
#                (1.25 puntos)
def total_facturado(festivales: List[Festival], fecha_ini: Optional[date]=None, fecha_fin: Optional[date]=None) -> float: 
    res = 0
    
    for f in festivales:
        if (f.estado == "CELEBRADO") and (fecha_ini is None or f.fecha_comienzo >= fecha_ini) and (fecha_fin is None or f.fecha_fin <= fecha_fin):
            res += (f.entradas_vendidas * f.precio)

    return res

#---------------------------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 3: -> recibe una lista de tuplas de tipo Festival y devuelve una tupla compuesta por un
#                número entero y una cadena de texto, que representan el número de festivales y el nombre del artista
#                que haya participado en más festivales que finalmente se han celebrado, respectivamente.
#                (1.75 puntos)
def artista_top(festivales: List[Festival]) -> Tuple[int, str]: 
    res = defaultdict(int)

    for f in festivales:
        for a in f.artistas:
            if f.estado == "CELEBRADO":
                res[a.nombre] += 1

    max_artista = max(res.items(), key=lambda x:x[1])

    return max_artista[1], max_artista[0]

#---------------------------------------------------------------------------------------------------------------------------------------------
#*********************************************************************************************************************************************
#EJERCICIO 4: -> recibe una lista de tuplas de tipo Festival y devuelve una cadena de
#                texto que será el nombre del mes, en español, de aquel que haya obtenido un mayor beneficio medio.
#                Es decir, cada festival tiene un beneficio que se calcula a partir de las entradas vendidas menos el caché
#                de los artistas. Pues esta función debe calcular el beneficio medio que se ha obtenido cada mes y
#                devolver aquel cuyo beneficio haya sido el mayor. Nota: Si hubiera algún festival que se celebra entre
#                dos meses, se imputará al mes en el que comienza. Por ejemplo, un festival que comience el 30 de junio
#                y acabe el 4 de julio será imputado al mes de junio.
#                (2.25 puntos)
def mes_mayor_beneficio_medio(festivales: List[Festival]) -> str:
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
             "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    beneficios_por_mes = defaultdict(list)

    for f in festivales:
        cache_total = sum(a.cache * 1000 for a in f.artistas)
        beneficio = f.entradas_vendidas * f.precio - cache_total
        mes = f.fecha_comienzo.month
        beneficios_por_mes[mes].append(beneficio)
    
    medias = {
        mes: sum(beneficios) / len(beneficios)
        for mes, beneficios in beneficios_por_mes.items()
    }

    mes_max = max(medias, key=medias.get)

    return meses[mes_max - 1]

#OTRA FORMA: 
from statistics import mean

def mes_mayor_beneficio_medio(festivales: List[Festival]) -> str:
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
             "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    beneficios_por_mes = defaultdict(list)

    for f in festivales:
        cache_total = sum(a.cache * 1000 for a in f.artistas)
        beneficio = f.entradas_vendidas * f.precio - cache_total
        mes = f.fecha_comienzo.month
        beneficios_por_mes[mes].append(beneficio)
    
    medias = {mes: mean(beneficios) for mes, beneficios in beneficios_por_mes.items()}
    mes_max = max(medias, key=medias.get)

    return meses[mes_max - 1]

#---------------------------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 5: -> recibe una lista de tuplas de tipo Festival y dos cadenas de texto festi1 y
#                festi2, y devuelve una lista con los nombres de aquellos artistas que se repitan entre festi1 y
#                festi2. Nota: se considera que no hay festivales repetidos.
#                (1.75 puntos)
def artistas_comunes(festivales: List[Festival], festi1: str, festi2: str) -> List[str]: 
    res = set()
    res2 = set()
    
    for f in festivales:
        for a in f.artistas:
            if f.nombre == festi1:
                res.add(a.nombre)
            if f.nombre == festi2:
                res2.add(a.nombre)
    
    return list(res.intersection(res2))

#---------------------------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 6: -> cada festival tiene una duración de entre 2 y 8 días. Implemente una
#                función que, recibiendo una lista de tuplas de tipo Festival, y un número n cuyo valor por defecto
#                será 3, devuelva un diccionario en el que las claves son las duraciones de los festivales, y los valores
#                listas con los nombres de los n festivales de más calidad (ordenados de más a menos calidad). La
#                calidad de un festival viene dada por el ratio entre entradas vendidas y número de artistas participantes
#                en el festival. Cuanto más alto es este ratio, más calidad tiene el festival.
#                (1.75 puntos)
def festivales_top_calidad_por_duracion(festivales: List[Festival], n: int=3) -> Dict[int, List[str]]: 
    res = defaultdict(list)
    
    for f in festivales:
        duracion = (f.fecha_fin - f.fecha_comienzo).days
        calidad = (f.entradas_vendidas / len(f.artistas))
        res[duracion].append((f.nombre, calidad))

    res2 = dict()
    for duracion, nombre_calidad in res.items():
        lista_ordenada = sorted(nombre_calidad, key=lambda x:x[1], reverse=True)[:n]
        res2[duracion] = [nombre for nombre, _ in lista_ordenada]

    return res2

#---------------------------------------------------------------------------------------------------------------------------------------------
