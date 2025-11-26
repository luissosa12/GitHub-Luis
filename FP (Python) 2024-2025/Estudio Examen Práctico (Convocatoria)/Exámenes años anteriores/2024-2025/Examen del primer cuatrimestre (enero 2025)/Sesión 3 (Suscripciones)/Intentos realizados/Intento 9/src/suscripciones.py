from typing import NamedTuple, List, Tuple, Dict, Set 
from datetime import datetime, date, time 
from collections import defaultdict, Counter 
import csv 
 
Suscripcion = NamedTuple("Suscripcion", 
                         [("nombre", str), 
                          ("dni", str), 
                          ("fecha_inicio", date), 
                          ("fecha_fin", date | None), # Será None si la suscripción sigue activa 
                          ("tipo_plan", str), 
                          ("num_perfiles", int), 
                          ("precio_mensual", float), 
                          ("addons", List[str]) 
                         ])

#---------------------------------------------------------------------------------------------------------------------------------------------
# OBSERVACIONES: 
#   • Si una suscripción sigue activa (fecha fin está vacía en el CSV) se almacenará el valor 
#       None en la tupla correspondiente. 
#   • Si una suscripción no tiene addons, se almacenará una lista vacía en la tupla 
#       correspondiente. 
#   • Tenga en cuenta que si lee el csv con csv.reader, los campos que aparecen 
#       entrecomillados en el CSV se obtendrán sin las comillas. 
#   • La cadena de formato para parsear las fechas es "%Y-%m-%d". 
#   • La duración en días de una suscripción se calcula como (fecha_fin  - 
#       fecha_inicio).days.  Para  aquellas  suscripciones  que  siguen  activas,  se  utilizará  la 
#       fecha actual como fecha fin. 
#   • Para  calcular el  importe  total  de  una  suscripción, se  considera  un precio  diario  igual 
#       al  precio  mensual  dividido  entre  30.  El  importe  total  se  calculará  multiplicando  el 
#       precio diario por el total de días de la suscripción.
#---------------------------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 1: -> Recibe la ruta de un fichero CSV y devuelve una lista de tuplas de tipo Suscripcion 
#                conteniendo todos los datos almacenados en el fichero.
#                (1 punto)
def lee_suscripciones(ruta_fichero: str) -> List[Suscripcion]: 
    res = []
    with open(ruta_fichero, 'r', encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=',')
        next(lector)

        for nombre, dni, fecha_inicio, fecha_fin, tipo_plan, num_perfiles, precio_mensual, addons in lector:
            nombre = str(nombre.strip())
            dni = str(dni.strip())
            fecha_inicio = datetime.strptime(fecha_inicio.strip(), "%Y-%m-%d").date()
            if fecha_fin == "":
                fecha_fin = None
            else:
                fecha_fin = datetime.strptime(fecha_fin.strip(), "%Y-%m-%d").date()
            tipo_plan = str(tipo_plan.strip()) #Básico, Estandar, Premium
            num_perfiles = int(num_perfiles.strip())
            precio_mensual = float(precio_mensual.strip())
            addons = parsea_list_addons(addons.strip())

            tupla = Suscripcion(nombre, dni, fecha_inicio, fecha_fin, tipo_plan, num_perfiles, precio_mensual, addons)
            res.append(tupla)
    
    return res

#FUNCIONES AUXILIARES: 
def parsea_list_addons(cadena: str) -> List[str]: 
    if len(cadena.strip()) > 0:
        trozos = cadena.strip().split()
        return [trocito for trocito in trozos]
    else:
        return []
    
#---------------------------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 2: -> Devuelve  las  n  suscripciones  más  rentables  (las  que  acumulen  un  mayor  importe  total),  de 
#                entre las que sean de alguno de los tipos de plan indicados por  tipos_plan. Si tipos_plan es 
#                None, se usarán todas las suscripciones para calcular el resultado. Para cada suscripción, se 
#                devuelve  una  tupla  con  el  dni  y  el  importe  total  de  la  suscripción.  Consulte  en  la  sección 
#                Observaciones cómo se calcula el importe total de una suscripción.
#                (1.5 puntos)
def suscripciones_mas_rentables(suscripciones: List[Suscripcion], n: int = 3, tipos_plan: Set[str]|None = None) -> List[Tuple[str, float]]: 
    res = defaultdict(float)
    
    for s in suscripciones:
        if (tipos_plan is None or s.tipo_plan in tipos_plan):
            if s.fecha_fin is None:
                fecha_fin = date(year=2025, month=1, day=15)
            else:
                fecha_fin = s.fecha_fin
            importe_total = (s.precio_mensual / 30) * (fecha_fin - s.fecha_inicio).days
            res[s.dni] = importe_total
    
    mas_rentables = sorted(res.items(), key=lambda x:x[1], reverse=True)[:n]

    return list(mas_rentables)

