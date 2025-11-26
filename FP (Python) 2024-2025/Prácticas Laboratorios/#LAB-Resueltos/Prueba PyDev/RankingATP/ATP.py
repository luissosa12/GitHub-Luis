'''
Created on 5 dic. 2018

@author: Juanmi
'''
import csv
import sys
from collections import defaultdict, namedtuple
from matplotlib import pyplot as plt


Jugador = namedtuple('Jugador', 'nombre, puntos')

def lee_temporada(temporada, ruta='./data/', prefijo='TOP25-ATP-', extension='.csv'):
    fichero = ruta + prefijo + str(temporada) + extension
    with open(fichero, 'r') as f:
        reader = csv.reader(f)
        lista_jugadores = [Jugador(nombre, int(puntos)) for nombre, puntos in reader]
    return lista_jugadores

def lee_temporadas(lista_temporadas, ruta='./data/', prefijo='TOP25-ATP-', extension='.csv'):
    dicc_temporadas=dict()
    for temporada in lista_temporadas:
        lista_ATPtemporada = lee_temporada(temporada)
        dicc_temporadas[temporada]=lista_ATPtemporada
    return dicc_temporadas

def lee_temporadas2(lista_temporadas, ruta='./data/', prefijo='TOP25-ATP-', extension='.csv'):
    dicc_temporadas={temporada:lee_temporada(temporada) for temporada in lista_temporadas}
    return dicc_temporadas

def getConjJugadores(dicc_temporadas):
    
    pass
def main():
    lista_ATP2008=lee_temporada(2008)
    print(lista_ATP2008)
    temporadas = range(2008, 2018)
    dicc_totalTemporadas = lee_temporadas(temporadas)
    for temporada in dicc_totalTemporadas:
        print ("Temporada {}:{}...".format(temporada, 
dicc_totalTemporadas[temporada][:2]))
if __name__ == '__main__':
    main()