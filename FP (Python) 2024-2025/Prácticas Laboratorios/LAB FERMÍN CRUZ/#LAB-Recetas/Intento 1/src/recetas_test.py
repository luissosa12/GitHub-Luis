from recetas import *
#-------------------------------------------------------------------------------------------------------------------------
#TEST DE LA FUNCIÓN 2:
def test_lee_recetas(recetas: list[Receta]) -> None:
    recetas = lee_recetas('data/recetas.csv')
    print()
    print('TEST DE LA FUNCIÓN 2: Probando la función: lee_recetas:...')
    print(f'Se han leído: {len(recetas)} recetas')
    print(f'Aquí se imprimen las 2 primeras recetas: {recetas[:2]}')
    print()
#------------------------------------------------------------------------------------------------------------------------.
#TEST DE LA FUNCIÓN 3:
def test_ingredientes_en_unidad(recetas: list[Receta], unidad: Optional[str]) -> None:
    sol = ingredientes_en_unidad(recetas, unidad)
    print('TEST DE LA FUNCIÓN 3: Probando la función: ingredientes_en_unidad:...')
    print(f'Hay: {sol} ingredientes que se miden en: {unidad}')
    print()
#-------------------------------------------------------------------------------------------------------------------------
#TEST DE LA FUNCIÓN 4:
def test_recetas_con_ingredientes(recetas: list[Receta], nombre_ingredientes: set[str]) -> None:
    sol = recetas_con_ingredientes(recetas, nombre_ingredientes)
    print('TEST DE LA FUNCIÓN 4: Probando la función: recetas_con_ingredientes:...')
    print(f'Con los ingredientes: {nombre_ingredientes}, tenemos las siguientes recetas: {sol}')
    print()
#-------------------------------------------------------------------------------------------------------------------------
#TEST DE LA FUNCIÓN 5:

#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    recetas = lee_recetas('data/recetas.csv')
    test_lee_recetas(recetas)

    test_ingredientes_en_unidad(recetas, None)
    test_ingredientes_en_unidad(recetas, 'gr')
    test_ingredientes_en_unidad(recetas, 'cl')

    test_recetas_con_ingredientes(recetas, {'harina', 'azúcar'})
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------