'''
Previo laboratorio 6

En esta práctica se aplicará la estructura diccionario para almacenar 
información estadística sobre los jugadores de baloncesto de la NBA.

Autor: Carlos Martinez 
Fecha: 07/05/2025
'''
# Importamos la clase que vamos a utilizar
from pr6_jugador import *

def LecturaFichero(n:str) -> (bool, list):
    '''
    Función auxiliar que recibe el nombre del fichero
    y devulve una lista con su contenido 

    Args:
    ---
        n = nombre del fichero, sin la ubicacion

    Returns:
    ---
        abierto = valor booleano, abierto o no
        info = lista que contiene las lineas leidas
    '''
    abierto = False
    fichero = 'datos/' + n

    try:
        f = open(fichero, mode= 'r', encoding= 'UTF-8')

    except:
        abierto = False

    else:
        abierto = True
        info = list()
        linea = f.readline()
        while linea != '':
            linea = linea.rstrip() # Eliminar caracteres -Espacios, tabuladores, saltos de linea-.
            info.append(linea)
            linea = f.readline()
        
        f.close()

    return abierto, info


def DicCabecera(l:str) -> dict:
    '''
    Funcion auxiliar, que recibe la cabecera de un fichero (primer linea)
    y la convierte en un diccionario.

    Args:
    ---
        l = primer linea del fichero

    Return:
    ---
        d = diccionario de los campos referidos a indicadores del jugador (menos nombre y equipo)
    '''
    d = {}

    claves = l.split(';')
    claves = claves[2:] # Evitamos el nombre y el equipo

    for clave in claves:
        d[clave] = claves.index(clave)

    return d


def DicJugador(lineas:list) -> dict:
    '''
    Función auxiliar, que recibe una lista con todas las lineas leidas 
    del fichero, y devolvera un dictionario que asociará el nombre de un jugador (clave) 
    con un objeto de tipo JugadorNBA (valor), que contendrá toda su información.

    Args:
    ---
        lineas = lista con todas las lineas, menos la cabecera 

    Return:
    ---
        d = diccionario con información de cada jugador 
    '''
    d = {}

    for linea in lineas:
        
        # Creamos el objeto para cada linea(jugador)
        j = JugadorNBA()

        # Usamos set linea, que procesa el str, para asignar nombre, equipo y stats
        j.SetLinea(linea)

        # Obtenemos el nombre del jugador -> objeto creado antes
        n = j.GetNombre() 

        # Añadimos al diccionario, con el nombre como clave, el objeto creado
        d[n] = j

    return d

def DicEquipos(djug: dict) -> dict:
    '''
    Función auxiliar, que recibe el dictionario que contiene 
    toda la informacion de los jugadores, con el nombre del jugador 
    como clave, para saber cuales pertenecen a determinado equipo.

    Args:
    ---
        djug = diccionario con informacion de los jugadores

    Return:
    ---
        d = diccionario con la cantidad de jugadores por equipo 
    '''
    d = {}
    # Como queremos contar cuantos jugadores hay por cada equipo

    # Equipos a los que se puede pertenece
    eq = [e for e in EQUIPOS.keys()] # Lista de equipos

    # Jugadores en cada equipo
    c = [0 for e in eq] # Habrán tantos ceros como equipos hayan, de inicio
    
    # Obtener la clave de cada objeto(jugador) para saber su equipo
    j = [clave for clave in djug] # Lista de jugadores 

    for jugador in j:
        # Obtenemos el equipo al que pertenece el jugador 
        pertenece = djug[jugador].GetEquipo()
        pos = eq.index(pertenece) # Identificamos la posicion del equipo en la lista 
        c[pos] += 1
    
    for indice in range(len(eq)):
        d[eq[indice]] = c[indice]

    return d


def main():

    print(__doc__)

    NOMBREFICHERO = 'nba_18_19.csv'

    # TAREA 1

    # Hacemos la lectura del fichero
    abierto, informacion = LecturaFichero(NOMBREFICHERO)

    if not abierto:
        print('Error abriendo fichero.')

    else:

        # TAREA 1

        # Diccionario 1 - Jugadores
        # Las claves están en la primer fila de cada archivo
        cabecera = informacion[0]
        
        dic_cab = DicCabecera(cabecera)

        print('Diccionario de campos:')
        print(dic_cab)

        # Diccionario 2 - Informacion
        info = informacion[1:] # Todas las lineas, despues de la cabecera

        # Ahora leemos la información de cada jugador
        dic_jug = DicJugador(info)

        print()
        print('Archivo leido: ', NOMBREFICHERO)
        print('Numero de jugadores: ', len(dic_jug))

        print('\nEjemplo de salida:')
        print(dic_jug['James Harden'])
        print()

        # TAREA 2

        # Diccionario 3 - Jugadores por equipo
        dic_eq = DicEquipos(dic_jug)

        print('Diccionario de cantidad de jugadores por equipo: ')
        print(dic_eq)
        print()

if __name__ == '__main__':
    main()