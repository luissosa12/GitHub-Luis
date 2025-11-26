from compras import *

#1:
def test_leer_compras(datos):
    print('-------------------------------------------------------------------------------------------------------')
    print("Probando la función leer_compras:...")
    print(f"Se han leído {len(datos)} datos")
    print(f"Aquí se imprimen los 3 primeros datos: {datos[0]}, {datos[1]}, {datos[2]}")
    print('-------------------------------------------------------------------------------------------------------')

#2:
def test_compra_maxima_minima_provincia(datos, provincia):
    compras_maximas_minimas_por_provincia = compra_maxima_minima_provincia(datos, provincia)
    print("Probando la función compra_maxima_minima_provincia:...")
    print(f"Aquí se imprimen el máximo y el mínimo de la provincia dada: {compras_maximas_minimas_por_provincia}")
    print('-------------------------------------------------------------------------------------------------------')

#3:
def test_hora_menos_afluencia(datos):
    hora, afluencia = hora_menos_afluencia(datos)
    print("Probando la función hora_menos_afluencia:...")
    print(f"La hora de menor afluencia fue {hora} en la que hubo {afluencia} clientes")
    print('-------------------------------------------------------------------------------------------------------')

##################################################################################################################
if __name__ == '__main__':
    datos = leer_compras("data/compras.csv")
    test_leer_compras(datos)
    test_compra_maxima_minima_provincia((datos), ('Sevilla'))
    test_hora_menos_afluencia(datos)