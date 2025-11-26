from centros import *

def test_leer_centros(datos):
    print('Probando la función: leer_centros...')
    print(f"Se han leido {len(datos)} registros.")
    print(f"Aquí se muestran los 3 primeros datos: {datos[0]}, {datos[1]}, {datos[2]}")

if __name__ == '__main__':
    datos = leer_centros("data/centrosSanitarios.csv")
    test_leer_centros(datos)