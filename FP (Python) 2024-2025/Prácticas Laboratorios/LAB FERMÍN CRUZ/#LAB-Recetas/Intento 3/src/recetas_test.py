from recetas import *
#-------------------------------------------------------------------------------------------------------------------------
#TEST DE LA FUNCIÓN 2:
def test_lee_recetas(recetas: list[Receta]) -> None:
    print()
    print('TEST DE LA FUNCIÓN 2: Probando la función: lee_recetas:...')
    print(f'Se han leído: {len(recetas)} recetas')
    print(f'Aquí se imprimen las 2 primeras recetas: {recetas[:2]}')
    print()
#-------------------------------------------------------------------------------------------------------------------------
#TEST DE LA FUNCIÓN 3:
def test_ingredientes_en_unidad(recetas: list[Receta], unidad_medida: Optional[str]) -> None:
    sol = ingredientes_en_unidad(recetas, unidad_medida)
    print('TEST DE LA FUNCIÓN 3: Probando la función: ingredientes_en_unidad:...')
    print(f'Se han encontrado: {sol} ingredientes con la unidad de medida: {unidad_medida}')
    print()
#-------------------------------------------------------------------------------------------------------------------------
#TEST DE LA FUNCIÓN 4:
def test_recetas_con_ingredientes(recetas: list[Receta], ingredientes_tenemos: set[str]) -> None:
    sol = recetas_con_ingredientes(recetas, ingredientes_tenemos)
    print(f'Con los ingredientes: {ingredientes_tenemos}, se puede hacer: {sol}')
    print()
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    recetas = lee_recetas('data/recetas.csv')
    
    #LLAMADA AL TEST DE LA FUNCIÓN 2:
    test_lee_recetas(recetas)

    #LLAMADA AL TEST DE LA FUNCIÓN 3:
    test_ingredientes_en_unidad(recetas, None)
    test_ingredientes_en_unidad(recetas, 'gr')
    test_ingredientes_en_unidad(recetas, 'cl')

    #LLAMADA AL TEST DE LA FUNCIÓN 4:
    test_recetas_con_ingredientes(recetas, {'harina', 'azúcar'})
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
