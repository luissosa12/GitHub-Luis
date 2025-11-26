from collections import namedtuple
import csv
from coordenadas import Coordenadas

CentroSanitario = namedtuple('CentroSanitario', 'nombre, localidad, coordenadas, estado, num_camas, acceso_minusvalidos, tiene_uci')


def leer_centros(ruta_fichero):
    with open(ruta_fichero, encoding ='utf-8') as f:
        res = []
        lector = csv.reader(f, delimiter = ";")
        next(lector)
#Se pone delimeter = ";" ya que Python de normal renococe una coma (,) entre valores de un csv, como en este caso es un punto y coma (;), se lo indicamos nosotros específicamente
        for nombre, localidad, latitud, longitud, estado, num_camas, acceso_minusvalidos, tiene_uci in lector:
            nombre = str(nombre.strip())
            localidad = str(localidad.strip())
            latitud = float(latitud.strip())
            longitud = float(longitud.strip())
            coordenadas = Coordenadas(latitud, longitud)
            estado = str(estado.strip())
            num_camas = int(num_camas.strip())
#strip() sirve para eliminar el espacio que hay antes del valor en el csv; en el csv, hay un espacio antes de la latitud y la longitud, al ejecutar el código sale error ya que no ejecuta el espacio bien, se elimina con el método strip()
            acceso_minusvalidos = acceso_minusvalidos == True
            tiene_uci = tiene_uci == True
            res.append(CentroSanitario(nombre, localidad, coordenadas, estado, num_camas, acceso_minusvalidos, tiene_uci))
    return res

def calcular_total_camas_centros_accesibles(lista):
    res = 0
    for c in lista:
        if c.acceso_minusvalidos == True:
            res += c.num_camas

