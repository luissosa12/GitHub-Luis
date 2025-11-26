from typing import NamedTuple
from datetime import datetime
import csv

Compra = NamedTuple('Compra',
                    [('dni', str),
                     ('supermercado', str),
                     ('provincia', str),
                     ('fecha_llegada', datetime),
                     ('fecha_salida', datetime),
                     ('total_compra', float)]
                    )

#1:
def leer_compras(ruta_fichero: str) -> list[Compra]:
    with open (ruta_fichero, encoding = 'utf-8') as f:
        res = []
        lector = csv.reader(f)
        next(lector)
        for dni, supermercado, provincia, fecha_llegada, fecha_salida, total_compra in lector:
            dni = str(dni)
            supermercado = str(supermercado)
            provincia = str(provincia)
            fecha_llegada = datetime.strptime(fecha_llegada, '%d/%m/%Y %H:%M')
            fecha_salida = datetime.strptime(fecha_salida, '%d/%m/%Y %H:%M')
            total_compra = float(total_compra)
            res.append(Compra(dni, supermercado, provincia, fecha_llegada, fecha_salida, total_compra))
        return res

#2:
def compra_maxima_minima_provincia(lista: list[Compra], provincia = None )-> tuple:
    compras = []
    for c in lista:
        if provincia == None or provincia == c.provincia:
            compras.append(c.total_compra)
    res = (max(compras), min(compras))
    return res

#3:
def hora_menos_afluencia(lista: list[Compra]):
    res = {}
    for l in lista:
        if l.fecha_llegada.hour not in res:
           res[l.fecha_llegada.hour] = 0
        res [l.fecha_llegada.hour] += 1
    return min(res.items(), key = lambda r:r[1])

#4:
