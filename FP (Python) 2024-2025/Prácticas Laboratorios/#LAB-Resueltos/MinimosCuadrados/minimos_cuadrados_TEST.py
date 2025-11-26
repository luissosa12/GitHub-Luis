# -*- coding: utf-8 -*-

from minimos_cuadrados import *

################################################################
#  Funciones de test
################################################################
def test_pesos_alturas_por_edades(registros):
    puntos = pesos_alturas_por_edades(registros, 11, 13.9)
    print(len(puntos), puntos)
    puntos = pesos_alturas_por_edades(registros, 14, 21)
    print(len(puntos), puntos)


def test_pesos_alturas_por_genero(registros):
    mujeres = pesos_alturas_por_genero(registros, 'f')
    print(len(mujeres), mujeres)
    hombres = pesos_alturas_por_genero(registros, 'm')
    print(len(hombres), hombres)


def test_calcula_recta_regresion(registros):
    puntos = pesos_alturas_por_edades(registros, 11, 21)
    a, b = calcula_recta_regresion(puntos)
    print("Recta: a={}    b={}".format(a, b))


def test_evalua_metrica_MAE(registros):
    menores = pesos_alturas_por_edades(registros, 9, 13.9)
    jovenes = pesos_alturas_por_edades(registros, 14, 21)
    a, b = calcula_recta_regresion(menores)
    print("Recta: a={}    b={}".format(a, b))
    print("Error menores: {}".format(evalua_metrica_MAE(menores, a, b)))
    print("Error jovenes: {}".format(evalua_metrica_MAE(jovenes, a, b)))


def test_muestra_recta_y_puntos(registros):
    hombres = pesos_alturas_por_genero(registros, 'm')
    a, b = calcula_recta_regresion(hombres)
    muestra_recta_y_puntos(a, b, hombres)


################################################################
#  Programa principal
################################################################
registros = lee_registros('./datos/registros.csv')
print("TODOS LOS REGISTROS: ", registros, '\n')

test_pesos_alturas_por_edades(registros)
test_pesos_alturas_por_genero(registros)
#test_calcula_recta_regresion(registros)
#test_evalua_metrica_MAE(registros)
#test_muestra_recta_y_puntos(registros)

