from suscripciones import *

#---------------------------------------------------------------------------------------------------------------------------------------------
#TEST DEL EJERCICIO 1: 
print()
print("TEST DEL EJERCICIO 1: ===============================================================================================================")
suscripciones = lee_suscripciones("data\CSV de la sesión 3")
print(f"Se han leído un total de: {len(suscripciones)} suscripciones")
print()
print(f"Aquí se muestran las 3 primeras: {suscripciones[:3]}")

#---------------------------------------------------------------------------------------------------------------------------------------------
#TEST DEL EJERCICIO 2: 
print()
print("TEST DEL EJERCICIO 2: ===============================================================================================================")
mas_rentables1 = suscripciones_mas_rentables(suscripciones, 3, None)
print(f"Las 3 suscripciones más rentables (sin filtrar) son: {mas_rentables1}")

mas_rentables2 = suscripciones_mas_rentables(suscripciones, 3, "BÁSICO")
print(f"Las 3 suscripciones más rentables filtrando por tipo de plan: ('BÁSICO') son: {mas_rentables2}")

#---------------------------------------------------------------------------------------------------------------------------------------------
#TEST DEL EJERCICIO 3: 
print()
print("TEST DEL EJERCICIO 3: ===============================================================================================================")
mas_perfiles1 = plan_mas_perfiles(suscripciones, None, None)
print(f"Sin filtrar fechas, el plan con más perfiles acumulados es: {mas_perfiles1[0]}, con un total de: {mas_perfiles1[1]} perfiles")

mas_perfiles2 = plan_mas_perfiles(suscripciones, date(year=2023, month=2, day=1), date(year=2023, month=3, day=31))
print(f"Entre el 1 de febrero de 2023 y el 31 de marzo de 2023:, el plan con más perfiles acumulados es: {mas_perfiles2[0]}, con un total de: {mas_perfiles2[1]} perfiles")

#---------------------------------------------------------------------------------------------------------------------------------------------
#TEST DEL EJERCICIO 4: 
print()
print("TEST DEL EJERCICIO 4: ===============================================================================================================")
media_dias_plan= media_dias_por_plan(suscripciones)
print(f"Duración media (en días) de suscripciones finalizadas por tipo de plan: {media_dias_plan}")

#---------------------------------------------------------------------------------------------------------------------------------------------
#TEST DEL EJERCICIO 5: 
print()
print("TEST DEL EJERCICIO 5: ===============================================================================================================")
addon_popular = addon_mas_popular_por_año(suscripciones)
print(f"El addons más popular por año es: {addon_popular}")

#---------------------------------------------------------------------------------------------------------------------------------------------
#*********************************************************************************************************************************************
#TEST DEL EJERCICIO 6: 
print()
print("TEST DEL EJERCICIO 6: ===============================================================================================================")
evolucion = evolucion_años(suscripciones)
print(f"Evolución de suscripciones por año: {evolucion}")

#---------------------------------------------------------------------------------------------------------------------------------------------
