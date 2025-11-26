from festivales import *

#---------------------------------------------------------------------------------------------------------------------------------------------
#TEST DEL EJERCICIO 1: 
print("TEST DEL EJERCICIO 1: ================================================================================================================")
festivales = lee_festivales("data\CSV de la sesión 1")
print(f"Se han leído: {len(festivales)} festivales")
print(f"Aquí se muestran los 3 primeros festivales: {festivales[:2]}")

#---------------------------------------------------------------------------------------------------------------------------------------------
#TEST DEL EJERCICIO 2: 
print("TEST DEL EJERCICIO 2: ================================================================================================================")
facturado1 = total_facturado(festivales, None, None)
print(f"Entre None y None el total es: {facturado1}")

facturado2 = total_facturado(festivales, None, date(year=2024, month=6, day=15))
print(f"Entre None y 2024-06-15 el total es: {facturado2}")

facturado3 = total_facturado(festivales, date(year=2024, month=6, day=15), None)
print(f"Entre 2024-06-15 y None el total es: {facturado3}")

facturado4 = total_facturado(festivales, date(year=2024, month=6, day=1), date(year=2024, month=6, day=15))
print(f"Entre 2024-06-01 y 2024-06-15 el total es: {facturado4}")

facturado5 = total_facturado(festivales, date(year=2024, month=6, day=1), date(year=2024, month=6, day=23))
print(f"Entre 2024-06-01 y 2024-06-23 el total es: {facturado5}")

#---------------------------------------------------------------------------------------------------------------------------------------------
#TEST DEL EJERCICIO 3: 
print("TEST DEL EJERCICIO 3: ================================================================================================================")
mas_festivales = artista_top(festivales)
print(f"El artista que ha actuado en más festivales es: {mas_festivales[1]}, con un total de: {mas_festivales[0]} festivales")

#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------
#*********************************************************************************************************************************************
#TEST DEL EJERCICIO 4: 
print("TEST DEL EJERCICIO 4: ================================================================================================================")
mas_beneficio = mes_mayor_beneficio_medio(festivales)
print(f"El mes con más beneficio es: {mas_beneficio}")

#*********************************************************************************************************************************************
#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------
#TEST DEL EJERCICIO 5: 
print("TEST DEL EJERCICIO 5: ================================================================================================================")
comunes1 = artistas_comunes(festivales, "Creamfields", "Tomorrowland")
print(f"Los artistas comunes entre Creamfields y Tomorrowland son: {comunes1}")

comunes2 = artistas_comunes(festivales, "Primavera Sound", "Coachella")
print(f"Los artistas comunes entre Primavera Sound y Coachella son: {comunes2}")

comunes3 = artistas_comunes(festivales, "Iconica Fest", "Primavera Sound")
print(f"Los artistas comunes entre Iconica Fest y Primavera Sound son: {comunes3}")

#---------------------------------------------------------------------------------------------------------------------------------------------
#TEST DEL EJERCICIO 6: 
print("TEST DEL EJERCICIO 6: ================================================================================================================")
top_festivales1 = festivales_top_calidad_por_duracion(festivales, 1)
print(f"Los mejores 1 festivales ordenados por número de días son: {top_festivales1}")

top_festivales2 = festivales_top_calidad_por_duracion(festivales, 3)
print(f"Los mejores 3 festivales ordenados por número de días son: {top_festivales2}")

#---------------------------------------------------------------------------------------------------------------------------------------------
