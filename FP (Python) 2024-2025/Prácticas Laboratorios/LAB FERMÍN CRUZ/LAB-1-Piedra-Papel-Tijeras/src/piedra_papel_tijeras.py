import random

def ordenador_decide_jugada():
    ''' 
    Elige aleatoriamente entre piedra, papel o tijeras y devuelve la elección.     
    '''
    opciones = ["piedra", "papel", "tijeras"]
    res = random.choice(opciones)
    return res

def usuario_decide_jugada():
    ''' 
    Pide al usuario que elija entre piedra, papel o tijeras y devuelve la elección.     
    '''
    eleccion_usuario = input("Elige piedra, papel o tijeras: ")    
    return eleccion_usuario

def determina_ganador(jugada_usuario, jugada_ordenador):
    if jugada_usuario == jugada_ordenador:
        return "Empate"
    elif jugada_usuario == "piedra" and jugada_ordenador == "tijeras":
        return "Ganaste"
    elif jugada_usuario == "tijeras" and jugada_ordenador == "papel":
        return "Ganaste"
    elif  jugada_usuario == "papel" and jugada_ordenador == "piedra":
        return "Ganaste"
    else:
        return "Perdiste"
    
def jugar():
    #Muestra un mensaje de bienvenida:
    print('Bienvenido al juego de piedras, papel o tijeras.')

    #Haz que el ordenador decida su jugada:
    jugada_ordenador = ordenador_decide_jugada()

    #Haz que el jugador decida su jugada:
    jugada_usuario = usuario_decide_jugada()

    #Muestra un mensaje indicando la elección del ordenador:
    print('El ordenador eligió: ', jugada_ordenador)

    #Muestra un mensaje indicando la elección del ordenador:
    print('El usuario eligió: ', jugada_usuario)

    #Determine quién es el ganador:
    ganador_de_la_ronda = determina_ganador(jugada_usuario, jugada_ordenador)
    print('El resultado es:', ganador_de_la_ronda)
    return ganador_de_la_ronda

if __name__ == "__main__":
    jugar()

