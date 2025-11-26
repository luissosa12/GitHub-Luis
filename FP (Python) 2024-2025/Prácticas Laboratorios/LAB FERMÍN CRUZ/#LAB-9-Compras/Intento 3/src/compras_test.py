from compras import *
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#TEST DE LA FUNCIÓN 1:
def test_lee_compras(compras: list[Compra]) -> None:
    compras = lee_compras('data\compras.csv')
    print()
    print('TEST DE LA FUNCIÓN DEL EJERCICIO 1: PROBANDO LA FUNCIÓN: "lee_compras:..."')
    print(f'Se han leído {len(compras)} compras')
    print(f'Aquí se imprimen las 2 primeras compras: {compras[:2]}')
    print()
#-------------------------------------------------------------------------------------------------------------------------
#TEST DE LA FUNCIÓN 2:
def test_compra_maxima_minima_provincia(compras: list[Compra], provincia: Optional[str]=None) -> None:
    sol = compra_maxima_minima_provincia(compras, provincia)
    print('TEST DE LA FUNCIÓN DEL EJERCICIO 2: PROBANDO LA FUNCIÓN: "compra_maxima_minima_provincia":...')
    print(f'Para la provincia de "{provincia}", la compra máxima es de: {sol[0]}€ y la mínima es de: {sol[1]}€')
    print()
#-------------------------------------------------------------------------------------------------------------------------
#TEST DE LA FUNCIÓN 3:
def test_hora_menos_afluencia(compras: list[Compra]) -> None:
    sol = hora_menos_afluencia(compras)
    print('TEST DE LA FUNCIÓN DEL EJERCICIO 3: PROBANDO LA FUNCIÓN: "hora_menos_afluencia:..."')
    print(f'La hora de menos afluencia son las: {sol[0]}h con un total de: {sol[1]} personas')
    print()
#-------------------------------------------------------------------------------------------------------------------------
#TEST DE LA FUNCIÓN 4:
def test_supermercados_mas_facturacion(compras: list[Compra], n: int = 3) -> None:
    sol = supermercados_mas_facturacion(compras, n)
    print('TEST DE LA FUNCIÓN DEL EJERCICIO 4: PROBANDO LA FUNCIÓN: "supermercados_mas_facturacion:..."')
    print(f'Los {n} supermercados con mayor facturación son: {sol}')
    print()
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
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------