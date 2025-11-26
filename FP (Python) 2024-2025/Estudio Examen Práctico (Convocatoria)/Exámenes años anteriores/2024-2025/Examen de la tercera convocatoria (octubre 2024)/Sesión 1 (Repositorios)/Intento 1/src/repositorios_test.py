from repositorios import *

#---------------------------------------------------------------------------------------------------------------------------------------------
#TEST DEL EJERCICIO 1: 
print()
print("TEST DEL EJERCICIO 1: ===============================================================================================================")
repositorios = lee_repositorios("data/repositorios.csv")
print(f"Se han leído: {len(repositorios)} repositorios")
print(f"Aquí se muestran los 2 primeros: {repositorios[:1]}")

#---------------------------------------------------------------------------------------------------------------------------------------------
#TEST DEL EJERCICIO 2: 
print()
print("TEST DEL EJERCICIO 2: ===============================================================================================================")
commits_por_anyo = total_commits_por_anyo(repositorios)
print(f"El total de commits por año para los repositorios públicos es: {commits_por_anyo}")

#---------------------------------------------------------------------------------------------------------------------------------------------
#*********************************************************************************************************************************************
#TEST DEL EJERCICIO 3: 
print()
print("TEST DEL EJERCICIO 3: ===============================================================================================================")
tasa_crecimiento_commits = n_mejores_repos_por_tasa_crecimiento(repositorios, 3)
print(f"Los 3 mejores repositorios según su tasa de crecimiento son: {tasa_crecimiento_commits}")

#*********************************************************************************************************************************************
#---------------------------------------------------------------------------------------------------------------------------------------------
#*********************************************************************************************************************************************
print()
print("TEST DEL EJERCICIO 4: ===============================================================================================================")

repo1 = buscar_repositorio_por_nombre(repositorios, "ProjectX")
recomendados1 = recomendar_lenguajes(repositorios, repo1)
print(f"Para el repositorio {repo1.nombre} que usa los lenguajes {repo1.lenguajes} se recomiendan: {recomendados1}")

repo2 = buscar_repositorio_por_nombre(repositorios, "MusicLibrary")
recomendados2 = recomendar_lenguajes(repositorios, repo2)
print(f"Para el repositorio {repo2.nombre} que usa los lenguajes {repo2.lenguajes} se recomiendan: {recomendados2}")

repo3 = buscar_repositorio_por_nombre(repositorios, "MyProject")
recomendados3 = recomendar_lenguajes(repositorios, repo3)
print(f"Para el repositorio {repo3.nombre} que usa los lenguajes {repo3.lenguajes} se recomiendan: {recomendados3}")

#*********************************************************************************************************************************************
#---------------------------------------------------------------------------------------------------------------------------------------------
#*********************************************************************************************************************************************
#TEST DEL EJERCICIO 5: 
print()
print("TEST DEL EJERCICIO 5: ===============================================================================================================")
media_minutos1 = media_minutos_entre_commits_por_usuario(repositorios, None, None)
print(f"Media de minutos entre commits para las fechas fecha_ini: None y fecha_fin: None: {media_minutos1}")
print()
media_minutos2 = media_minutos_entre_commits_por_usuario(repositorios, None, date(year=2021, month=12, day=31))
print(f"Media de minutos entre commits para las fechas fecha_ini: None y fecha_fin: 2021-12-31: {media_minutos2}")
print()
media_minutos3 = media_minutos_entre_commits_por_usuario(repositorios, date(year=2023, month=9, day=1), None)
print(f"Media de minutos entre commits para las fechas fecha_ini: 2023-09-01 y fecha_fin: None: {media_minutos3}")
print()
media_minutos4 = media_minutos_entre_commits_por_usuario(repositorios, date(year=2023, month=1, day=1), date(year=2023, month=11, day=1))
print(f"Media de minutos entre commits para las fechas fecha_ini: 2023-01-01 y fecha_fin: 2023-11-01: {media_minutos4}")

#*********************************************************************************************************************************************
#---------------------------------------------------------------------------------------------------------------------------------------------
