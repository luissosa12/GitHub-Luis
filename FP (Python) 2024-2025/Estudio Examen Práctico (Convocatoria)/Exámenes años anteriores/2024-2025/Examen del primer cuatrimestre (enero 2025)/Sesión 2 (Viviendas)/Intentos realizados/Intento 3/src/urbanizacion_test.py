from urbanizacion import *

#---------------------------------------------------------------------------------------------------------------------------------------------
#TEST DEL EJERCICIO 1: 
print()
print("TEST DEL EJERCICIO 1: ===============================================================================================================")
viviendas = lee_viviendas("data\CSV de la sesión 2")
print(f"Se han leído un total de: {len(viviendas)} viviendas")
print(f"Aquí se muestran las 2 primeras: {viviendas[:2]}")

#---------------------------------------------------------------------------------------------------------------------------------------------
#TEST DEL EJERCICIO 2: 
print()
print("TEST DEL EJERCICIO 2: ===============================================================================================================")
mejoras_por_calle1 = total_mejoras_por_calle(viviendas, "par")
print(f"Número de mejoras en viviendas con número ('par'): {mejoras_por_calle1}")

mejoras_por_calle2 = total_mejoras_por_calle(viviendas, "impar")
print(f"Número de mejoras en viviendas con número ('impar'): {mejoras_por_calle2}")

#---------------------------------------------------------------------------------------------------------------------------------------------
#TEST DEL EJERCICIO 3: 
print()
print("TEST DEL EJERCICIO 3: ===============================================================================================================")
menos_tiempo = vivienda_con_mejora_mas_rapida(viviendas)
print(f"La vivienda que hizo una mejora en menos tiempo es: {menos_tiempo}")

#---------------------------------------------------------------------------------------------------------------------------------------------
#TEST DEL EJERCICIO 4: 
print()
print("TEST DEL EJERCICIO 4: ===============================================================================================================")
mayor_diferencia = calle_mayor_diferencia_precios(viviendas)
print(f"La calle con mayor diferencia de precios entre números impares y pares es: {mayor_diferencia}")

#---------------------------------------------------------------------------------------------------------------------------------------------
#*********************************************************************************************************************************************
#TEST DEL EJERCICIO 5: 
print()
print("TEST DEL EJERCICIO 5: ===============================================================================================================")
mas_valoradas1 = n_viviendas_top_valoradas_por_calle(viviendas, date(year=2020, month=1, day=1), 4)
print(f"Para n=4 y fecha=2020-01-01 las viviendas más valoradas son: {mas_valoradas1}")
print()
mas_valoradas2 = n_viviendas_top_valoradas_por_calle(viviendas, None, 3)
print(f"Con parámetros por defecto las viviendas más valoradas son: {mas_valoradas2}")

#*********************************************************************************************************************************************
#---------------------------------------------------------------------------------------------------------------------------------------------
#*********************************************************************************************************************************************
#TEST DEL EJERCICIO 6: 
print()
print("TEST DEL EJERCICIO 6: ===============================================================================================================")
metro_cuadrado = valor_metro_cuadrado_por_calle_y_año(viviendas)
print(metro_cuadrado)

#*********************************************************************************************************************************************
#---------------------------------------------------------------------------------------------------------------------------------------------
