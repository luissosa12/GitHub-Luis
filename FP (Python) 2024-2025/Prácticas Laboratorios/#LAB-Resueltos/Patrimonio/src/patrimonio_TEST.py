# -*- coding: utf-8 -*-

from patrimonio import *

################################################################
#  Funciones de test
################################################################
def test_calcula_paises(registros):
    paises = calcula_paises(registros)
    print("Salida esperada:")
    print('Número de países con bienes Patrimonio de la Humanidad:', len(paises))
    print("Salida obtenida:")
    print("Número de países con bienes Patrimonio de la Humanidad: 163")
def test_bienes_por_tipo(registros):
    bienes_tipo = bienes_por_tipo(registros)
    print("\nSalida esperada:")
    print('Número de bienes por tipo:')
    print('    Natural - 190\n    Cultural - 813\n    Mixed - 33')
    print("Salida obtenida:")
    print('Número de bienes por tipo:')
    for tipo in bienes_tipo:
        print('   ' , tipo, '-', len(bienes_tipo[tipo]))
    
def test_dibuja_bienes_por_tipo(registros):
    print("\nSalida esperada:")
    print("Ver pdf en la carpeta 'doc'")
    dibuja_bienes_por_tipo(registros)

def test_pais_mas_bienes(registros):
    numero_bienes, pais = pais_mas_bienes(registros)
    print("\nSalida esperada:")
    print('El país con más bienes de tipo cultural es Italy con 44')
    print('El país con más bienes de tipo natural es [Australia o China] con 12')
    print("Salida obtenida:")
    print('El país con más bienes de tipo cultural es', pais, 'con', numero_bienes)
    numero_bienes, pais = pais_mas_bienes(registros, 'Natural')
    print('El país con más bienes de tipo natural es', pais, 'con', numero_bienes)
    
       
################################################################
#  Programa principal
################################################################

registros = lee_bienes('../data/whs.csv')
print ("Salida esperada:")
print ("Número total de bienes: 1036")
print ("[(1, 'Galápagos Islands', 1978, 'Natural', 'Ecuador'), (2, 'City of Quito', 1978, 'Cultural', 'Ecuador'), (3, 'Aachen Cathedral ', 1978, 'Cultural', 'Germany'), (4, 'L’Anse aux Meadows National Historic Site', 1978, 'Cultural', 'Canada'), (8, 'Ichkeul National Park', 1980, 'Natural', 'Tunisia')] ")
print ("Salida obtenida:")
print("Número total de bienes:", len(registros)) 
print(registros[:5], '\n')

'''
Elimine los comentarios de las llamadas a los test a medida que
vaya escribiendo las respectivas funciones
'''

#test_calcula_paises(registros)
test_bienes_por_tipo(registros)
#test_dibuja_bienes_por_tipo(registros)
#test_pais_mas_bienes(registros)
