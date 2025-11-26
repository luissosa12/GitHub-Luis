from typing import NamedTuple
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
from typing import Optional
from collections import defaultdict
def compra_maxima_minima_provincia(lista_compras: list[Compra], provincia: Optional[str]) -> tuple[float, float]:
    res = []
    for r in lista_compras:
        if r.provincia == provincia or provincia is None:
            res.append(r.total_compra)
    
    maxima_compra = max(res)
    minima_compra = min(res)
    tupla = (maxima_compra, minima_compra)

    return tupla
#-------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 3:
from collections import defaultdict
def hora_menos_afluencia(lista_compras: list[Compra]) -> tuple[str, int]:
    res = defaultdict(int)
    for r in lista_compras:
        res[r.fecha_llegada.hour] += 1
    
    hora_menos_clientes = min(res.items(), key=lambda t:t[1])

    return hora_menos_clientes
#-------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 4:
from collections import defaultdict
def supermercados_mas_facturacion(lista_compras: list[Compra], n: int = 3) -> list[tuple[int, tuple[str, float]]]:
    res = defaultdict(float)
    for r in lista_compras:
        res[r.supermercado] += r.total_compra
    
    ordenado_por_precio_decreciente = sorted(res.items(), key=lambda t:t[1], reverse=True)
    #----------
    res_2 = []
    posicion = 1
    for supermercado, facturacion in ordenado_por_precio_decreciente:
        res_2.append((posicion, (supermercado, facturacion)))
        posicion += 1
    
    return res_2[:n]
#-------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 5:
def clientes_itinerantes(lista_compras: list[Compra], n: int) -> list[tuple[str, list[str]]]:
    res = defaultdict(set)
    for r in lista_compras:
        res[r.dni].add(r.provincia)
    
    res_2 = []
    for dni, provincias in res.items():
        if len(provincias) > n:
            res_2.append((dni, sorted(provincias)))

    return res_2
#-------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 6:

#-------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 7:
#compras_test.py
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------