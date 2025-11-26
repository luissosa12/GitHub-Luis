from typing import NamedTuple, List, Set, Tuple, Dict, Optional 
from datetime import datetime, date, time 
from collections import defaultdict, Counter 
import csv 

Commit = NamedTuple("Commit",      
       [("id", str), # Identificador alfanumérico del commit 
        ("mensaje", str), # Mensaje asociado al commit 
        ("fecha_hora", datetime) # Fecha y hora en la que se registró el commit 
       ]) 
Repositorio = NamedTuple("Repositorio",      
      [("nombre", str),  # Nombre del repositorio 
       ("propietario", str), # Nombre del usuario propietario 
       ("lenguajes", Set[str]),  # Conjunto de lenguajes usados 
       ("privado", bool),  # Indica si es privado o público 
       ("commits", List[Commit])  # Lista de commits realizados 
       ])

#---------------------------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 1: -> dada una cadena de texto con la ruta de un fichero CSV, devuelve una lista de tuplas de 
#                tipo Repositorio con la información contenida en el fichero.
#                (1,75 puntos)
def lee_repositorios(ruta_fichero: str) -> List[Repositorio]: 
    res = []
    with open(ruta_fichero, 'r', encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=',')
        next(lector)

        for nombre, propietario, lenguajes, privado, commits in lector:
            nombre = str(nombre.strip())
            propietario = str(propietario.strip())
            lenguajes = parsea_set_lenguajes(lenguajes.strip())
            privado = bool(privado.strip().upper() == "TRUE") #TRUE -> True
            commits = parsea_list_commits(commits.strip())

            tupla = Repositorio(nombre, propietario, lenguajes, privado, commits)
            res.append(tupla)
    
    return res

#FUNCIONES AUXILIARES: 
def parsea_commits(cadena: str) -> Commit: 
    trozos = cadena.strip().split("#")

    id = str(trozos[0].strip())
    mensaje = str(trozos[1].strip())
    fecha_hora = datetime.strptime(trozos[2].strip(), "%Y-%m-%d %H:%M:%S")

    return Commit(id, mensaje, fecha_hora)

def parsea_list_commits(cadena: str) -> List[Commit]: 
    cadena = cadena.strip().strip("[]")  # Elimina los corchetes del principio y final
    if len(cadena) > 0:
        trozos = cadena.split(";")
        return [parsea_commits(trocito) for trocito in trozos]
    else:
        return []
    
def parsea_set_lenguajes(cadena: str) -> Set[str]: 
    res = set()

    if len(cadena.strip()) > 0:
        trozos = cadena.strip().split(",")
        res.update(trocito.strip() for trocito in trozos)
        return res
    
    else:
        return res
    
#---------------------------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 2: -> dada una lista de tuplas de tipo Repositorio, devuelve un diccionario en el que 
#                las claves son los años, y los valores el número total de commits registrados en el año dado como clave para 
#                los repositorios públicos.
#                (1,25 puntos)
def total_commits_por_anyo(repositorios: List[Repositorio]) -> Dict[int, int]: 
    res = defaultdict(int)

    for r in repositorios:
        for c in r.commits:
            año = c.fecha_hora.year
            if r.privado == False:
                res[año] += len(r.commits)
    
    return res

#---------------------------------------------------------------------------------------------------------------------------------------------
#*********************************************************************************************************************************************
#EJERCICIO 3: -> dada  una  lista  de  tuplas  de  tipo  Repositorio  y  un  número 
#                entero n (con valor por defecto igual a 3), devuelve una lista con los n nombres de los repositorios y sus tasas 
#                de crecimiento más altas.
#                (1,75 puntos)
def calcular_tasa_crecimiento(repositorio: Repositorio) -> float:
    commits = repositorio.commits
    if len(commits) < 2:
        return 0.0
    dias = (commits[-1].fecha_hora - commits[0].fecha_hora).days
    if dias < 1:
        return 0.0
    
    return len(commits) / dias

from typing import List, Tuple, Optional

def n_mejores_repos_por_tasa_crecimiento(repositorios: List[Repositorio], n: Optional[int] = 3) -> List[Tuple[str, float]]:
    repos_y_tasas = [(repo.nombre, calcular_tasa_crecimiento(repo)) for repo in repositorios]
    repos_ordenados = sorted(repos_y_tasas, key=lambda t: t[1], reverse=True)
    return repos_ordenados[:n]

