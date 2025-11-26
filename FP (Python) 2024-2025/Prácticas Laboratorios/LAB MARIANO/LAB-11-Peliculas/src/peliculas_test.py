from peliculas import *

def test_lee_peliculas(peliculas):
    print('----------------------------------------------------------------------------------------------------------')
    print("1:")
    print("Probando la función: lee_peliculas...:")
    print(f"Se han leído {len(peliculas)} películas")
    print(f"Las tres primeras son: {peliculas[:3]}")
    print('----------------------------------------------------------------------------------------------------------')



if __name__ == '__main__':
    peliculas = lee_peliculas('data/peliculas.csv')
    test_lee_peliculas(peliculas)