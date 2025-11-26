from typing import NamedTuple, List, Tuple, Set, Dict 
from datetime import datetime, date, time 
from collections import defaultdict, Counter 
import csv 
 
Mejora = NamedTuple("Mejora",      
       [("denominacion", str),  
        ("coste", int),  
        ("fecha", date)]) 
 
Vivienda = NamedTuple("Vivienda",      
      [("propietario", str), 
       ("calle", str), 
       ("fecha_adquisicion", date), 
       ("numero", int), 
       ("metros",float), 
       ("precio",int),         
       ("mejoras", List[Mejora])])

#---------------------------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 1: -> Recibe la ruta de un fichero CSV y devuelve una lista de tuplas de tipo  Vivienda conteniendo 
#                todos los datos almacenados en el fichero. 
#                Antes  de  implementar  la  función  anterior,  implemente  una  función  auxiliar  que  dada  una 
#                cadena de texto con las mejoras separadas por *, devuelva una lista de tipo Mejora. Tenga en 
#                cuenta que si la cadena de texto está vacía la función debe devolver una lista vacía 
#                (compruébelo en el penúltimo registro de los resultados esperados).
#                (1,5 puntos)
def lee_viviendas(ruta_fichero: str) -> List[Vivienda]: 
    res = []
    with open(ruta_fichero, 'r', encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=';')
        next(lector)

        for propietario, calle, numero, fecha_adquisicion, metros, precio, mejoras in lector:
            propietario = str(propietario.strip())
            calle = str(calle.strip())
            numero = int(numero.strip())
            fecha_adquisicion = datetime.strptime(fecha_adquisicion.strip(), "%d/%m/%Y").date()
            metros = float(metros.strip())
            precio = int(precio.strip())
            mejoras = parsea_list_mejoras(mejoras.strip())

            tupla = Vivienda(propietario, calle, fecha_adquisicion, numero, metros, precio, mejoras)
            res.append(tupla)

    return res

#FUNCIONES AUXILIARES:
def parsea_mejora(cadena: str) -> Mejora: 
    trozos = cadena.split("-")

    denominacion = str(trozos[0].strip())
    coste = int(trozos[1].strip())
    fecha = datetime.strptime(trozos[2].strip(), "%d/%m/%Y").date()

    return Mejora(denominacion, coste, fecha)

def parsea_list_mejoras(cadena: str) -> List[Mejora]: 
    if len(cadena.split()) > 0:
        trozos = cadena.split("*")
        return [parsea_mejora(trocito) for trocito in trozos]
    else:
        return []

#---------------------------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 2: -> Devuelve un diccionario que hace corresponder cada calle con el número total de mejoras de 
#                las viviendas de número par o impar de esa calle, según sea el valor del parámetro 
#                par_impar. El parámetro par_impar puede tomar los valores "par" o "impar".
#                (1,25 puntos)
def total_mejoras_por_calle (viviendas: List[Vivienda], par_impar: str) -> Dict[str,int]: 
    res = defaultdict(int)

    for v in viviendas:
        if (par_impar == "par") and (v.numero % 2 == 0):
            res[v.calle] += len(v.mejoras)
        elif (par_impar == "impar") and (v.numero % 2 != 0):
            res[v.calle] += len(v.mejoras)
    
    return res

#---------------------------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 3: -> Devuelve una tupla con información de la vivienda que menos días tardó en hacer una mejora 
#                desde que fue adquirida. La tupla contendrá el propietario, la calle, el número, el número de 
#                días transcurridos entre la adquisición de la vivienda y la primera mejora, y la denominación 
#                de esa mejora. Tenga en cuenta que las mejoras no están ordenadas por fecha.
#                (1,25 puntos)
def vivienda_con_mejora_mas_rapida(viviendas: List[Vivienda]) -> Tuple[str, str, int, int, str]: 
    minima = None
    dias_min = None

    for v in viviendas:
        for m in v.mejoras:
            dias = (m.fecha - v.fecha_adquisicion).days
            if dias_min is None or dias < dias_min:
                dias_min = dias
                minima = (v.propietario, v.calle, v.numero, dias, m.denominacion)

    return minima

