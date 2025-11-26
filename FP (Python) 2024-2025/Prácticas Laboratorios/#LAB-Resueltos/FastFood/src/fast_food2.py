'''
Created on 1 ago. 2019

@author: Juanmi
'''
import csv
import math
from collections import Counter
from matplotlib import pylab as plt
from builtins import list

def lee_fichero(fichero):
    with open(fichero, 'r', encoding="utf-8") as f:
        lector=csv.reader(f)
        next(lector)
        registros = [(nom,st,ci,direc,cp,float(lat),float(long)) for nom,st,ci,direc,cp,lat,long in lector]
        return registros

def nombres_restaurantes(registros):
    restaurantes= {nom for nom,_,_,_,_,_,_ in registros }
    return list(restaurantes)

def restaurantes_en_estado(registros,estado):
    restaurantes={nom for nom,st,_,_,_,_,_ in registros if st == estado}
    return list(restaurantes)

def porc_rest_nombre(registros, nombre):
    total_nombre = 0
    for nom,_,_,_,_,_,_ in registros:
        if nom==nombre:
            total_nombre += 1
    return total_nombre*100/len(registros)

def contar_restaurantes (registros):
    lista=nombres_restaurantes(registros)
    c=Counter(lista)
    return c

def rest_mayor_porc(registros):
    restaurantes = contar_restaurantes(registros)
    rest_mayor=max(restaurantes, key=restaurantes.get)
    return rest_mayor, porc_por_rest(registros)

def porc_por_rest(registros):
    dicc={nom:porc_rest_nombre(registros, nom) for nom in nombres_restaurantes(registros)}
    return dicc

def distancia(coordenadas1,coordenadas2):
    return math.sqrt((coordenadas2[0]-coordenadas1[0])**2+(coordenadas2[1]-coordenadas1[1])**2)

def rest_cercanos(registros,coordenadas,radio=0.5):
    lista = [(distancia(coordenadas, (lat,long)),nom,ciu,dir) for nom,_,ciu,dir,_,lat,long in registros
             if distancia(coordenadas, (lat,long)) <= radio]
    lista.sort()
    return lista

def histograma_porcentajes(registros):
    dicc = porc_por_rest(registros)
    restaurantes_ord = sorted(dicc, key=dicc.get, reverse=True)
    l_restaurantes = restaurantes_ord[0:10]
    l_porcentajes =[dicc[nom] for nom in l_restaurantes]
    titulo="Restaurantes con mayor representacion"
    plt.title(titulo)
    indice = range(len(l_restaurantes))
    plt.bar(indice,l_porcentajes)
    plt.xticks(indice, l_restaurantes, fontsize=8, rotation='vertical')
    plt.show()
    pass