# -*- coding: utf-8 -*-

''' 
Poblacion mundial

@author: Toñi Reina
REVISOR: José Antonio Troyano, Daniel Mateos, Mariano González
ÚLTIMA MODIFICACIÓN: 17/10/2018


En este proyecto trabajaremos con datos de población mundial, representados 
mediante listas. Implementaremos una serie de funciones que nos permitirán mostrar
gráficas de evolución de la población, así como, comparar la población en distintos
países.

CONJUNTOS DE DATOS:
-------------------
El proyecto incluye un conjuntos de datos de prueba:
  - population.csv: con los datos de población de diversos países o agrupaciones de países 
    en distintos años.
 
FUNCIONES QUE FORMAN PARTE DEL EJERCICIO:
-----------------------------------------
- lee_poblaciones(fichero):
    lee el fichero de entrada y devuelve una lista de tuplas 
    (nombre_pais, cod_pais, anyo, num_habitantes)
- calcula_paises(poblaciones):
    toma una lista de tuplas (nombre_pais, cod_pais, anyo, num_habitantes) 
    y devuelve una lista ordenada con los nombres
    de los paises o conjuntos de paises para los que hay datos
- filtra_por_pais(poblaciones, pais):
    toma una lista de tuplas (nombre_pais, cod_pais, anyo, num_habitantes) y 
    devuelve una lista de tuplas (anyo, num_habitantes)
    con los datos del pais que se pasa como parámetro. 
    El pais se puede dar con su nombre completo o con su código
- filtra_por_paises_y_anyo(poblaciones, anyo, paises):
    toma una lista de tuplas (nombre_pais, cod_pais, anyo, num_habitantes) y 
    devuelve una lista de tuplas (nombre_pais, num_habitantes)
    con los datos del año pasado como parámetro para los paises 
    incluidos en el parámetro paises. 
- muestra_evolucion_poblacion(poblaciones, pais):
    toma una lista de tuplas (nombre_pais, cod_pais, anyo, num_habitantes) 
    y genera un gráfico con la evolución de la población
    del pais dado como parámetro. El pais se puede dar con su nombre completo o con
    su código
- muestra_comparativa_paises_anyo(poblaciones, anyo, paises):
    toma una lista de tuplas (nombre_pais, cod_pais, anyo, num_habitantes), un año y 
    un grupo de paises y genera un gráfico 
    de barras con la población de esos países en el año dado como parámetro

'''
import csv
from matplotlib import pyplot as plt

########################################################################################
def lee_poblaciones(fichero):
    ''' Lee el fichero de entrada y devuelve una lista de tuplas poblaciones

    Cada línea del fichero se corresponde con los datos de un pais o agrupación de países, 
    y se representa con una tupla con los siguientes valores:
        - Nombre pais
        - Código pais
        - Año 
        - Num. habitantes del pais en ese año
    Hay que transformar la entrada (cadenas de caracteres) en valores numéricos
    en aquellos datos que sean de tipo numérico.
    '''
    registro = []
    f = open(fichero, 'r')
    fichero = csv.reader(f)
    for p, c, a, pob in fichero:
        tupla = (p, c, int(a), int(pob))
        registro.append(tupla)
    return registro
############################################################################################

############################################################################################
def calcula_paises(poblaciones):
    ''' Calcula el conjunto de paises presentes en una lista de paises

    Toma como entrada una lista de tuplas (pais, cod_pais, anyo, num_habitantes) y 
    produce como  salida una lista ordenada con los nombres de los paises 
    para los que haya al menos un dato de poblacion. 
    La lista de salida no contendrá elementos repetidos.
    '''
    paises = []
    conj_paises = set()
    for p, _, _, _ in poblaciones:
        conj_paises.add(p)
    paises = list(conj_paises)
    return sorted(paises)

##############################################################################################
############################################################################################## 
def filtra_por_pais(poblaciones, pais):
    ''' Selecciona las tuplas correspondientes a un determinado pais

    Toma como entrada una lista de tuplas (nombre_pais, cod_pais, anyo, num_habitantes) y
    produce como salida otra lista de tuplas (anyo, num_habitantes) con los datos de 
    poblacion del pais que se pasa como parámetro. El pais se puede indicar 
    bien dando su nombre completo, bien dando su código.
    '''
    pais_filtrado = []
    for p, c, a, pob in poblaciones:
        if p == pais or c == pais:
            pais_filtrado.append((a, pob))
    return pais_filtrado
##############################################################################################

############################################################################################## 
def filtra_por_paises_y_anyo(poblaciones, anyo, paises):
    ''' Selecciona las tuplas correspondientes a un conjunto de paises de un año concreto

    Toma como entrada una lista de tuplas (nombre_pais, cod_pais, anyo, num_habitantes) y 
    produce como salida otra lista de tuplas (nombre_pais, num_habitantes) 
    en la que solo se incluyen aquellos datos
    correspondientes al año dado como parámetro y de los paises 
    incluidos en la colección paises
    '''
    paises_anyo = []
    for p, _, a, pob in poblaciones:
        if p in paises and a == anyo:
            paises_anyo.append((p,pob))
    return paises_anyo
    #return [(p,pob) for p,_,a,pob in poblaciones if p in paises and a == anyo]
    
##############################################################################################

###############################################################################################
def muestra_evolucion_poblacion(poblaciones, pais):
    ''' Genera una curva con la evolución de la población de un país. El pais puede
    darse como su nombre completo o por su código. 

    Toma como entrada una lista de tuplas (nombre_pais, cod_pais, anyo, num_habitantes) y 
    produce como salida un gráfico con la evolución de la población del país dado como
    parámetro a lo largo del tiempo. 
    
    Estas son las instrucciones 'matplotlib' para trazar el gráfico
    a partir una cadena con el título que se va a mostrar en el gráfico,
    una lista de años y otra lista con los número de habitantes (con el mismo orden):
        
        plt.title(titulo)
        plt.plot(l_anyos,l_habitantes)
        plt.show()
    '''
    poblacion_pais = filtra_por_pais(poblaciones,pais)
    poblaciones = [poblacion for _,poblacion in poblacion_pais]
    anyos = [anyo for anyo,_ in poblacion_pais]
    lab='Evolución de la población de ' + pais
    plt.title(lab)
    plt.plot(anyos,poblaciones)
    plt.legend()
    plt.show()
    pass
   
###############################################################################################

###############################################################################################
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
    
    pass
###############################################################################################