#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------
#*********************************************************************************************************************************************
#EJERCICIO 4: -> Devuelve  la  calle  en  la  que  hay  una  mayor  diferencia  entre  la  suma  de  los  precios  de  las 
#                viviendas con número impar y la suma de los precios de las viviendas con número par. Utilice 
#                el valor absoluto (función abs) de la diferencia de ambas sumas de precios.
#                (2 puntos)
def calle_mayor_diferencia_precios(viviendas: List[Vivienda]) -> str:
    res = defaultdict(int)

    for v in viviendas:
        if (v.numero % 2 != 0):     # impar → se suma
            res[v.calle] += v.precio
        elif (v.numero % 2 == 0):   # par → se resta
            res[v.calle] -= v.precio

    # Buscar la calle con mayor diferencia absoluta
    return max(res, key=lambda calle: abs(res[calle]))

#*********************************************************************************************************************************************
#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------
#*********************************************************************************************************************************************
#EJERCICIO 5: -> Devuelve un diccionario que hace corresponder cada calle con una lista de tuplas formadas 
#                por  nombre  del  propietario,  el  número  de  la  vivienda  y  el  valor  de  cada  vivienda,  de  las  n 
#                viviendas más valoradas de la calle de que se trate, para las viviendas adquiridas en la  fecha 
#                dada o con posterioridad. Si fecha es None, se tendrán en cuenta todas las viviendas. El valor 
#                de  una  vivienda se  calcula  como  el  precio de  compra  más  el  coste de  las mejoras que  se  le 
#                hayan realizado.
#                (2 puntos)
def n_viviendas_top_valoradas_por_calle(viviendas: List[Vivienda], fecha: date | None = None, n: int = 3) -> Dict[str, List[Tuple[str, int, int]]]:

    agrupadas = defaultdict(list)

    for v in viviendas:
        if fecha is None or v.fecha_adquisicion >= fecha:
            valor = v.precio + sum(m.coste for m in v.mejoras)
            agrupadas[v.calle].append((v.propietario, v.numero, valor))

    resultado = {
        calle: sorted(lista, key=lambda t: t[2], reverse=True)[:n]
        for calle, lista in agrupadas.items()
    }

    return resultado

#*********************************************************************************************************************************************
#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------
#*********************************************************************************************************************************************
#EJERCICIO 6: -> Se quiere obtener el precio medio del metro cuadrado de las viviendas de cada calle por 
#                año. Para ello, la función debe devolver una lista de tuplas, ordenada de menor a mayor año. 
#                Cada tupla estará formada por dos elementos:  
#                   1. El año. 
#                   2. Una lista de tuplas con el nombre de la calle y el precio medio del metro cuadrado de las 
#                   viviendas de la calle en ese año. Esta lista estará ordenada de mayor a menor precio medio.
#                (2 puntos)
def valor_metro_cuadrado_por_calle_y_año(viviendas: List[Vivienda]) -> List[Tuple[int, List[Tuple[str, float]]]]:
    # Diccionario: {año: {calle: [precio/metro, precio/metro, ...]}}
    datos = defaultdict(lambda: defaultdict(list))

    for v in viviendas:
        año = v.fecha_adquisicion.year
        precio_m2 = v.precio / v.metros
        datos[año][v.calle].append(precio_m2)

    resultado = []

    for año in sorted(datos):
        datos_calle = datos[año]
        
        medias = []
        for calle, valores in datos_calle.items():
            media = sum(valores) / len(valores)
            medias.append((calle, media))

        # Ordenar calles por media descendente
        medias_ordenadas = sorted(medias, key=lambda t: t[1], reverse=True)

        resultado.append((año, medias_ordenadas))

    return resultado

#*********************************************************************************************************************************************
#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------
