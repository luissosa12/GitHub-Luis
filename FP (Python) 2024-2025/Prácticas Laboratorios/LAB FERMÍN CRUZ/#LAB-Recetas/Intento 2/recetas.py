#EJERCICIO 1:
from typing import NamedTuple
from datetime import datetime, date
Ingrediente = NamedTuple("Ingrediente",
					[("nombre",str),
					 ("cantidad",float),
					 ("unidad",str)])
						 
Receta = NamedTuple("Receta", 
                    [("denominacion", str),
                     ("tipo", str),
                     ("dificultad", str),
                     ("ingredientes", list[Ingrediente]),
                     ("tiempo", int),
                     ("calorias", int),
                     ("fecha", date),
                     ("precio", float)])
#-------------------------------------------------------------------------------------------------------------------------
#EJERCICIOS DE CARGA DE DATOS:
# EJERCICIO 2:
import csv
def lee_recetas(ruta_fichero: str) -> list[Receta]:
    res = []
    with open(ruta_fichero, 'r', encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=';')
        next(lector)
        for denominacion, tipo, dificultad, ingredientes, tiempo, Calorias, Fecha_creacion, precio_estimado in lector:
            ingredientes = parsea_ingredientes(ingredientes)
            tiempo = int(tiempo)
            calorias = int(Calorias)
            fecha = datetime.strptime(Fecha_creacion, '%d/%m/%Y').date()
            precio = float(precio_estimado.replace(',', '.'))
            tupla = Receta(denominacion, tipo, dificultad, ingredientes, tiempo, calorias, fecha, precio)
            res.append(tupla)
    return res


# parsear_ingredientes:
def parsea_ingredientes(cadena: str) -> list[Ingrediente]:
    if not cadena:
        return []
    res = []
    for r in cadena.split(','):
        res.append(parsea_ingrediente(r))
    return res
#---------------------------------------------------------
# parsear_ingrediente:
def parsea_ingrediente(cadena: str) -> Ingrediente:
    nombre, cantidad, unidad = cadena.split('-')
    #otra forma:
    #   partes = cadena.split('-')

    #   nombre = partes[0].strip()
    #   cantidad = float(partes[1].strip())
    #   unidad = partes[2].strip()

    return Ingrediente(nombre, cantidad, unidad)
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#EJERCICIOS DE TRATAMIENTOS SECUENCIALES SIMPLES:
# EJERCICIO 3:
from typing import Optional
def ingredientes_en_unidad(lista_recetas: list[Receta], unidad_medida: Optional[str]) -> int:
    res = set()
    for r in lista_recetas:
        for i in r.ingredientes:
            if i.unidad == unidad_medida or unidad_medida is None:
                res.add(i.nombre)

    return len(res)
#-------------------------------------------------------------------------------------------------------------------------
# EJERCICIO 4:
def recetas_con_ingredientes(lista_recetas: list[Receta], ingredientes_tenemos: set[str]) -> list[tuple[str, int, float]]:
    res = set()
    for r in lista_recetas:
        for i in r.ingredientes:
            if i.nombre in ingredientes_tenemos:
                res.add((r.denominacion, r.calorias, r.precio))
    return res
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#EJERCICIOS DE MÁXIMOS, MÍNIMOS Y ORDENACIONES:
# EJERCICIO 5:
def receta_mas_barata(lista: list[Receta], tipos_recetas: set[str], n: Optional[int] = None) -> str:
    res = []
    for r in lista:
        if r.tipo in tipos_recetas:
            res.append(r)

    res.sort(key = lambda x:x.calorias)
    las_n_recetas = res[:n] if n is not None else res
    mas_barata = min(las_n_recetas, key = lambda x:x.precio)

    return mas_barata
#-------------------------------------------------------------------------------------------------------------------------
# EJERCICIO 6:
def recetas_baratas_con_menos_calorias(lista: list[Receta], n: int) -> list[tuple[str, int]]:
    res = []

    precio_total = [r.precio for r in lista]
    precio_medio = sum(precio_total) / len(precio_total)

    for r in lista:
        if r.precio <= precio_medio:
            res.append((r.denominacion, r.calorias))

    res.sort(key = lambda x:x[1])

    return res[:n]
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------