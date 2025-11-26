#Parsear listas (forma 1):
def parsea_lista_1(cadena: str) -> list[str]:
    lista_cadenas = cadena.split(',')
    res = []
    for c in lista_cadenas:
        res.append(c.strip)
    return res
#--------------------------------------------------
#Parsear listas (forma 2):
def parsea_lista_2(cadena: str) -> list[str]:
    return[c.strip() for c in cadena.split(',')]