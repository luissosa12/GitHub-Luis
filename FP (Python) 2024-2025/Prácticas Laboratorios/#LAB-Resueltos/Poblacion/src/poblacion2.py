# -*- coding: utf-8 -*-
'''
Created on 7 ago. 2019

@author: Juanmi
'''
import csv
from matplotlib import pyplot as plt

########################################################################################
def lee_poblaciones(fichero):
    with open(fichero, 'r', encoding="utf-8") as f:
        lector = csv.reader(f)
        registro = [(pais, codpa, int(anyo), int(hab)) for pais,codpa,anyo,hab in lector]
        return registro
    
def calcula_paises(poblaciones):
    pais=[]
    conj_paises = set()
    for pais,_,_,_ in poblaciones:
        conj_paises.add(pais)
    pais = list(conj_paises)
    return sorted(pais)

def filtra_por_pais(poblaciones, pais):
    pais_filtrado = []
    paisIf = pais
    for pais,codpa,anyo,hab in poblaciones:
        if pais == paisIf or codpa == paisIf:
            pais_filtrado.append((anyo,hab))
    return pais_filtrado

def filtra_por_paises_y_anyo(poblaciones, anyo, paises):
    paises_filtrados = []
    anyoIf = anyo
    for pais,_,anyo,hab in poblaciones:
        if pais in paises and anyo == anyoIf:
            paises_filtrados.append((pais,hab))
    return paises_filtrados

def muestra_evolucion_poblacion(poblaciones, pais):
    pais_filtrado = filtra_por_pais(poblaciones, pais)
    poblacion = [poblacion for _,poblacion in pais_filtrado]
    anyo = [anyo for anyo,_ in pais_filtrado]
    titulo = "Evolución de la población en " + pais
    plt.title(titulo)
    plt.plot(anyo,poblacion)
    plt.show()

def muestra_comparativa_paises_anyo(poblaciones, anyo, paises):
    ''' Genera una gráfica de barras en la que se muestra la comparativa de
    la población de varios países en un año concreto

    Toma como entrada una lista de tuplas (nombre_pais, cod_pais, anyo, num_habitantes) y 
    produce como salida un gráfico de barras con el número de habitantes de los paises 
    dados como parámetro en el año anyo.
    Cada barra corresponde a un pais.
    
    Estas son las instrucciones 'matplotlib' para trazar el diagrama de barras
    a partir de una cadena con el título del gráfico, 
    una lista de nombres paises y otra lista (con el mismo orden) de
    número de habitantes de esos países:
       
        plt.title(titulo)
        indice = range(len(l_paises))
        plt.bar(indice, l_habitantes)
        plt.xticks(indice, l_paises, fontsize=8)
        plt.show()
    '''
    paises_filtrados = filtra_por_paises_y_anyo(poblaciones, anyo, paises)
    pais = [pais for pais,_ in paises_filtrados]
    poblacion = [poblacion for _,poblacion in paises_filtrados]
    titulo = "Comparacion de la poblacion de los dife. paises en " + str(anyo)
    plt.title(titulo)
    indice = range(len(pais))
    plt.bar(indice, poblacion)
    plt.xticks(indice, pais, fontsize=8)
    plt.show()
    