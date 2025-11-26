from typing import NamedTuple, List, Optional, Dict 
from datetime import datetime, date, time 
import csv 
from collections import defaultdict 
 
Piloto = NamedTuple("Piloto", [("nombre", str),("escuderia", str)]) 
 
CarreraFP = NamedTuple("CarreraFP",[ 
            ("fecha_hora",datetime),  
            ("circuito",str),                     
            ("pais",str),  
            ("seco",bool), # True si el asfalto estuvo seco, False si estuvo mojado 
            ("tiempo",float),  
            ("podio", list[Piloto])]) 

#----------------------------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 1: -> Recibe  la  ruta  de  un  fichero  CSV  y  devuelve  una  lista  de  tuplas  de  tipo  CarreraFP 
#                conteniendo todos los datos almacenados en el fichero. 
#                (1 punto) 
def lee_carreras(ruta_fichero: str) -> list[CarreraFP]: 
    res = []
    with open(ruta_fichero, 'r', encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=',')
        next(lector)

        for fecha_hora, circuito, pais, asfalto, tiempo, primero_nombre, primero_escuderia, segundo_nombre, segundo_escuderia, tercero_nombre, tecero_escuderia in lector:
            fecha_hora = datetime.strptime(fecha_hora.strip(), "%Y-%m-%d %H:%M")
            circuito = str(circuito.strip())
            pais = str(pais.strip())
            seco = bool(asfalto.strip().upper() == "SECO")
            tiempo = float(tiempo.strip())
            podio = [Piloto(primero_nombre.strip(), primero_escuderia.strip()),
                     Piloto(segundo_nombre.strip(), segundo_escuderia.strip()),
                     Piloto(tercero_nombre.strip(), tecero_escuderia.strip())]
            tupla = CarreraFP(fecha_hora, circuito, pais, seco, tiempo, podio)
            res.append(tupla)
    
    return res

#----------------------------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 2: -> Devuelve el tiempo máximo (en días) que nombre_piloto estuvo sin ganar una 
#                carrera. Es decir, el número máximo de días transcurridos entre dos carreras 
#                ganadas  por  el  piloto.  Si  el  piloto  no  ha  ganado  al  menos  dos  carreras,  la  función debe devolver None.
#                (1,5 puntos)
def maximo_dias_sin_ganar(carreras: List[CarreraFP], nombre_piloto: str) -> Optional[int]:
    # 1. Extraer fechas en las que el piloto ganó
    fechas_victorias = []
    for carrera in carreras:
        if carrera.podio and carrera.podio[0].nombre == nombre_piloto:
            fechas_victorias.append(carrera.fecha_hora)

    # 2. Si no hay al menos 2 victorias, devolver None
    if len(fechas_victorias) < 2:
        return None

    # 3. Ordenar fechas de victoria cronológicamente
    fechas_victorias.sort()

    # 4. Calcular máximos días sin ganar
    max_dias = 0
    for i in range(1, len(fechas_victorias)):
        dias_sin_ganar = (fechas_victorias[i] - fechas_victorias[i - 1]).days
        if dias_sin_ganar > max_dias:
            max_dias = dias_sin_ganar

    return max_dias

#----------------------------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 3: -> Devuelve  un  diccionario  que  a  cada  circuito  le  hace  corresponder  el  nombre  del 
#                piloto que más veces ha estado en el podio en ese circuito.
#                (1,5 puntos)
def piloto_mas_podios_por_circuito(carreras: List[CarreraFP]) -> Dict[str, str]:
    conteo = defaultdict(int)

    # 1. Contar cada aparición en el podio por circuito y piloto
    for carrera in carreras:
        for piloto in carrera.podio:
            clave = (carrera.circuito, piloto.nombre)
            conteo[clave] += 1

    # 2. Buscar el piloto con más podios por circuito
    resultado = {}
    for (circuito, piloto), veces in conteo.items():
        if circuito not in resultado or conteo[(circuito, piloto)] > conteo[(circuito, resultado[circuito])]:
            resultado[circuito] = piloto

    return resultado

#----------------------------------------------------------------------------------------------------------------------------------------------
