# -*- coding: utf-8 -*-
'''
Created on 2 nov. 2018

@author: reinaqu_2
'''
import fast_food2
from fast_food import rest_mayor_porc, porc_por_rest, lee_fichero,\
    nombres_restaurantes, restaurantes_en_estado, porc_rest_nombre,\
    contar_restaurantes, distancia, rest_cercanos, histograma_porcentajes
################################################################
#  Tests
################################################################
def mostrar_numerado(iterable):
    for num, elem in enumerate(iterable):
        print (num, "--", elem)

def test_lee_fichero(registros):
    print("Se han leido ", len (registros), "datos")
    mostrar_numerado(registros)
    
def test_nombres_restaurantes(registros):
    restaurantes = nombres_restaurantes(registros)
    print ("Hay ", len(restaurantes), " cadenas de restaurantes distintas")
    mostrar_numerado(restaurantes)

def test_restaurantes_en_estado(registros, estado): 
    print('\nMostrando restaurantes en el estado de', estado, ':')
    rest = restaurantes_en_estado(registros, estado)
    mostrar_numerado(rest)

def test_porc_rest_nombre(registros, nombre):
    porcentaje = porc_rest_nombre (registros, nombre)
    print('\nMostrando porcentaje de restaurantes ', nombre)
    print('{:.2f}%'.format(porc_rest_nombre(registros, nombre)))   
    
def test_rest_mayor_porc(registros):
    print('\nMostrando el restaurante con mayor presencia en el dataset:')
    print(rest_mayor_porc(registros))

def test_contar_restaurantes(registros):
    print('\nMostrando el restaurante con mayor presencia en el dataset:')
    dicc = contar_restaurantes(registros)
    for nombre, cont in dicc.items():
        print(nombre,"-->", cont) 
    
def test_porc_por_rest(registros):
    print('\nMostrando el porcentaje de cada restaurante:')
    dicc=porc_por_rest(registros)
    for nombre, porc in dicc.items():
        print(nombre,"-->", '{:.2f}%'.format(porc)) 

def test_distancia (coordenada1, coordenada2):
    dist = distancia(coordenada1, coordenada2)
    print("La distancia de ", coordenada1, " a ", coordenada2, " es ", dist)
            
def test_rest_cercanos(registros,coordenadas,radio=0.5):
    print('\nMostrando resturantes cercanos a {}'.format(coordenadas))
    cercanos = rest_cercanos(registros, coordenadas, radio)
    #print(cercanos[0:5])
    mostrar_numerado(cercanos)


################################################################
#  Programa principal
################################################################
if __name__ == '__main__':
    REGISTROS= lee_fichero('../data/fast_food.csv')
    test_lee_fichero(REGISTROS)
    test_nombres_restaurantes(REGISTROS)
    test_restaurantes_en_estado(REGISTROS, 'IL')   
    test_porc_rest_nombre(REGISTROS, 'Burger King')
    test_contar_restaurantes(REGISTROS)
    test_rest_mayor_porc(REGISTROS)
    test_porc_por_rest(REGISTROS)
    test_distancia((34,-81), (REGISTROS[0][5], REGISTROS[0][6]))
    test_rest_cercanos(REGISTROS,(34,-81))
    
    histograma_porcentajes(REGISTROS)