#---------------------------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 3: -> Devuelve una tupla con el tipo de plan y el total de perfiles correspondiente al plan que suma 
#                mayor número total de perfiles entre todas las suscripciones cuya  fecha_inicio esté dentro 
#                del  rango  indicado  por  los  parámetros  fecha_ini y  fecha_fin.  Ambas  fechas  fecha_ini y 
#                fecha_fin están incluidas en el rango. Si fecha_ini es None no se establece un límite inferior; 
#                si fecha_fin es None no se establece un límite superior.
#                (1.5 puntos)
def plan_mas_perfiles(suscripciones: List[Suscripcion], fecha_ini: date|None = None, fecha_fin: date|None = None) -> Tuple[str, int]: 
    res = defaultdict(int)
    
    for s in suscripciones:
        if (fecha_ini is None or s.fecha_inicio >= fecha_ini) and (fecha_fin is None or s.fecha_inicio <= fecha_fin):
            res[s.tipo_plan] += s.num_perfiles
    
    mas_perfiles = max(res.items(), key=lambda x:x[1])

    return mas_perfiles

#---------------------------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 4: -> Calcula la duración media (en días) de las suscripciones finalizadas (aquellas con  fecha_fin 
#                no  None)  agrupadas  por  tipo  de  plan.  Devuelve  un  diccionario  en  el  que  las  claves  son  los 
#                tipos de plan y los valores la media de días.
#                (2 puntos)
def media_dias_por_plan(suscripciones: List[Suscripcion]) -> Dict[str, float]: 
    res = defaultdict(list)
    
    for s in suscripciones:
        if (s.fecha_fin is not None):
            dias = (s.fecha_fin - s.fecha_inicio).days
            res[s.tipo_plan].append(dias)
    
    res2 = dict()
    for tipo_plan, dias in res.items():
        media_dias = (sum(dias) / len(dias))
        res2[tipo_plan] = media_dias

    return res2

#---------------------------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 5: -> Devuelve un diccionario que hace corresponder a cada año de inicio de suscripción el  addon 
#                que aparece en más suscripciones ese año.
#                (2 puntos)
def addon_mas_popular_por_año(suscripciones: List[Suscripcion]) -> Dict[int,str]: 
    res = defaultdict(Counter)

    for s in suscripciones:
        anyo = s.fecha_inicio.year
        res[anyo].update(s.addons)
    
    res2 = dict()
    for anyo, addons in res.items():
        addon_mas_popular = max(addons.items(), key=lambda x:x[1])
        res2[anyo] = addon_mas_popular[0]
    
    return res2

#---------------------------------------------------------------------------------------------------------------------------------------------
#*********************************************************************************************************************************************
#EJERCICIO 6: -> Calcula la variación anual (incrementos o decrementos) en el número total de suscripciones,  
#                devolviendo  una  lista  de  tuplas  con  el  año  y  la  diferencia  respecto  al  año  anterior.  La  lista 
#                estará ordenada cronológicamente por año. 
#                Para ello, considere lo siguiente:  
#                   • Cuando una suscripción se inicia en un año determinado, se suma una unidad al total 
#                     de suscripciones de ese año.  
#                   • Cuando una suscripción finaliza en un año determinado, se resta una unidad del total 
#                     de suscripciones de ese año. 
#                   • Si una suscripción se inicia y finaliza dentro del mismo año, su efecto se anula y no se 
#                     contabiliza en la variación.
#                (2 puntos)
def evolucion_años(suscripciones: List[Suscripcion]) -> List[Tuple[int, int]]:
    # Contamos las suscripciones iniciadas y finalizadas por año
    sus_por_año = defaultdict(int)

    for s in suscripciones:
        año_ini = s.fecha_inicio.year
        año_fin = s.fecha_fin.year if s.fecha_fin is not None else None

        # Si la suscripción empieza y termina en el mismo año, no afecta a la variación
        if año_fin is not None and año_ini == año_fin:
            continue
        
        sus_por_año[año_ini] += 1
        if año_fin is not None:
            sus_por_año[año_fin] -= 1

    # Ordenamos los años cronológicamente
    años_ordenados = sorted(sus_por_año.items())  # [(2022, +5), (2023, -2), ...]

    # Calculamos la diferencia con respecto al año anterior
    resultado = []
    for (año1, total1), (año2, total2) in zip(años_ordenados, años_ordenados[1:]):
        diferencia = total2 - total1
        resultado.append((año2, diferencia))

    return resultado

#---------------------------------------------------------------------------------------------------------------------------------------------
