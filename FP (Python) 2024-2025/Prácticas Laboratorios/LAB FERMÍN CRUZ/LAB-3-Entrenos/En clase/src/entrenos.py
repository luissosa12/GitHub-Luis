from datetime import datetime
import csv
from collections import namedtuple

# Definimos el tipo Entreno como una namedtuple
Entreno = namedtuple('Entreno', ['tipo','fechahora', 'ubicacion', 'duracion', 'calorias', 'distancia', 'frecuencia', 'compartido'])

def lee_entrenos(ruta):
    ruta = ("data/entrenos.csv")
    '''
    Recibe la ruta de un fichero en formato CSV codificado en UTF-8
        y devuelve una lista de tuplas de tipo Entreno
    '''
    with open(ruta, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        res = []

        for (tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido) in lector:
            #Convertir el tipo de aquellos campos que no sean str
            tipo = str(tipo)

            fechahora = datetime.strptime(fechahora, '%d/%m/%Y %H:%M')
            
            ubicacion = str(ubicacion)
            duracion = int(duracion)
            calorias = int(calorias)
            distancia = float(distancia)
            frecuencia = int(frecuencia)

            compartido = compartido == 'S'
            #if compartido == 'S':
            #    compartido = True
            #else:
            #    compartido = False
            
            tupla = Entreno(tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido)

            res.append(tupla)
        return res
    
def tipos_entreno(lista_entrenos):
    #Crear un conjunto vacío
    conjunto = set()
    for e in conjunto:
        #Añadir al conjunto el tipo de e
        conjunto.add(e.tipo)
    #Obtener una lista ordenada con los elementos del conjunto
    return sorted(conjunto)

    #Si me piden una lista sin más (sin ordenar):
    # return list(conjunto)

def entrenos_duracion_superior(lista_entrenos, d):
    res = []
    for e in lista_entrenos:
        if e.duracion > d:
            res.append(e)

    return res

def suma_calorias(lista_entrenos, f_inicio, f_fin):
    res = 0
    for e in lista_entrenos:
        if f_inicio <= e.fechahora <= f_fin:
            res += e.calorias
    return res