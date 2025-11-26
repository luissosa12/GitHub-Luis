from collections import namedtuple
import csv

FrecuenciaNombre = namedtuple('FrecuenciaNombre', 'año','nombre','frecuencia','genero')

#1:
def leer_frecuencias_nombres(ruta_fichero):
    with open(ruta_fichero, encoding ='utf-8') as f:
        res = []
        lector = csv.reader(f)
        next()
        
        for año, nombre, frecuencia, genero in lector:
            año = int(año)
            nombre = str(nombre)
            frecuencia = int(frecuencia)
            genero = str(genero)
            res.append(FrecuenciaNombre(año, nombre, frecuencia, genero))
        return res

#2:
def filtrar_por_genero(lista, genero):
    res = []
    for z in lista:
        if z.genero == genero:
            res.append(z)
    return res

#3:
def calcular_nombres(lista, genero):
    conjunto = set()
    for x in lista:
#Utilizamos la función: if genero == None para evaluar primero antes que nada si el valor que entregamos no es ninguno
        if genero == None or x.genero == genero:
            conjunto.add(x.nombre)
    return conjunto

#4:
def calcular_top_nombres_de_año(lista, año, numero_limite=10, genero=None):
    res = []
    for l in lista:
        if l.año == año and l.genero == genero:
            res.append((l.nombre, l.frecuencia))
#Lo primero es sacar del bucle el--> res.sort ya que una vez tenga toda la lista de tuplas creadas, las ordenamos/
#Introduciendo la función key=lambda, lambda es una función que vamos a crear en esa misma línea de código, lambda recibe los parámetros en su misma línea de manera que es--> lo_que_recibe:lo_que_queremos:que_devuelva/
#En este caso además está ordenado de menor a mayor y nosotros queremos que sea al revés, añadimos--> reverse = True/
    res.sort(key=lambda f:f[1], reverse = True)
#Ahora queremos imprimir la lista de tuplas ordenadas, pero sólo los primeros numero_limite elementos, por lo que ponemos--> :numero limite/
    return res[:numero_limite]

#5:
def calcular_nombres_ambos_generos(lista):
    hombres = calcular_nombres(lista,"Hombre")
    mujeres = calcular_nombres(lista,"Mujeres")
    return hombres & mujeres
#6:
