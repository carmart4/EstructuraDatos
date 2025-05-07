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
    '''
    Evalua si es una rama final del arbol. Es decir, 
    que no tenga más hijos.

    Args
    ---
    a = nodo de Arbol binario

    Return
    ---
    hoja = valor booleano para saber si es el ultimo nodo de una rama
    '''
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


def Afirmativa(s:str)->bool:
    '''Verifica todos los 'si' posibles enn una expresion''' 
    opciones = ["sí","si","Sí","Si","SÍ","SI"]
    return s in opciones


def Jugar(a:ArbolBinario):
    '''
    Recorre el arbol desde su raiz, devolviendo al usuario
    el valor que hay en cada nodo, para evaluar si se 
    desplaza por su rama derecha o izquierda, mientras no sea hoja (fin de la rama).

    Args
    ---
    a = arbol binario
    '''
    while not EsHoja(a):
        resp = input("Pregunta: " + a.Raiz() + " (Sí/No) ") # Input por el usuario
        
        if Afirmativa(resp):
            a = a.SubarbIzq()
        else: # lo que no sea afirmativo es negativo
            a = a.SubarbDer()
    print()
    print ("Respuesta:", a.Raiz())
    return


def MostrarFormato(a:ArbolBinario, nivel=0, nivel_max=[0], hojas=[]):
    '''
    Recorre el arbol para extraer el valor de los nodos e ir mostrando 
    el valor de sus hijos, cuando no sea una hoja.

    Args
    ---
    a = Arbol binario
    nivel = Nivel inicial del arbol.
    nivel_max = una lista con un solo valor, que será el nivel máximo encontrado en el arbol.
    hojas = lista con los valores terminales del arbol. 

    Retun
    ---
    t = El valor leido en cada nodo.
    '''
    if a.EsVacio():
        t = ''
    
    else:

        if nivel > nivel_max[0]:
            nivel_max[0] = nivel

        tabulador = '  ' * nivel
        valor = a.Raiz()
        salida = str(valor) + '\n'

        # Verificar si es hoja, si el arbol 'a' no es vacio pero sus hijos si.
        if EsHoja(a):
            hojas.append(valor)

        izq = MostrarFormato(a.SubarbIzq(), nivel + 1, nivel_max, hojas)
        salida_izq = tabulador + '[SÍ] ' + izq if izq else ''

        der = MostrarFormato(a.SubarbDer(), nivel + 1, nivel_max, hojas)
        salida_der = tabulador + '[NO] ' + der if der else ''

        t = salida + salida_izq + salida_der

    return t


def main():

    print(__doc__)

    fichero = 'arbol_personajes.dat'

    try:
        with open(fichero, 'r', encoding='utf-8') as f:
            arbol = GenerarArbol(f)

    except:
        print('Error abriendo fichero.')

    else:
        # Ejercicio 1.
        print('Recorrido del arbol en prefijo: \n')
        recorrer_prefijo(arbol)
        print('-----')

        # Ejercicio 2.
        print('\nJuego para una sola persona: ')
        Jugar(arbol)
        print()
        print('-----')
        
        # Ejercicio 3.
        n = [0] # Debe ser en un dato mutable para saber la profundidad, niveles
        h = [] # Lista que contendra los valores de las hojas

        formato= MostrarFormato(arbol, nivel_max=n, hojas=h)
        print('Formato: ')
        print(formato)
        print('Niveles: ', n[0])
        print('Nodos: ', len(h))

if __name__ == '__main__':
    main()