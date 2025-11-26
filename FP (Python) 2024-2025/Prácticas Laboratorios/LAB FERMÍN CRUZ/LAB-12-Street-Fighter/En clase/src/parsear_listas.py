def parsear_lista_1(cadena: str) -> list[str]:
    lista_cadenas = cadena.split(',')
    res = []
    for c in lista_cadenas:
        res.append(c.strip)
    return res