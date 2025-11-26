# -*- coding: utf-8 -*-
''' Examen de diciembre 18-19 Fundamentos de Programación (Python)

AUTOR: Mariano González
REVISORES: Carlos García, Fermín Cruz, Toñi Reina
ÚLTIMA MODIFICACIóN: 10/9/2019

################################################################
#  Datos del alumno
#
#  Nombre y apellidos: 
#  DNI: 
#  Grupo: 
################################################################

En este ejercicio trabajaremos sobre un dataset con información
sobre contratos de trabajo. 

Los datos se encuentran almacenados en un fichero en formato CSV.
Estas son las primeras líneas del fichero de entrada (fíjese en que
la primera línea es una cabecera con los nombres de las columnas):

    Numero SS,fecha,codigo,dias,horas,sueldo
    41347712,01/03/2014,77232,239,6,20.8
    75402883,28/07/2014,77232,363,4,24.5
    62583432,15/07/2014,12271,214,4,29.1
    62583432,16/04/2015,50323,324,5,15.7
    ...
            
Donde:
    número SS: número de la Seguridad Social del trabajador.
    Fecha: fecha del contrato.
    Código: código identificativo del campo de actividad del contrato.
    Día: número de días del contrato.
    Hora: número de horas de trabajo al día.
    Sueldo: sueldo bruto por hora.

En el fichero pueden existir distintos contratos para el mismo trabajador.
    
Implemente las funciones con los comentarios EJERCICIO Nº,
eliminando previamente la instrucción pass.
'''

import csv
from datetime import datetime
from matplotlib import pylab as plt
from collections import namedtuple
from collections import defaultdict
from collections import Counter
from csv import DictReader


Contrato = namedtuple("Contrato", "numSS, fecha, codigo, dias, hora, sueldo")

# EJERCICIO 1:
def lee_contratos(fichero):
    ''' Lee el fichero de entrada y devuelve una lista de tuplas.
    
        Cada línea del fichero de entrada contiene seis datos:
            número SS: número de la Seguridad Social del trabajador.
            Fecha: fecha del contrato.
            Código: código identificativo del campo de actividad del contrato.
            Día: número de días del contrato.
            Hora: número de horas de trabajo al día.
            Sueldo: sueldo bruto por hora.
            
        Hay que transformar ciertos elementos de la entrada en valores numóricos
        o de tipo fecha para que puedan ser procesados posteriormente.
        
        Para convertir una cadena de texto del estilo de '30/10/2007'
        en una fecha, utilice esta función: 
        fecha = datetime.strptime(fecha_en_cadena, '%d/%m/%Y').date()
        
    '''
    with open(fichero, 'r', encoding="utf-8") as f:
        lector = csv.reader(f)
        next(lector)
        contratos=[]
        for numSS, fecha, codigo, dias, hora, sueldo in lector:
            fecha = datetime.strptime(fecha, '%d/%m/%Y').date()
            dias = int(dias)
            hora = int(hora)
            sueldo = float(sueldo)
            c = Contrato(numSS,fecha,codigo,dias,hora,sueldo)
            contratos.append(c)
    return contratos

# EJERCICIO 2
def trabajadores_contratados_actividad(contratos, codigo):
    ''' Recibe una lista de tuplas con la información sobre los contratos y
    el código de una actividad y devuelve un conjunto con los números de la
    Seguridad Social de los trabajadores con contrato en dicha actividad.
    '''
    res ={contrato.numSS for contrato in contratos if contrato.codigo == codigo}
    return res

# EJERCICIO 3
def dias_contrato_trabajador(contratos, numeroSS):
    ''' Recibe una lista de tuplas con la información sobre los contratos y
    el número de la Seguridad Social de un trabajador y devuelve el total de
    días de trabajo acumulados por los contratos del trabajador.
    '''
    res = sum(contrato.dias for contrato in contratos if contrato.numSS == numeroSS)
    return res
                
