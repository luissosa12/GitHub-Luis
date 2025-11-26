from collections import namedtuple
import math

Coordenadas = namedtuple('Coordenadas', 'latitud, longitud')

def calcular_distancia(c1, c2):
    distancia = math.sqrt((c1.latitud-c2.latitud)**2 + (c1.longitud-c2.longitud)**2)
    return distancia

def calcular_media_coordenadas(lista_coordenadas):
    suma_lat, suma_lon = 0, 0
    for l in lista_coordenadas:
        suma_lat += l.latitud
        suma_lon += l.longitud
    return Coordenadas(
            suma_lat / len(lista_coordenadas),
            suma_lon / len(lista_coordenadas),
        )

