from extranjeria import *
#1
def test_leer_datos_extranjeria(datos):
    print('Probando la función: leer_datos_extranjeria...')
    print(f'Se han leído {len(datos)} registros')
    print(f'Aquí se muestran los primeros 3 datos: {datos[0]}, {datos[1]}, {datos[2]}')
    print('----------------------------------------------------------------------------------------------------------')

#2
def test_numero_nacionalidades_distintas(datos):
    nacionalidades = numero_nacionalidades_distintas(datos)
    print('Probando la función: numero_nacionalidades_distintas...')
    print(f'Se han encontrado {nacionalidades} nacionalidades distintas')
    print('----------------------------------------------------------------------------------------------------------')

#3
def test_secciones_distritos_con_extranjeros_nacionalidades(datos, paises):
    distrito_seccion = secciones_distritos_con_extranjeros_nacionalidades(datos, paises)
    print('Probando la función: secciones_distritos_con_extranjeros_nacionalidades...')
    print(f'Hay {len(distrito_seccion)} distritos con habitantes de {paises}')
    print(f'Aqui se muestran las 3 primeras secciones: {distrito_seccion[0]}, {distrito_seccion[1]}, {distrito_seccion[3]}')
    print('----------------------------------------------------------------------------------------------------------')

#4


#----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    datos = leer_datos_extranjeria("data/extranjeriaSevilla.csv")
    test_leer_datos_extranjeria(datos)
    test_numero_nacionalidades_distintas(datos)
    test_secciones_distritos_con_extranjeros_nacionalidades((datos), ('ALEMANIA', 'ITALIA'))