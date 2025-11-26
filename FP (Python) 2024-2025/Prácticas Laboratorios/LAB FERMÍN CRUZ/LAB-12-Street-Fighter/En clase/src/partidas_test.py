from partidas import *

#1:
def test_lee_partidas(partidas):
    print("----------------------------------------------------------------------------------------------------------")
    print("1:")
    print("Probando la función lee_partidas:...")
    print(f"Se han leído {len(partidas)} partidas")
    print(f"Aquí se muestran las 3 primeras: {partidas[:3]}")
    print("----------------------------------------------------------------------------------------------------------")

#2:



if __name__ == '__main__':
    partidas = lee_partidas('data/games.csv')
    test_lee_partidas(partidas)