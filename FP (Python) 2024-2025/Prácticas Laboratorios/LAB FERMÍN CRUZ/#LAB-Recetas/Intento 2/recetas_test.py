from recetas import *
#-------------------------------------------------------------------------------------------------------------------------
#TEST DE LA FUNCIÓN 2:
def test_lee_recetas(recetas: str) -> None:
    recetas = lee_recetas('data/recetas.csv')
    print()
    print('TEST DE LA FUNCIÓN 2: Probando la función: lee_recetas:...')
    print(f'Se han leído: {len(recetas)} recetas')
    print(f'Aquí se imprimen las 2 primeras recetas: {recetas[:2]}')
    print(f'Aquí se imprimen las 2 últimas recetas: {recetas[-2:]}')
    print()
#-------------------------------------------------------------------------------------------------------------------------
#TEST DE LA FUNCIÓN 3:
def test_ingredientes_en_unidad(recetas: list[Receta], unidad_medida: Optional[str]) -> None:
    sol = ingredientes_en_unidad(recetas, unidad_medida)
    print('TEST DE LA FUNCIÓN 3: Probando la función: ingredientes_en_unidad:...')
    print(f'Hay: {sol} ingredientes que se miden en: {unidad_medida}')
    print()
#-------------------------------------------------------------------------------------------------------------------------
#TEST DE LA FUNCIÓN 4:
def test_recetas_con_ingredientes(recetas: list[Receta], ingredientes_tenemos: set[str]) -> None:
    sol = recetas_con_ingredientes(recetas, ingredientes_tenemos)
    print('TEST DE LA FUNCIÓN 4: Probando la función: recetas_con_ingredientes:...')
    print(f'Con los ingredientes que tenemos: {ingredientes_tenemos}, podemos hacer: {sol}')
    print()
#-------------------------------------------------------------------------------------------------------------------------
#TEST DE LA FUNCIÓN 5:

#-------------------------------------------------------------------------------------------------------------------------
#TEST DE LA FUNCIÓN 6:

#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    #LLAMADA AL TEST DE LA FUNCIÓN 2:
    recetas = lee_recetas('data/recetas.csv')
    test_lee_recetas(recetas)

    #LLAMADA AL TEST DE LA FUNCIÓN 3:
    test_ingredientes_en_unidad(recetas, None)
    test_ingredientes_en_unidad(recetas, 'gr')
    test_ingredientes_en_unidad(recetas, 'cl')

    #LLAMADA AL TEST DE LA FUNCIÓN 4:
    test_recetas_con_ingredientes(recetas, {'harina', 'azúcar'})

    #LLAMADA AL TEST DE LA FUNCIÓN 5:


    #LLAMADA AL TEST DE LA FUNCIÓN 6:

#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------