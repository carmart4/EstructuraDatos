'''
Previo laboratorio 5

Implementacion de un arbol binario para la simulación del 
juego de mesa '¿Quien es quien?'

Autor: Carlos Martinez
Fecha: 8/4/2025
'''

from clase_arbol import *

def GenerarArbol(f) -> ArbolBinario:
    '''
    Funcion que permite crear un arbol binario con el formato que 
    se describe en un fichero.

    Args
    ---
    f = fichero ya abierto para lectura.

    Return
    ---
    a = arbol binario con el contenido del fichero.
    
    '''
    txt = f.readline().rstrip('\n')

    if txt == ".":
        a = ArbolBinario()
    else:
        i = GenerarArbol(f)
        d = GenerarArbol(f)
        a = ArbolBinario(info= txt, subizq= i, subder= d)
    return a

def EsHoja(a:ArbolBinario)->bool:
    if a.SubarbIzq().EsVacio() and a.SubarbDer().EsVacio():
        hoja = True
    else:
        hoja = False
    return hoja

def recorrer_prefijo(a:ArbolBinario):
    '''
    Funcion que recorre un arbol binario en orden prefijo.

    Args
    ---
    a = arbol binario

    '''
    if not a.EsVacio():
        print(a.Raiz())
        recorrer_prefijo(a.SubarbIzq())
        recorrer_prefijo(a.SubarbDer())
    return

def main():

    print(__doc__)

    fichero = 'arbol_personajes.dat'

    try:
        with open(fichero, 'r', encoding='utf-8') as f:
            arbol = GenerarArbol(f)

    except:
        print('Error abriendo fichero.')

    else:
        recorrer_prefijo(arbol)

if __name__ == '__main__':
    main()

