'''
Created on 21 nov. 2018

@author: Juanmi
'''
from os import listdir
import csv
from collections import namedtuple
from datetime import datetime
from sqlalchemy.sql.expression import true

Partido = namedtuple('Partido', 'fecha local goles_local visitante goles_visitante')

def lee_temporada(fichero):
    with open(fichero, 'r', encoding='utf-8') as f:
        lector=csv.reader(f)
        partidos=[Partido(datetime.strptime(fecha,"%d/%m/%Y").date(),local,
                          int(goles_local),visitante,int(goles_visitante)) for fecha,local,goles_local,
                          visitante,goles_visitante in lector]
    return partidos

primera_15_16 = lee_temporada('../data/Primera/15-16.csv')

def lee_competicion(carpeta):
    partidos_total=[]
    for fichero in listdir(carpeta):
        partidos=lee_temporada(carpeta+fichero)
        partidos_total += partidos
    return partidos_total

def aplana(lista_de_lista):
    lista_res=[]
    for lista in lista_de_lista:
        lista_res += lista
    return lista_res

def equipos_participantes(partidos):
    conjunto_equipos=set()
    for p in partidos:
        conjunto_equipos.add(p[1])
        conjunto_equipos.add(p[3])
    return conjunto_equipos

def partidos_por_fechas(partidos, inicio=None, fin=None):
    if inicio == None:
        inicio=min([p.fecha for p in partidos])
    if fin==None:
        fin=max([p.fecha for p in partidos])
    return [p for p in partidos if inicio <= p[0] <= fin]

inicio = datetime(2007, 9, 15).date()
fin = datetime(2008, 7, 1).date()

def estaEnRango(fecha, inicio=None, fin=None):
    if inicio==None and fin==None:
        res=true
    elif inicio==None:
        res=fecha<=fin
    elif fin==None:
        res=inicio<=fecha
    else:
        res=inicio<=fecha<=fin
    return res

def partidos_por_equipos(partidos, equipos):
    partidos_filtrados = list() #partidos_filtrados=[]
    for partido in partidos:
        if partido[1] in equipos or partido[3] in equipos:
            partidos_filtrados.append(partido)
    return partidos_filtrados
    #return [partido for partido in partidos if partido[1] in equipos or partido[3] in equipos]


def calcula_elo(elo_a, elo_b, goles_a, goles_b, k=20):
    ea = 1/(1+10**(elo_b-elo_a)/400)
    eb = 1/(1+10**(elo_a-elo_b)/400)
    if goles_a<goles_b:
        s_a=0
        s_b=1
    elif goles_a>goles_b:
        s_a=1
        s_b=0
    else:
        s_a=0.5
        s_b=0.5
    elo_a = elo_a *(s_a-ea)*k
    elo_b = elo_b *(s_b-eb)*k
    return (elo_a, elo_b)

def muestra_ranking(ranking, limite=None):
    lista=[]
    #solucion 1
    for clave in ranking:
        lista.append((clave, ranking[clave]))
    #solucion 2
    lista = ranking.items()
    lista.sort(reverse=true)
    lista_limitada = [lista[i] for i in range(limite)]
    return lista_limitada

def calcula_ranking_elo(partidos, ranking_previo=dict()):
    equipos=equipos_participantes(partidos)
    if len(ranking_previo.items()==0):
        ranking_previo={equipo:1000 for equipo in equipos}
    partidos.sort()
    for partido in partidos:
        nuevo_eloa, nuevo_elob = calcula_elo(ranking_previo[partido.local], ranking_previo[partido.visitante], 
                                             ranking_previo[partido.goles_local], ranking_previo[partido.goles_visitante])
        ranking_previo[partido.local]=nuevo_eloa
        ranking_previo[partido.visitante]=nuevo_elob
    return ranking_previo

def calcula_rendimiento(equipo, partidos, ranking_elo):
    suma_puntos = 0
    partidos_local = (partido for partido in partidos if partidos.local==equipo)
    partidos_visitante = (partido for partido in partidos if partidos.visitante==equipo)
    for p in partidos_local:
        puntos=0
        if p.goles_local>p.goles_visitante:
            puntos=400
        elif p.goles_local<p.goles_visitante:
            puntos=-400
        suma_puntos=suma_puntos + ranking_elo[p.visitante] + puntos
    for p in partidos_visitante:
        puntos=0
        if p.goles_local<p.goles_visitante:
            puntos=400
        elif p.goles_local>p.goles_visitante:
            puntos=-400
        suma_puntos=suma_puntos + ranking_elo[p.local] + puntos
    return suma_puntos/(len(partidos_local)+len(partidos_visitante))
        
    
