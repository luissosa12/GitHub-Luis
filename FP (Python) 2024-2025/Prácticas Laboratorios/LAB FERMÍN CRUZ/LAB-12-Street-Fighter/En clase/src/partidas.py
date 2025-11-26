from typing import NamedTuple
from datetime import datetime
import csv
from parsear_listas import *

Partida = NamedTuple("Partida", [
    ("pj1", str),
    ("pj2", str),
    ("puntuacion", int),
    ("tiempo", float),
    ("fecha_hora", datetime),
    ("golpes_pj1", list[str]),
    ("golpes_pj2", list[str]),
    ("movimiento_final", str),
    ("combo_finish", bool),
    ("ganador", str),
    ])

#1:
def lee_partidas(ruta_fichero: str) -> list[Partida]:
    with open(ruta_fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        partidas = []
        for pj1, pj2, puntuacion, tiempo, fecha_hora, golpes_pj1, golpes_pj2, movimiento_final, combo_finish, ganador in lector:
            pj1 = str(pj1)
            pj2 = str(pj2)
            puntuacion = int(puntuacion)
            tiempo = float(tiempo)
            fecha_hora = datetime.strptime(fecha_hora, '%Y-%m-%d %H:%M:%S')
            golpes_pj1 = parsear_lista_1(golpes_pj1)
            golpes_pj2 = parsear_lista_1(golpes_pj2)
            movimiento_final = str(movimiento_final)
            combo_finish = combo_finish == 1
            ganador = str(ganador)

            tupla = Partida(pj1, pj2, puntuacion, tiempo, fecha_hora, golpes_pj1, golpes_pj2, movimiento_final, combo_finish, ganador)
            partidas.append(tupla)
    return partidas

#2:
def victoria_mas_rapida(partidas:list[Partida]) -> tuple[str, str, float]:
    mas_rapida = None
    for p in partidas:
        if mas_rapida == None or p.tiempo < mas_rapida.tiempo:
            mas_rapida = p
    return[(mas_rapida.pj1, mas_rapida.pj1, mas_rapida.tiempo)]

#3:
def top_ratio_medio_personajes(partidas: list[Partida], n: int) -> list[str]:
    pass