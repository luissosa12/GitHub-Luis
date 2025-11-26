from entrenos import *

def test_lee_entrenos():
    print('Probando lee_entrenos')
    datos = lee_entrenos("data/entrenos.csv")
    print('Se han leído', len(datos), 'registros')
    print('Mostrando los tres primeros registros')
    print(datos[0])
    print(datos[1])
    print(datos[2])
    print()