# EJERCICIO 4
def trabajador_mas_dias(contratos):
    ''' Recibe una lista de tuplas con la información sobre los contratos,
    y busca el trabajador que acumula más días de contrato. Devuelve una tupla formada por
    el número de días totales y el número de la Seguridad Social del trabajador.
    En caso de empate a número de días, devuelve uno cualquiera de ellos.
    '''
    dias_por_numSS = acumuladorDiasPorNumSS(contratos)
    mayor = max(dias_por_numSS, key=dias_por_numSS.get)
    return (dias_por_numSS[mayor], mayor)
    pass

def acumuladorDiasPorNumSS(contratos):
    res = dict()
    for contrato in contratos:
        clave = contrato.numSS
        if clave in res:
            res[clave] = res[clave] + contrato.dias
        else:
            res[clave] = contrato.dias
    return res
    
    
# EJERCICIO 5
def indexa_contratos_por_actividad(contratos):
    ''' Recibe una lista de tuplas con la información sobre los contratos,
    y devuelve un diccionario en el que las claves son los códigos de actividad
    y los valores asociados son listas con las tuplas correspondientes a
    la información sobre los 3 contratos con mayor duración en días de cada actividad. 
    
    Las listas asociadas a los códigos de actividad deben estar ordenadas
    de mayor a menor duración en días.    
    '''    
    ind_act = indexa_por_actividad2(contratos)
    res = indexa_maximos(ind_act)
    return res

def indexa_por_actividad(contratos):
    '''funcion auxiliar. versión 1 (con dict)'''
    ''' ENTRADA: Una lista de Contrato
        SALIDA: Un diccionario str:list(Contrato) en el que las claves son el código
        de las actividades y los valores son una la lista con los contratos que tienen
        ese código de actividad
    '''
    res = dict()
    for contrato in contratos:
        clave = contrato.codigo
        if clave in res:
            res[clave].append(contrato)
        else:
            res[clave] = list(contrato)
    return res

def indexa_por_actividad2(contratos):
    '''funcion auxiliar. versión 2 (con defaultdict)'''
    ''' ENTRADA: Una lista de Contrato
        SALIDA: Un defaultdict str:list(Contrato) en el que las claves son el código
        de las actividades y los valores son una la lista con los contratos que tienen
        ese código de actividad
    '''
    res = defaultdict(list)
    for contrato in contratos:
        clave = contrato.codigo
        res[clave].append(contrato)
    return res     

def indexa_maximos(dic_cont_por_act):
    '''
        ENTRADA: diccionario str:list(Contrato) en el que las claves son el código actividad,
        y los  valores, listas de Contrato con los contratos de esa actividad
        SALIDA: diccionario str:list(Contrato) en el que las claves son el código actividad,
        y los  valores, listas de Contrato con los tres contratos de esa actividad en los
        que se ha trabajado más días
    '''
    res = dict()
    for actividad, contratos in dic_cont_por_act.items():
        contratos_ordenados = sorted(contratos, key = lambda contrato:contrato.dias, reverse=True) 
        res[actividad] =contratos_ordenados[:3]
    return res


# EJERCICIO 6
def muestra_evolucion_contratos(contratos, codigo):
    ''' Recibe una lista de tuplas con la información sobre los contratos y
    el código de una actividad. Muestra una gráfica con la evolución a lo largo
    de los años del número de contratos de la actividad en cuestión.
    
    Para mostrar la gráfica use el siguiente código:
    
        plt.bar(range(len(numero_contratos)), numero_contratos, tick_label=anyos)
        plt.show()
    
    Debe calcular previamente las siguientes listas:
    
    - anyos: lista ordenada con los años DEL PERIODO COMPLETO para el que hay datos
    en la lista de contratos, ordenados crecientemente. Cada año debe aparecer una sola vez.
    Para obtener el año de una fecha f, utilize la expresión f.year
    - numero_contratos: lista con el número de contratos de la actividad dada
    en cada uno de los años de la lista anterior.
    '''
    pass

