from typing import NamedTuple, Optional
from datetime import datetime
from datetime import date

Compra = NamedTuple('Compra',
                    [('dni', str),
                     ('supermercado', str),
                     ('provincia', str),
                     ('fecha_llegada', datetime),
                     ('fecha_salida', datetime),
                     ('total_compra', float)]
                    )
#-------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 1:
import csv

def lee_compras(ruta_fichero: str) -> list[Compra]:
    res = []
    with open(ruta_fichero, 'r', encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=',')
        next(lector)
        for dni, supermercado, provincia, fecha_llegada, fecha_salida, total_compra in lector:
            fecha_llegada = datetime.strptime(fecha_llegada, '%d/%m/%Y %H:%M').date()
            fecha_salida = datetime.strptime(fecha_salida, '%d/%m/%Y %H:%M').date()
            total_compra = float(total_compra)
            tupla = Compra(dni, supermercado, provincia, fecha_llegada, fecha_salida, total_compra)
            res.append(tupla)
    return res
#-------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 2:
def compra_maxima_minima_provincia(lista: list[Compra], provincia: Optional[str]) -> tuple[float, float]:
    res = []
    for r in lista:
        if r.provincia == provincia or provincia is None:
            res.append(r.total_compra)
    
    maxima_compra = max(res)
    minima_compra = min(res)

    return tuple(maxima_compra, minima_compra)
#-------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 3:
from collections import defaultdict

def hora_menos_afluencia(lista: list[Compra]) -> tuple[str, int]:
    res = defaultdict(int)
    for r in lista:
        res[r.fecha_llegada.hour] += 1

    minima = min(res.items(), key = lambda x:x[1])

    return minima
#-------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 4:
def supermercados_mas_facturacion(lista: list[Compra], n: int = 3) -> list[tuple[int, tuple[str, float]]]:
    res = defaultdict(float)
    for r in lista:
        res[r.supermercado] += r.total_compra

    ordenada = sorted(res.items(), key = lambda x:x[1], reverse = True)

    posicion = 1
    res2 = []
    for supermercado, facturacion in ordenada:
        res2.append((posicion, (supermercado, facturacion)))
        posicion += 1

    return res2[:n]
#-------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 5:
