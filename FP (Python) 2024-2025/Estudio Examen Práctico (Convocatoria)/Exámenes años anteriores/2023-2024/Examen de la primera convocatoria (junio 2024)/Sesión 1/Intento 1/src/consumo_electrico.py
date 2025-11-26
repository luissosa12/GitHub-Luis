from typing import NamedTuple, Set, List, Dict, Tuple 
from datetime import datetime, date, time 
import csv 
 
IntervaloFechas = NamedTuple("IntervaloFechas",  
                     [("inicio", date), ("fin", date)]) 
 
Factura = NamedTuple("Factura",  
                     [("id_vivienda", str), 
                      ("tipo_vivienda", str), 
                      ("barrio", str), 
                      ("tipo_tarifa", str), 
                      ("periodo_facturado", IntervaloFechas), 
                      ("coste_potencia", float), 
                      ("consumo_punta", float), 
                      ("consumo_valle", float), 
                      ("precio_punta", float), 
                      ("precio_valle", float), 
                      ("importe_total", float)]) 

#----------------------------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 1: -> recibe la ruta de un fichero CSV y devuelve una lista de tuplas de tipo Factura
#                conteniendo todos los datos almacenados en el fichero. La lista devuelta debe estar ordenada por el
#                campo periodo_facturado.inicio. (1 punto)
def lee_facturas(ruta_fichero: str) -> List[Factura]:
    res = []
    with open(ruta_fichero, 'r', encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)

        for id_vivienda, tipo_vivienda, barrio, tipo_tarifa, periodo_inicio, periodo_fin, coste_potencia, consumo_punta, consumo_valle, precio_kwh, importe_total in lector:
            id_vivienda = str(id_vivienda.strip())
            tipo_vivienda = str(tipo_vivienda.strip())
            barrio = str(barrio.strip())
            tipo_tarifa = str(tipo_tarifa.strip())

            periodo_inicio = datetime.strptime(periodo_inicio.strip(), "%Y-%m-%d").date()
            periodo_fin = datetime.strptime(periodo_fin.strip(), "%Y-%m-%d").date()
            periodo_facturado = IntervaloFechas(periodo_inicio, periodo_fin)

            coste_potencia = float(coste_potencia.strip())
            consumo_punta = float(consumo_punta.strip())
            consumo_valle = float(consumo_valle.strip())

            if tipo_tarifa == "única":
                precio_punta = precio_valle = float(precio_kwh)
            else:
                precio_punta, precio_valle = [float(x) for x in precio_kwh.split("/")]

            importe_total = float(importe_total.strip())

            tupla = Factura(id_vivienda, tipo_vivienda, barrio, tipo_tarifa, periodo_facturado, coste_potencia, consumo_punta, consumo_valle, precio_punta, precio_valle, importe_total)

            res.append(tupla)
    return sorted(res, key=lambda x:x.periodo_facturado.inicio)

#----------------------------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 2: -> recibe una lista de facturas y un tipo de tarifa, y devuelve un diccionario en el
#                que las claves son cadenas "año-mes" (por ejemplo, "2023-01") y los valores son tuplas con el precio
#                por kWh en horario punta y valle para dicho tipo de tarifa de cada mes. Tenga en cuenta que el precio
#                del kWh es igual para todos los clientes del mismo tipo de contrato para cada mes. (1 punto)
#                Nota: Para obtener la cadena "año-mes" puede utilizar el método strftime del tipo date, pasándole la cadena de formato 
#                "%Y-%m".
def extrae_precio_por_mes(facturas: List[Factura], tipo_tarifa: str) -> Dict[str, Tuple[float, float]]:
    res = dict()

    for f in facturas:
        if f.tipo_tarifa == tipo_tarifa: 
            mes = f.periodo_facturado.inicio.strftime("%Y-%m")
            res[mes] = f.precio_punta, f.precio_valle

    return res 

#----------------------------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 3: -> recibe una lista de facturas y devuelve una tupla con el
#                identificador de la vivienda con mayor consumo acumulado, y el valor de dicho consumo acumulado. El
#                consumo acumulado de una vivienda es la suma de los consumos tanto de horario punta como de
#                horario valle de todas las facturas de esa vivienda contenidas en la lista recibida. (1 punto)
from collections import defaultdict

def busca_vivienda_mayor_consumo_acumulado(facturas: List[Factura]) -> Tuple[str, float]:
    res = defaultdict(float)

    for f in facturas:
        res[f.id_vivienda] += (f.consumo_punta + f.consumo_valle)
    
    max_vivienda = max(res.items(), key=lambda x:x[1])

    return [max_vivienda[0], max_vivienda[1]]

#----------------------------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 4: -> recibe una lista de facturas y un entero top_n, y devuelve una
#                lista con los top_n barrios con mayor consumo medio en horario valle. (1,5 puntos)
from collections import defaultdict

def barrios_mayor_consumo_valle_medio(facturas: List[Factura], top_n: int) -> List[str]:
    consumo = defaultdict(float)
    conteo = defaultdict(int)

    for f in facturas:
        consumo[f.barrio] += f.consumo_valle
        conteo[f.barrio] += 1

    for barrio in consumo:
        consumo[barrio] /= conteo[barrio]  # media

    return [barrio for barrio, _ in sorted(consumo.items(), key=lambda x: x[1], reverse=True)[:top_n]]

#----------------------------------------------------------------------------------------------------------------------------------------------
