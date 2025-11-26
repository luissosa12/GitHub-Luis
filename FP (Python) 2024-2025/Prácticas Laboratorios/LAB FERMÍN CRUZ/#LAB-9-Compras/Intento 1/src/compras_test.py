from compras import *
#-------------------------------------------------------------------------------------------------------------------------
#TEST DE LA FUNCIÓN 1:
def test_lee_compras(compras):
    print('TEST DE LA FUNCIÓN 1:')
    print('Probando la función: lee_compras:...')
    print(f'Se han leído: {len(compras)} compras')
    print(f'Aquí se imprimen las 3 primeras compras: {compras[:3]}')
    print()
#-------------------------------------------------------------------------------------------------------------------------
#TEST DE LA FUNCIÓN 2:

#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    compras = lee_compras('data\compras.csv')
    test_lee_compras(compras)