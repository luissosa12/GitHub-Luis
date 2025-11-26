from collections import namedtuple
import matplotlib.pyplot as plt

RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')

def lee_poblacion(nombre_fichero):
    poblaciones = []
    with open(nombre_fichero, 'r', encoding='utf-8') as fichero:
        next(fichero)
        for linea in fichero:
            pais, codigo, año, censo = linea.strip().split(',')
            poblaciones.append(RegistroPoblacion(pais, codigo, int(año), int(censo)))
    return poblaciones

def filtra_por_codigo_o_nombre(poblaciones, nombre_o_codigo):
    return [p for p in poblaciones if p.pais == nombre_o_codigo or p.codigo == nombre_o_codigo]

def filtra_por_paises_y_anyo(poblaciones, anyo, paises):
    return [(p.pais, p.censo) for p in poblaciones if p.año == anyo and p.pais in paises]

def muestra_evolucion_poblacion(poblaciones, nombre_o_codigo):
    datos_filtrados = filtra_por_codigo_o_nombre(poblaciones, nombre_o_codigo)
    if not datos_filtrados:
        print(f"No se encontraron datos para {nombre_o_codigo}.")
        return

    lista_años = [p.año for p in datos_filtrados]
    lista_habitantes = [p.censo for p in datos_filtrados]
    titulo = f"Evolución de la población en {nombre_o_codigo}"

    plt.title(titulo)
    plt.plot(lista_años, lista_habitantes)
    plt.show()

def muestra_comparativa_paises_anyo(poblaciones, anyo, paises):
    datos_filtrados = filtra_por_paises_y_anyo(poblaciones, anyo, paises)
    if not datos_filtrados:
        print(f"No se encontraron datos para el año {anyo} y los países {paises}.")
        return

    lista_paises = [p[0] for p in sorted(datos_filtrados)]
    lista_habitantes = [p[1] for p in sorted(datos_filtrados)]

    titulo = f"Comparativa de población en el año {anyo}"
    plt.title(titulo)
    plt.bar(lista_paises, lista_habitantes)
    plt.show()
    