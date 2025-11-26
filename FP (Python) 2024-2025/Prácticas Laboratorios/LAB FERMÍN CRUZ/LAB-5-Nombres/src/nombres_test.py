#ESQUEMA BÁSICO TEST_FUNCIONES PYTHON:

from xxx import *

#Para cada función que queramos probar:
def test_xxxx(datos):
    print("Probando función XXXX...")
    #Llamamos a la función, y guardamos el resultado:
    res = XXXX(datos, ....)

    #Mostramos "algo" de lo que ha devuelto la función
    print(...)

if__name__ == '__main__':
    datos = leer_frecuencia_nombre("data/ijvhervbihvb.csv")
    test_XXXX(datos)