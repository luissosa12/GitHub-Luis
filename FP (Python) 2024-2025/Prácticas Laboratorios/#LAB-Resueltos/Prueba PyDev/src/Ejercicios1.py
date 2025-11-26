'''
Created on 28 sept. 2018

@author: Juanmi

Definicion de variables y tipo
'''
import math

def leerEntero():
    x=input('Deme un entero: ')
    return int(x)

def leerCadena():
    x=input('Deme una cadena: ')
    return x

def leerEntero2(mensaje):
    x=input(mensaje)
    return int(x)

'''
a=leerEntero2('Dame un entero: ')
b=leerEntero2('Dame otro entero: ')

print(a+b)
'''

def suma(x,y):
    return x+y

def producto(x,y):
    return x*y
'''
a=leerEntero()
b=leerEntero()

print('La suma de dos enteros es: ',suma(a, b),' y el producto es: ', producto(a, b))
print(suma('Queso', 'Eso'))
'''

def areaCirculo(radio):
    return math.pi*radio**2

def areaLongitudCirculo(radio):
    '''
    return (areaCirculo(radio), math.pi*2*radio)
    '''
    area=areaCirculo(radio)
    longitud=math.pi*2*radio
    return (area,longitud)

#print('El area es: ',areaLongitudCirculo(4.5)[0],'y la longitud es: ',areaLongitudCirculo(4.5)[1])
'''
Operadores
'''
def esPar(num):
    return num%2==0

def esMultiplo(m,n=2):
    return m%n==0

def estaIntervaloCerrado(x,a,b):
    return x>=a and x<=b

def estaIntervaloAbierto(x,a,b):
    return x>a and x<b

def estaFueraIntervaloCerrado(x,a,b):
    #return not estaFueraIntervaloCerrado(x, a, b)
    return x<a or x>b

'''
Estructura If
'''
def signoQuinela(gl,gv):
    if gl>gv:
        res='1'
    elif gl<gv:
        res='2'
    else:
        res='x'
    return res

def Minimo(a,b,c):
    if a>b:
        if b>c:
            menor=c
        else:
            menor=b
    else:
        if a<c:
            menor=a
        else:
            menor=c
    return menor 

'''
Estructuras While y For
'''
def muestra1(n):
    for i in range(n):
        print(i+1)

def muestra2(n):
    for i in range(n):
        print(i)

def sumaPrimeros(n):
    suma = 0
    for i in range(n+1):
        #suma = suma + i
        suma +=i
    return suma

def sumaPrimeros2(n):
    suma = 0
    i=1
    while i<=n:
        suma = suma + i
        i += 1
    return suma

def muestraentreDos(n,m):
    for i in range(n,m):
        print(i)

def Calcularfactor(n):
    mult=1
    while n >= 1:
        mult = mult * n
        n -= 1
    return mult

def ElevadoA(x,n):
    mult=1
    while n > 0:
        mult = mult * x
        n -= 1
    return mult

'''
Lista
'''
valores=[3,4,5,8,3,7,4,8,10]

texto=['implementa','una','funcion','que','escriba','en',
       'la','consola','los','numeros','primos','entre','dos','dados']

#len(valores)
#valores.sort()
#valoresOrd=sorted(valores)
#texto.reverse()

def creaLista(n):
    '''
    return [i for i range(1,n+1)]
    '''
    lista=list()
    #lista=[]
    for i in range(n):
        lista.append(i+1)
    return lista

def creaListaPar(n):
    '''
    return [i for i range(1,n+1) if i%2==0]
    '''
    #lista=list()
    lista=[]
    for i in range(1,n+1):
        if i%2==0:
            lista.append(i)
    return lista

def sumaLista(lista):
    suma=0
    for i in lista:
        suma += i
    return suma
#sum(valores)        sumaLista()=sum()
def MinimoLista(lista):
    minimo=lista[0]
    for i in lista:
        if minimo > i:
            minimo=i
    return minimo
def MaximoLista(lista):
    maximo=lista[0]
    for i in lista:
        if maximo < i:
            maximo=i
    return maximo
#min(), max()        MinimoLista()=min()    MaximoLista()=max()

def minimoListaPares(lista):
    listaPares=[i for i in lista if esMultiplo(i)]
    return min(listaPares)
    #return min([i for i in lista if esMultiplo(i)])

def minimoListaCondicion(lista,condicion):
    return min([i for i in lista if condicion(i)])

def existeValorLista(lista, valor):
    for i in lista:
        if i==valor:
            return True
            break
    return False

def todosValoresListaPares(lista):
    for i in lista:
        if i%2!=0:
            return 'Existen uno o varios valores impares'
    return 'Todos los valores son pares'

valores2=[2,4,6,8,88,84,24]
#print(todosValoresListaPares(valores2))

'''07/11/2018'''
#Dada una lista devuelve el minimo y ls posicion que ocupa.
def minimo_y_posicion(lista):
    minimo=lista[0]
    pos=0
    for i,x in enumerate(lista):
        if minimo>x:
            minimo=x
            pos=i
    return (minimo,pos)

def posicionesPalabrasTerminan(listapal, caracter):
    listapos=list()
    for i,palabra in enumerate(listapal):
        if palabra[-1]==caracter:
            listapos.append(i)
    return listapos

def organizar_lista_por_modulo(lista, n):
    dicc=dict()
    for i in range(n):
        #dicc[i] debe ser la lista de valores con los numeros de lista que sean modulo i
        for valor in lista:
            if valor%n==i:
                dicc[i].append(valor) 
    return dicc
    pass

(m,p)=minimo_y_posicion([2,4,6,7,8,0,1,3,4,7])
print('el minimo es', m , 'y su posicion es', p)
print(posicionesPalabrasTerminan(['hello','casa','perro','podrido'], 'o'))