from typing import NamedTuple
import csv

RegistroExtranjeria = NamedTuple('RegistroExtranjeria', 
                                    [
                                        ("distrito", str),
                                        ("seccion", str),
                                        ("barrio", str),
                                        ("pais", str),
                                        ("hombres", int),
                                        ("mujeres", int)
                                    ])

#1
def leer_datos_extranjeria(ruta_fichero: str) -> list[RegistroExtranjeria]:
    with open (ruta_fichero, encoding = 'utf-8') as f:
        res = []
        lector = csv.reader(f)
        next(lector)
        for distrito, seccion, barrio, pais, hombres, mujeres in lector:
            distrito = str(distrito)
            seccion = str(seccion)
            barrio = str(barrio)
            pais = str(pais)
            hombres = int(hombres)
            mujeres = int(mujeres)
            res.append(RegistroExtranjeria(distrito, seccion, barrio, pais, hombres, mujeres))
        return res

#2
def numero_nacionalidades_distintas(registros: list[RegistroExtranjeria]) -> int:
    res = set()
    for r in registros:
        res.add(r.pais)
    return len(res)

#3
def secciones_distritos_con_extranjeros_nacionalidades(
                    registros: list[RegistroExtranjeria],
                    paises: set[str]) -> list[tuple[str,str]]: 
    distritos = set()
    for r in registros:
        if r.pais in paises:
            distritos.add((r.distrito, r.seccion))
    
    return sorted(distritos)

#4
def total_extranjeros_por_pais(registros: list[RegistroExtranjeria]) -> dict[str,int]:
    pass

#5
def top_n_extranjeria(registros: list[RegistroExtranjeria], n: int=3) -> list[tuple[str,int]]:
    total_por_pais = total_extranjeros_por_pais(registros)
#Ordenamos de mayor a menor número de items del diccionario:
    res = sorted(total_por_pais.items(), key = lambda tupla:tupla[1], reverse = True)
#Devolvemos los primeros n elementos de la lista
    return res[:n]

#-----------------------------------------------------------------------------------------------------
#SUMAR VALORES A UN VALOR DE UN DICCIONARIO:
#Ej: calcular cuantas personas hay de un mismo país en todos los distritos:
#res = {}
#for r in registros:
#   if r.pais not in res:
#       res[r.pais] = 0
#   res[r.pais] += r.hombres + r.mujeres