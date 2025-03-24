'''
Desarrollo de previo laboratorio.

Este programa, llamado “pr3_v1.py” debe importar la clase Atleta creada previamente y 
leer los datos del archivo “atletas_small.csv”, guardarlos en una lista solo aquellos 
atletas cuya información sea correcta, de acuerdo con los requisitos de validación indicados, 
y mostrar el número de atletas almacenados y la información de cada uno de ellos.

Autor: Carlos Martinez
Fecha: 10/03/2025

'''
from atleta_carlos import *


def LeerFichero(nom: str)->(bool, list):
    '''
    Leer archivo de Atletas.
    Args:
        nom = Nombre del archivo
    Return:
        abierto para lectura correctamente = True/False
        lista de personas leidas, vacía si no abierto
    '''
    abierto = False
    lista = []
    try:
        f = open(nom)
    except:
        abierto = False
    else:
        abierto = True
        # Leer cabecera y no hacer nada con ella.
        f.readline()
        # Leer las restantes lineas y convertirlas en personas vacunadas.
        for linea in f:
            lista.append(linea)
        f.close()
    return abierto, lista


def ConvertirStr (l:list) -> list: 
    '''
    Recibe una lista con cadenas de texto del archivo de Atletas y
    devuelve una lista con objetos Atleta, más el total de Atletas registrados correctamente. 
    Arg: 
        l = lista de personas con atributos separados por ;

    return:
        la = lista con objetos Atleta 
        total = total de Atletas leidos correctamente
    '''
    la = list()
    total = 0
    
    for linea in l:
        linea = linea.rstrip("\n") # Elimina el salto de linea si lo tuviera.
        at = list()
        at = linea.split(';') # Separa los valores de cada linea por ';' y los guarda en una lista con 4 elementos. 
        if len(at) >= 4:
            a = Atleta()
            if a.SetValores(at[0], at[1], at[2], at[3]):
                la.append(a)
                total += 1
    return la, total


def main():

    fname = 'atletas_small.csv'
    abierto, datos = LeerFichero(fname)

    #fname = 'atletas_big.csv'
    #abierto, datos = LeerFichero(fname)

    if abierto:
        
        print('Fichero abierto. \n')
        listaAtletas, total = ConvertirStr(datos)   

        print('Número de atletas correctamente leídos = ', total)    
        print()

        # i ya es un objeto Atleta
        print('Datos de los atletas: ')
        for i in listaAtletas:
            print('     ', i)
        print()

    else:
        print('Error abriendo fichero.')

if __name__ == '__main__':
    main()