# -*- coding: utf-8 -*-

from normalidad import *

################################################################
#  Funciones de test
################################################################
def test_muestra_histograma():
    muestra_histograma(FRECUENCIAS)
    muestra_histograma(PESOS)
    muestra_histograma(SINTETICA)
    

def test_calcula_momento_central():
    # El momento central de grado 1 es 0 (o muy cercano)
    print(calcula_momento_central(FRECUENCIAS, grado=1))
    # El momento central de grado 2 coincide con la varianza
    print(calcula_momento_central(FRECUENCIAS))
    

def test_calcula_asimetria():
    # La distribución de FRECUENCIAS no es simétrica
    print(calcula_asimetria(FRECUENCIAS))
    # La distribución de PESOS es simétrica
    print(calcula_asimetria(PESOS))
    # La distribución SINTETICA es muy simétrica
    print(calcula_asimetria(SINTETICA))


def test_calcula_curtosis():
    # La distribución de FRECUENCIAS es más 'picuda'
    print(calcula_curtosis(FRECUENCIAS))
    # La distribución de PESOS es más 'acampanada'
    print(calcula_curtosis(PESOS))
    # La distribución SINTETICA es muy 'acampanada'
    print(calcula_curtosis(SINTETICA))
    
    
def test_calcula_jarque_bera():
    # La distribución de FRECUENCIAS 'no es normal'
    print(calcula_jarque_bera(FRECUENCIAS))
    # La distribución de PESOS 'es más normal'
    print(calcula_jarque_bera(PESOS))
    # La distribución SINTETICA 'es muy normal'
    print(calcula_jarque_bera(SINTETICA))


def test_calcula_pvalue():
    # No podemos afirmar que FRECUENCIAS es normal
    jb_frec = calcula_jarque_bera(FRECUENCIAS)
    print(calcula_pvalue(jb_frec, valores_chi2_2, pvalues_chi2_2))
    # No podemos afirmar que PESOS es normal
    jb_peso = calcula_jarque_bera(PESOS)
    print(calcula_pvalue(jb_peso, valores_chi2_2, pvalues_chi2_2))
    # Podemos afirmar que SINTETICA es normal con un nivel de significación de 0.95
    jb_sint = calcula_jarque_bera(SINTETICA)
    print(calcula_pvalue(jb_sint, valores_chi2_2, pvalues_chi2_2))
    # Cálculo del estadístico Jarque-Bera y el pvalue con la implementación de Scipy
    print(jarque_bera(FRECUENCIAS))
    print(jarque_bera(PESOS))
    print(jarque_bera(SINTETICA))
    

################################################################
#  Programa principal
################################################################
FRECUENCIAS = lee_serie('./csv/frecuencias.csv')
print(FRECUENCIAS[:10])
PESOS = lee_serie('./csv/pesos.csv', float)
print(PESOS[:10])
SINTETICA = lee_serie('./csv/1000-puntos-normal-0-1.csv', float)
print(SINTETICA[:10])
    
#test_muestra_histograma()
#test_calcula_momento_central()
#test_calcula_asimetria()
#test_calcula_curtosis()
#test_calcula_jarque_bera()
#test_calcula_pvalue()    