'''
Practica de laboratorio 2.

Algoritmos de ordenación. 

En esta práctica vamos a abordar el cálculo empírico de costes de diversos 
algoritmos de ordenación. En concreto, se pretende obtener resultados 
experimentales del coste real en pasos de la implementación en Python 
de los dos algoritmos de ordenación analizados en las clases de teoría:

1. Ordenación por selección.
2. Quicksort.

Autor: Carlos Martinez
Fecha: 25/02/2025
'''
from pr2_persona import *
from pr2_algoritmos import *

def LeerFichero(nom: str) -> (bool, list):
    """ Leer archivo de personas vacunadas.
        Args:
            nom = Nombre del archivo
        Return:
            abierto para lectura correctamente = True/False
            lista de personas leidas, vacía si no abierto
    """
    abierto = False
    lista = []
    try:
        f = open(nom)
    except:
        abierto = False
    else:
        abierto = True
        #Leer cabecera y no hacer nada con ella
        f.readline()
        #Leer las restantes lineas y convertirlas en personas vacunadas
        for linea in f:
            lista.append(linea)
        f.close()
    return abierto, lista

def ConvertirPersonas(l: list) -> list:
    '''
    Leer la lista l que contiene las personas en formato texto csv
    y devolverlas en objeto PersonaVacunada
    Args:
        l = Contiene la lista de personas en texto csv

    Returns:
        lv = Contiene la lista de personas como objetos
    '''
    lv = list()
    for p in l:
        persona = PersonaVacunada()
        persona.SetDatos(p)
        lv.append(persona)
    return lv

def main():

    f = 'vacunaciones_small.csv'
    f2 = 'vacunaciones_big.csv'
    abierto, datos = LeerFichero(f)
    abierto2, datos2 = LeerFichero(f2)
    
    # Ejercicio 1

    if abierto:
        listaVacunados = ConvertirPersonas(datos)

        for persona in listaVacunados:
            print(persona)   

    # Ejercicio 2

        pasos = OrdSeleccion(listaVacunados)
        print('Pasos: ', pasos)

        #pasosq = OrdQuicksort(listaVacunados)
        #print('Quicksort: ', pasosq)
        
        print('Orden (solo se muestran identificadores): ')
        for i in range(len(listaVacunados)):
            print(' ', i,'.',listaVacunados[i].GetId())
        

    # Ejercicio 3

    #if abierto: 
        vacunas = ConvertirPersonas(datos)

        copia1 = vacunas.copy()
        copia2 = vacunas.copy()

        p1 = OrdSeleccion(copia1)
        p2 = OrdQuicksort(copia2)
        ratio = p1/p2
        print()
        print('Selección: ', p1)
        print('Quicksort: ', p2)
        print('Ratio: ', round(ratio, 2))
        print()
        print('Lista ordenada por fecha 1a. dosis: ')
        for persona in copia1:
            print(persona)

        if abierto2: 
            vacunas2 = ConvertirPersonas(datos2)

        copiab1 = vacunas2.copy()
        copiab2 = vacunas2.copy()

        pb1 = OrdSeleccion(copiab1)
        pb2 = OrdQuicksort(copiab2)
        ratio2 = pb1/pb2
        print()
        print('Selección: ', pb1)
        print('Quicksort: ', pb2)
        print('Ratio: ', round(ratio2, 2))
    
if __name__ == '__main__':
    main()