from typing import NamedTuple, Optional
from datetime import datetime, date

Compra = NamedTuple('Compra',
                    [('dni', str),
                     ('supermercado', str),
                     ('provincia', str),
                     ('fecha_llegada', datetime),
                     ('fecha_salida', datetime),
                     ('total_compra', float)]
                    )
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 1:
import csv

def lee_compras(ruta_fichero: str) -> list[Compra]:
    res = []
    with open(ruta_fichero, 'r', encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=',')
        next(lector)
        for dni, supermercado, provincia, fecha_llegada, fecha_salida, total_compra in lector:
            fecha_llegada = datetime.strptime(fecha_llegada, '%d/%m/%Y %H:%M')
            fecha_salida = datetime.strptime(fecha_salida, '%d/%m/%Y %H:%M')
            total_compra = float(total_compra)
            tupla = Compra(dni, supermercado, provincia, fecha_llegada, fecha_salida, total_compra)
            res.append(tupla)
    return res
#-------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 2:
from collections import defaultdict
def compra_maxima_minima_provincia(lista_compras: list[Compra], provincia : Optional[str]=None) -> tuple[float, float]:
    res = []
    for r in lista_compras:
        if r.provincia == provincia or provincia is None:
            res.append(r.total_compra)

    compra_maxima = max(res)
    compra_minima = min(res)

    tupla = (compra_maxima, compra_minima)

    return tupla
#-------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 3:
def hora_menos_afluencia(lista_compras: list[Compra]) -> tuple[str, int]:
    res = defaultdict(int)
    for r in lista_compras:
        res[r.fecha_llegada.hour] += 1
    
    minimo = min(res.items(), key=lambda t:t[1])

    return minimo
#-------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 4:
def supermercados_mas_facturacion(lista_compras: list[Compra], n: int = 3) -> list[tuple[int, tuple[str, float]]]:
    res = defaultdict(float)
    for r in lista_compras:
        res[r.supermercado] += r.total_compra

    ordenada_por_precio_decreciente = sorted(res.items(), key = lambda t:t[1], reverse = True)
#----------------------------------------
    res2 = []
    posicion = 1
    for supermercado, facturacion in ordenada_por_precio_decreciente:
        res2.append((posicion, (supermercado, facturacion)))
        posicion += 1

    return res2[:n]
#-------------------------------------------------------------------------------------------------------------------------