#*********************************************************************************************************************************************
#---------------------------------------------------------------------------------------------------------------------------------------------
#*********************************************************************************************************************************************
#EJERCICIO 4: -> dada una lista de tuplas de tipo Repositorio y un repositorio específico, devuelve 
#                un  conjunto  con  los  lenguajes  de  programación  recomendados  para  dicho  repositorio.  Los  lenguajes 
#                recomendados  son  aquellos  que  se  usan  en  repositorios  similares  al  repositorio  dado. Se  considera  que  un 
#                repositorio es similar al dado si comparte al menos uno de los lenguajes de programación con el repositorio 
#                dado. Por ejemplo, si queremos hacer una recomendación para el repositorio "LAB-FP", cuyo lenguaje es Java, 
#                podemos  considerar  similar  el  repositorio  "LAB-Calificaciones",  que  utiliza  Java  y  Python,  ya  que  ambos 
#                comparten el lenguaje Java. En este caso, se recomendaría Python como nuevo lenguaje para el repositorio "LAB-FP".
#                (2,5 puntos)
def recomendar_lenguajes(repositorios: List[Repositorio], repositorio: Repositorio) -> Set[str]:
    recomendados = set()

    for otro_repo in repositorios:
        if otro_repo.nombre != repositorio.nombre:
            lenguajes_comunes = repositorio.lenguajes.intersection(otro_repo.lenguajes)
            if lenguajes_comunes:
                nuevos = otro_repo.lenguajes - repositorio.lenguajes
                recomendados.update(nuevos)

    return recomendados

#FUNCIONES AUXILIARES: 
def buscar_repositorio_por_nombre(repos: List[Repositorio], nombre: str) -> Repositorio:
    for repo in repos:
        if repo.nombre == nombre:
            return repo
    raise ValueError(f"Repositorio '{nombre}' no encontrado.")

#*********************************************************************************************************************************************
#---------------------------------------------------------------------------------------------------------------------------------------------
#*********************************************************************************************************************************************
#EJERCICIO 5: -> media_minutos_entre_commits_por_propietario: dada una lista de tuplas de tipo Repositorio, una 
#                fecha inicial y una fecha final (ambas opcionales con valor por defecto None), devuelve un diccionario en el 
#                que las claves son los nombres de los propietarios de los repositorios, y los valores la media de minutos entre 
#                los  commits  realizados  en  los  repositorios  de  cada  propietario  dentro  del  intervalo  de  fechas  dado  por 
#                [fecha_ini, fecha_fin). Si fecha_ini es None no se restringe el inicio del intervalo, y si fecha_fin es None, no se 
#                limita  el  final  del  intervalo.  Si  ambas  fechas  son  None,  se  consideran  todos  los  commits  sin  restricción 
#                temporal.  
#                Es  importante  tener  en  cuenta  que  un  mismo  propietario  puede  tener  varios  repositorios,  por  lo  que  los 
#                cálculos  abarcarán  todos  los  commits  realizados  en  los  repositorios  de  ese  propietario  dentro  del  intervalo 
#                especificado.
import statistics

def media_minutos_entre_commits(lista_commits: List[Commit]) -> Optional[float]:
    if len(lista_commits) < 2:
        return None
    
    # Ordenar los commits por fecha
    commits_ordenados = sorted(lista_commits, key=lambda c: c.fecha_hora)

    # Calcular las diferencias de tiempo entre cada par consecutivo
    diferencias = [
        (c2.fecha_hora - c1.fecha_hora).total_seconds() / 60
        for c1, c2 in zip(commits_ordenados, commits_ordenados[1:])
    ]

    return statistics.mean(diferencias)

from collections import defaultdict
from typing import Optional, Dict
from datetime import date

def media_minutos_entre_commits_por_usuario(
        repositorios: List[Repositorio],
        fecha_ini: Optional[date] = None,
        fecha_fin: Optional[date] = None
    ) -> Dict[str, float]:

    # Agrupar commits por propietario
    commits_por_usuario = defaultdict(list)

    for repo in repositorios:
        for commit in repo.commits:
            fecha_commit = commit.fecha_hora.date()
            if (fecha_ini is None or fecha_commit >= fecha_ini) and \
               (fecha_fin is None or fecha_commit < fecha_fin):
                commits_por_usuario[repo.propietario].append(commit)

    # Calcular la media de minutos entre commits para cada usuario
    resultado = dict()
    for usuario, commits in commits_por_usuario.items():
        media = media_minutos_entre_commits(commits)
        if media is not None:
            resultado[usuario] = media

    return resultado

#*********************************************************************************************************************************************
#---------------------------------------------------------------------------------------------------------------------------------------------
