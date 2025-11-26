from compras import *
#-------------------------------------------------------------------------------------------------------------------------
#TEST 1:
def test_lee_compras(compras: list[Compra]) -> None:
    print()
    print('TEST 1 DE LA FUNCIÓN: lee_compras:...')
    compras = lee_compras('data\compras.csv')
    print(f'Se han leído {len(compras)} compras')
    print(f'Aquí se muestran las 2 primeras compras: {compras[:2]}')
    print()
    print(f'Aquí se muestran las 2 últimas compras: {compras[-2:]}')
    print()
#-------------------------------------------------------------------------------------------------------------------------
#TEST 2:
def test_compra_maxima_minima_provincia(compras: list[Compra], provincia: Optional[str]=None ) -> None:
    print('TEST 2 DE LA FUNCIÓN: compra_maxima_minima_provincia:...')
    sol = compra_maxima_minima_provincia(compras, provincia)
    print(f'En la provincia de: {provincia} la compra máxima fue de: {sol[0]}€ y la compra mínima fue de: {sol[1]}€')
    print()
#-------------------------------------------------------------------------------------------------------------------------
#TEST 3:
def test_hora_menos_afluencia(compras: list[Compra]) -> None:
    print('TEST 3 DE LA FUNCIÓN: hora_menos_afluencia:...')
    sol = hora_menos_afluencia(compras)
    print(f'La hora de menos afluencia son las: {sol[0]}h con un total de: {sol[1]} personas')
    print()
#-------------------------------------------------------------------------------------------------------------------------
#TEST 4:
def test_supermercados_mas_facturacion(compras: list[Compra], n: int = 3) -> None:
    print('TEST 4 DE LA FUNCIÓN: supermercados_mas_facturacion:...')
    sol = supermercados_mas_facturacion(compras, n)
    print(f'Los {n} supermercados con más facturación son: {sol}')
    print()
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    compras = lee_compras('data\compras.csv')
    test_lee_compras(compras)

    test_compra_maxima_minima_provincia(compras, 'Huelva')
    test_compra_maxima_minima_provincia(compras, None)

    test_hora_menos_afluencia(compras)

    test_supermercados_mas_facturacion(compras, 2)
    test_supermercados_mas_facturacion(compras)