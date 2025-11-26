'''
Created on 9 ene. 2019

@author: Juanmi
'''
import csv
from datetime import time
from collections import namedtuple


Registro = namedtuple('Registro', 'momento cadenaTV audiencias')
Cadenas = ['TVE1', 'La2', 'A3TV','Cuatro','Tele5','laSexta']
Segmentos = ['NINOS', 'JOVENES', 'ADULTOS', 'MAYORES', 'TODOS']

def lee_mediciones(fichero):
    list_registro=[]
    with open(fichero, encoding='utf-8') as f:
        lector=csv.reader(f)
        for hora,minuto,cadenaTV,aud1,aud2,aud3,aud4 in lector:
            momento=time(int(hora), int(minuto))
            total=float(aud1)+float(aud2)+float(aud3)+float(aud4)
            audiencias=(float(aud1),float(aud2),float(aud3),float(aud4),total)
            medicion=Registro(momento,cadenaTV,audiencias)
            list_registro.append(medicion)
    return list_registro

def totalAudienciaCadena(list_registros, cadenaTV):
    return sum([r.audiencias[4] for r in list_registros if r.cadenaTV == cadenaTV])

def conjuntoCadenasTV(list_registro):
    return {r.cadenaTV for r in list_registro}

def getDiccAudienciasXCadena(list_registro):
    return {clave: totalAudienciaCadena(list_registro, clave) for clave in conjuntoCadenasTV(list_registro)}

def totalAudienciaSegmentoCadena(list_registro,cadenaTV,segmento):
    p=Segmentos.index(segmento)
    return sum([r.audiencias[p] for r in list_registro if r.cadenaTV==cadenaTV])

def cadenaMaxAudiencia(list_registro):
    dicc=getDiccAudienciasXCadena(list_registro)
    tuplaCadenaudiencia=max(dicc.items(), key=lambda t:t[1])
    return tuplaCadenaudiencia[0]

def cadenaMaxAudienciaSegmento(list_registro,segmento):
    lista_aud=[]
    for cadenaTV in conjuntoCadenasTV(list_registro):
        total=totalAudienciaSegmentoCadena(list_registro, cadenaTV, segmento)
        lista_aud.append((total,cadenaTV))
    return max(lista_aud)

def main():
    list_mediciones = lee_mediciones('./data/audiencias.txt')
    #print(list_mediciones[:10])
    AudienciaA3 = totalAudienciaCadena(list_mediciones, Cadenas[2])
    print('La audiencia de Antena3 es ', AudienciaA3)
    print(getDiccAudienciasXCadena(list_mediciones))
    print(totalAudienciaSegmentoCadena(list_mediciones, Cadenas[0],'NINOS'))
    print(cadenaMaxAudiencia(list_mediciones))
    audiencia,cadena=cadenaMaxAudienciaSegmento(list_mediciones, 'NINOS')
    print('La audiencia de ', audiencia, ' tiene su max en el canal', cadena)

if __name__ == '__main__':
    main()