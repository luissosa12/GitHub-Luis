'''
Created on 19 oct. 2018

@author: Juanmi
'''
import csv
from matplotlib import pyplot as plt

def lee_audiencias(nombrefich):
    listaau=[] #=list()
    with open(nombrefich,'r') as f:
        for linea in f:
            #linea tiene un str con un valor entero, una coma
            #y un valor real
            edicion, audiencia = linea.split(',')
            #edicion y audiencia son str
            edicion = int(edicion)
            audiencia= float(audiencia)
            tupla=(edicion,audiencia)
            listaau.append(tupla)
            #listaau.append((int(edicion),float(audiencia)))
    return listaau  

def lee_audiencias2(nombrefich):
    listaau=[]
    with open(nombrefich, 'r') as f:
        lector=csv.reader(f)
        for edicion, audiencia in lector:
            listaau.append((int(edicion),float(audiencia)))    
    return listaau 

def calcula_ediciones(lista):
    conjunto = set()
    for tupla in lista:
        conjunto.add(tupla[0]) #usando un conjunto eliminamos repetidos
    return list(conjunto)

def calcula_ediciones2(lista):
    conjunto = {t[0] for t in lista}
    return list(conjunto)

def calcula_ediciones3(lista):
    return list({t[0] for t in lista})
def filtra_por_edicion(lista, edicion):
    listafil=[]
    for tupla in lista:
        if (tupla[0] == edicion):
            listafil.append(tupla)
    
    return listafil

def filtra_por_edicion2(lista, edicion):
    return [t for t in lista if t[0]==edicion]

def filtra_por_ediciones(lista, lista_ediciones):
    return [t for t in lista if t[0] in lista_ediciones]

def media_lista(lista):
    listord = sorted(lista)
    tam = len(listord)
    if tam%2!=0:
        mediana=listord[tam//2]
    else:
        mediana=(listord[tam//2-1]+listord[tam//2])/2
    return mediana

def media_audiencia(lista,edicion):
    listf=filtra_por_edicion(lista, edicion)
    lista_au=[t[1] for t in listf]
    return media_lista(lista_au)

def medias_por_ediciones(lista):
    claves=calcula_ediciones(lista)
    diccionario=dict()
    for clave in claves:
        diccionario[clave]=media_audiencia(lista, clave)
    return diccionario

def medias_por_ediciones2(lista):
    dicc=dict()
    dicc_aud_por_edicion=medias_por_edicion(lista)
    for clave in dicc_aud_por_edicion.keys():
        #dicc[clave]=media_lista(dicc_aud_por_edicion[clave])
        lista_aud=dicc_aud_por_edicion[clave]
        media=media_lista(lista_aud)
        dicc[clave]=media
    return dicc

def medias_por_ediciones3(lista):
    dicc=dict()
    dicc_aud_por_edicion=medias_por_edicion(lista)
    for ed, lista_aud in dicc_aud_por_edicion.items():
        media=media_lista(lista_aud)
        dicc[ed]=media
    return dicc

def medias_por_edicion(lista):
    dicc=dict()
    #for tupla in lista:
        #tupla[0] Son las ediciones
        #tupla[1] Son las audiencias
    for ed, aud in lista:
        if ed in dicc:
            '''Si la clave ya esta debo anadir aud como
            elemento en la lista de valores correspondiente'''
            dicc[ed].append(aud)
        else:
            '''Si la edicion no esta en dicc
            deberiamos anadir el par (clave con valor ed, lista con
            un unico elemento aud
            '''
            dicc[ed]=[aud]
    return dicc

def lista_medias_shares(lista):
    lista_medias=[(e,media_audiencia(lista, e)) for e in calcula_ediciones(lista)]
    return lista_medias
    pass

def main():
    audiencias=lee_audiencias2('csv\GH.csv')
    '''print(audiencias[:20])
    ediciones=calcula_ediciones(audiencias)
    print(ediciones)
    print(filtra_por_edicion(audiencias,5))
    print(filtra_por_ediciones(audiencias, [3,4,5]))
    print(media_lista([5,34,532,7]))'''
    print(medias_por_ediciones(audiencias))
    print(medias_por_ediciones2(audiencias))
    print(medias_por_ediciones3(audiencias))
    
if __name__ == '__main__':
    main()