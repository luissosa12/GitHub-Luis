# -*- coding: utf-8 -*-
'''
Created on 30 oct. 2018

@author: mateosg & riquelme & reinaqu
'''
import csv
import math
from collections import Counter
from matplotlib import pylab as plt

def lee_fichero(fichero):
    '''
    Cabecera del fichero:
    name,state,city,address,postalCode,latitude,longitude
    Función que lee el fichero y devuelve una lista de tuplas 
    (name, state, city, address,postalCode,latitude,longitude). 
    Use la función next para saltar la primera línea.
    '''
    with open(fichero, 'r', encoding="utf-8") as f:
        lector = csv.reader(f)
        next(lector)
        registros = [(nom,st,ci,direc,cp,float(lat),float(long)) for nom,st,ci,direc,cp,lat,long in lector]
    return registros
    pass

def nombres_restaurantes(registros):
    '''
       Recibe:
        * registros: lista de tuplas (name, state, city, address,postalCode,latitude,longitude)
       Devuelve:
        * Una lista con los nombres de las cadenas de restaurantes (sin repetir). 
    '''
    restaurantes= {nom for nom,_,_,_,_,_,_ in registros}
    return list(restaurantes)
    pass

def restaurantes_en_estado(registros,estado):
    '''
       Recibe:
        * registros: lista de tuplas (name, state, city, address,postalCode,latitude,longitude)
        * estado: nombre de un estado
       Devuelve:
        * Una lista en orden alfabético los nombres de las cadenas de restaurantes (sin repetir) 
         que tienen local en ese estado.
    ''' 
    restaurantes= {nom for nom,st,_,_,_,_,_ in registros if st == estado}
    return list(restaurantes)
    pass

def porc_rest_nombre(registros, nombre):
    '''
       Recibe:
        * registros: lista de tuplas (name, state, city, address,postalCode,latitude,longitude)
        * nombre: nombre de unrestaurante
       Devuelve:
        * Devuelve el porcentaje de restaurantes de ese nombre que hay en el fichero.
    '''
    total_nombre = 0
    for nom,_,_,_,_,_,_ in registros:
        if nom==nombre:
            total_nombre += 1
    return total_nombre*100/len(registros)
    pass


def contar_restaurantes (registros):
    '''
       Recibe:
        * registros: lista de tuplas (name, state, city, address,postalCode,latitude,longitude)
       Devuelve:
        * Devuelve un diccionario que asocia a cada restaurante, el número de restaurantes de ese nombre.
    '''  
    lista = [nom for nom,_,_,_,_,_,_ in registros]
    c = Counter(lista)
    return dict(c)
    pass
  
def rest_mayor_porc(registros):
    '''
       Recibe:
        * registros: lista de tuplas (name, state, city, address,postalCode,latitude,longitude)
       Devuelve:
        * Devuelve  la cadena con mayor número de restaurantes y su
          porcentaje respecto al total.
    '''
    restaurantes = contar_restaurantes(registros)
    rest_mayor = max(restaurantes, key=restaurantes.get)
    return rest_mayor, porc_rest_nombre(registros, rest_mayor)
    pass
    
def distancia(coordenadas1,coordenadas2):
    '''
       Recibe:
        * coordenadas1: tupla (latitud, longitud), que respresenta las coordenadas de un punto
        * coordenadas2: tupla (latitud, longitud), que respresenta las coordenadas de otro punto 
       Devuelve:
        * Devuelve la distancia euclídea entre esas dos coordenadas. La distancia euclídea se 
          define como la raíz cuadrada de la diferencia de coordenadas al cuadrado
        
    '''
    return math.sqrt((coordenadas2[0]-coordenadas1[0])**2+(coordenadas2[1]-coordenadas1[1])**2)
    pass

def rest_cercanos(registros,coordenadas,radio=0.5):
    '''
       Recibe:
        * registros: registros: lista de tuplas (name, state, city, address,postalCode,latitude,longitude)
        * coordenadas: tupla (latitud, longitud), que respresenta las coordenadas de un punto
        * radio: Número real que representa el radio en kilómetros en el que deben estar situados
            los restaurantes buscados
       Devuelve:
        * Devuelve una lista de tuplas (distancia, nombre, ciudad, dirección) ordenada por distancia
          con todos los restaurantes que se encuentran a una distancia menor que la dada por el valor
          radio del punto definido por las coordenadas dadas como parámetro
        
    '''
    lista = [(distancia(coordenadas, (lat,long)),nom,ciu,dir) for nom,_,ciu,dir,_,lat,long in registros
             if distancia(coordenadas, (lat,long)) <= radio]
    lista.sort()
    return lista
    pass
   
       

def porc_por_rest(registros):
    '''
       Recibe:
        * registros: registros: lista de tuplas (name, state, city, address,postalCode,latitude,longitude)
       Devuelve:
        * Devuelve un diccionario que tiene como clave el nombre del restaurante 
          y como valor, porcentaje de presencia del mismo
    '''
    dicc={nom:porc_rest_nombre(registros, nom) for nom in nombres_restaurantes(registros)}
    return dicc
    pass
    
    

def histograma_porcentajes(registros):
    '''
       Recibe:
        * registros: registros: lista de tuplas (name, state, city, address,postalCode,latitude,longitude)
       Efecto lateral:
        Dibuja un histograma en el que el eje de abcisas contiene los nombres de los diez restaurantes más presentes
        y el de ordenadas, el porcentaje de aparición. Para el dibujo use las siguientes líneas:
    
        plt.title(titulo)
        indice = range(len(l_restaurantes))
        plt.bar(indice,l_porcentajes)
        plt.xticks(indice, l_restaurantes, fontsize=8, rotation='vertical')
    '''
    dicc = porc_por_rest(registros)
    restaurantes_ord = sorted(dicc, key=dicc.get,reverse=True)
    l_restaurantes = restaurantes_ord[0:10]
    l_porcentajes =[dicc[nom] for nom in l_restaurantes]
    titulo="Restaurantes con mayor representacion"
    plt.title(titulo)
    indice = range(len(l_restaurantes))
    plt.bar(indice,l_porcentajes)
    plt.xticks(indice, l_restaurantes, fontsize=8, rotation='vertical')
    plt.show()
    pass


