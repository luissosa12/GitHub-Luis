from consumo_electrico import *

#----------------------------------------------------------------------------------------------------------------------------------------------
#TEST DEL EJERCICIO 1: 
print("TEST DEL EJERCICIO 1: ================================================================================================================")
facturas = lee_facturas("data\CSV de la sesión 1")
print(f"Hay un total de: {len(facturas)} facturas")
print(f"Aquí se muestran las dos primeras: {facturas[:1]}")

#----------------------------------------------------------------------------------------------------------------------------------------------
#TEST DEL EJERCICIO 2: 
print()
print("TEST DEL EJERCICIO 2: ================================================================================================================")
precio1 = extrae_precio_por_mes(facturas, "única")
print(f"Precio por mes con tarifa única: {precio1}")
print()
precio2 = extrae_precio_por_mes(facturas, "tramos")
print(f"Precio por mes con tarifa tramos: {precio2}")

#----------------------------------------------------------------------------------------------------------------------------------------------
#TEST DEL EJERCICIO 3: 
print()
print("TEST DEL EJERCICIO 3: ================================================================================================================")
mayor_consumo_acumulado = busca_vivienda_mayor_consumo_acumulado(facturas)
print(f"La vivienda con mayor consumo acumulado es la que tiene como ID: {mayor_consumo_acumulado[0]} con un consumo total de: {mayor_consumo_acumulado[1]}kwh")

#----------------------------------------------------------------------------------------------------------------------------------------------
#TEST DEL EJERCICIO 4: 
print()
print("TEST DEL EJERCICIO 4: ================================================================================================================")


#----------------------------------------------------------------------------------------------------------------------------------------------