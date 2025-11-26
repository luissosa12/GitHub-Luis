from coordenadas import *

def test_calcular_distancia(c1, c2):
    print('Probando la función: calcular_distancia...:')
    distancia = calcular_distancia(c1, c2)
    print(f"La distancia entre {c1} y {c2} es: {distancia}")

def test_calcular_media_coordenadas(lista_coordenadas):
    print('Probando la función: calcular_media_distancia...:')
    media = calcular_media_coordenadas(lista_coordenadas)
    print(f"La media de las coordenadas es: {media}")

if __name__ == "__main__":
    lista_coordenadas = [
    Coordenadas(1.0, 2.0),
    Coordenadas(2.0, 3.0),
    Coordenadas(5.2, 1.2),
    ]

test_calcular_distancia(lista_coordenadas[0], lista_coordenadas[1])
test_calcular_media_coordenadas(lista_coordenadas)