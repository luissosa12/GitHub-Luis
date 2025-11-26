from compras import *
#-------------------------------------------------------------------------------------------------------------------------
#TEST DE LA FUNCIÓN 1:
def test_lee_compras(compras: list[Compra]) -> None:
    compras = lee_compras('data\compras.csv')
    print()
    print('TEST DE LA FUNCIÓN 1: Probando la función: lee_compras:...')
    print(f'Se han leído: {len(compras)} compras')
    print(f'Aquí se imprimen las 2 primeras compras: {compras[:2]}')
    print()
    print(f'Aquí se imprimen las 2 últimas compras: {compras[-2:]}')
    print()
#-------------------------------------------------------------------------------------------------------------------------
#TEST DE LA FUNCIÓN 2:
def test_compra_maxima_minima_provincia(compras: list[Compra], provincia: Optional[str]=None) -> None:
    sol = compra_maxima_minima_provincia(compras, provincia)
    print()
    print('TEST DE LA FUNCIÓN 2: Probando la función: compra_maxima_minima_provincia:...')
    print(f'En la provincia de: {provincia}, la compra máxima fue de: {sol[0]}€ y la compra mínima fue de: {sol[1]}€')
    print()
#-------------------------------------------------------------------------------------------------------------------------
#TEST DE LA FUNCIÓN 3:
def test_hora_menos_afluencia(compras: list[Compra]) -> None:
    sol = hora_menos_afluencia(compras)
    print('TEST DE LA FUNCIÓN 3: Probando la función: hora_menos_afluencia:...')
    print(f'La hora de menso afluencia fueron las: {sol[0]}h con un total de: {sol[1]} personas')
    print()
#-------------------------------------------------------------------------------------------------------------------------
#TEST DE LA FUNCIÓN 4:
def test_supermercados_mas_facturacion(compras: list[Compra], n: int = 3) -> None:
    sol = supermercados_mas_facturacion(compras, n)
    print('TEST DE LA FUNCIÓN 4: Probando la función: supermercados_mas_facturacion:...')
    print(f'Los {n} supermercados con mayor facturación son: {sol}')
    print()
#-------------------------------------------------------------------------------------------------------------------------
#TEST DE LA FUNCIÓN 5:
def test_clientes_itinerantes(compras: list[Compra], n: int) -> None:
    sol = clientes_itinerantes(compras, n)
    print('TEST DE LA FUNCIÓN 5: Probando la función: clientes_itinerantes:...')
    print(f'Los clientes que han comprado en más de: {n} provincias son: {sol}')
    print()
#-------------------------------------------------------------------------------------------------------------------------
#TEST DE LA FUNCIÓN 6:

#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    compras = lee_compras('data\compras.csv')
    test_lee_compras(compras)

    test_compra_maxima_minima_provincia(compras, "Huelva")
    test_compra_maxima_minima_provincia(compras)

    test_hora_menos_afluencia(compras)

    test_supermercados_mas_facturacion(compras, 2)
    test_supermercados_mas_facturacion(compras)

    test_clientes_itinerantes(compras, 7)
    test_clientes_itinerantes(compras, 6)
#-------------------------------------------------------------------------------------------------------------------------