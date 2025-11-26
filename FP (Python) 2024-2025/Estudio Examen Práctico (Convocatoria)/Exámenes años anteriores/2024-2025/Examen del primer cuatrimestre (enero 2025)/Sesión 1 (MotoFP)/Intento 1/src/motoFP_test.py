from MotoFP import *

#----------------------------------------------------------------------------------------------------------------------------------------------
#TEST DEL EJERCICIO 1: 
print()
print("TEST DEL EJERCICIO 1: ================================================================================================================")
carreras = lee_carreras("data\CSV de la sesión 1")
print(f"Se han leído un total de: {len(carreras)}")
print(f"Aquí se muestran las 3 primeras carreras: {carreras[:2]}")

#----------------------------------------------------------------------------------------------------------------------------------------------
#TEST DEL EJERCICIO 2: 
print()
print("TEST DEL EJERCICIO 2: ================================================================================================================")
sin_ganar1 = maximo_dias_sin_ganar(carreras, "Marc Marquez")
print(f"Para 'Marc Marquez': {sin_ganar1}")
sin_ganar2 = maximo_dias_sin_ganar(carreras, "Jorge Martin")
print(f"Para 'Jorge Martin': {sin_ganar2}")
sin_ganar3 = maximo_dias_sin_ganar(carreras, "Fredi Mercuri")
print(f"Para 'Freddy Mercuri': {sin_ganar3}")

#----------------------------------------------------------------------------------------------------------------------------------------------
#TEST DEL EJERCICIO 3: 
print()
print("TEST DEL EJERCICIO 3: ================================================================================================================")
mas_podios_circuito = piloto_mas_podios_por_circuito(carreras)
print(f"El piloto con más podios por circuitos es: {mas_podios_circuito}")

#----------------------------------------------------------------------------------------------------------------------------------------------
#TEST DEL EJERCICIO 4: 
print()
print("TEST DEL EJERCICIO 4: ================================================================================================================")
