from collections import namedtuple
import matplotlib.pyplot as plt

# Definimos una tupla con nombre para almacenar la información de población
RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')

# Función que lee un fichero CSV y lo convierte en una lista de tuplas RegistroPoblacion
def lee_poblacion(nombre_fichero):
    poblaciones = []
    with open(nombre_fichero, 'r', encoding='utf-8') as fichero:
        next(fichero)  # Saltamos la primera línea si es un encabezado
        for linea in fichero:
            # Descomponemos cada línea en país, código, año y censo
            pais, codigo, año, censo = linea.strip().split(',')
            # Creamos un nuevo registro y lo añadimos a la lista
            poblaciones.append(RegistroPoblacion(pais, codigo, int(año), int(censo)))
    return poblaciones

# Función que filtra los datos de población por nombre de país o código
def filtra_por_codigo_o_nombre(poblaciones, nombre_o_codigo):
    # Devolvemos una lista de tuplas donde el país o código coincide con lo dado
    return [p for p in poblaciones if p.pais == nombre_o_codigo or p.codigo == nombre_o_codigo]

# Función que filtra por año y por un conjunto de países
def filtra_por_paises_y_anyo(poblaciones, anyo, paises):
    # Devolvemos una lista con el nombre del país y el censo en el año especificado
    return [(p.pais, p.censo) for p in poblaciones if p.año == anyo and p.pais in paises]

# Función que muestra la evolución de la población de un país en el tiempo
def muestra_evolucion_poblacion(poblaciones, nombre_o_codigo):
    # Filtramos los datos para el país/código especificado
    datos_filtrados = filtra_por_codigo_o_nombre(poblaciones, nombre_o_codigo)
    
    if not datos_filtrados:
        print(f"No se encontraron datos para {nombre_o_codigo}.")
        return

    # Creamos listas para los años y los censos
    lista_años = [p.año for p in datos_filtrados]
    lista_habitantes = [p.censo for p in datos_filtrados]
    titulo = f"Evolución de la población en {nombre_o_codigo}"

    # Mostramos la gráfica de evolución
    plt.title(titulo)
    plt.plot(lista_años, lista_habitantes)
    plt.show()

# Función que muestra una comparativa de la población de varios países en un año dado
def muestra_comparativa_paises_anyo(poblaciones, anyo, paises):
    # Filtramos los datos para el año y los países especificados
    datos_filtrados = filtra_por_paises_y_anyo(poblaciones, anyo, paises)
    
    if not datos_filtrados:
        print(f"No se encontraron datos para el año {anyo} y los países {paises}.")
        return

    # Creamos listas con los nombres de países y el censo en ese año
    lista_paises = [p[0] for p in sorted(datos_filtrados)]
    lista_habitantes = [p[1] for p in sorted(datos_filtrados)]

    # Mostramos la gráfica de barras comparando la población
    titulo = f"Comparativa de población en el año {anyo}"
    plt.title(titulo)
    plt.bar(lista_paises, lista_habitantes)
    plt.show()
