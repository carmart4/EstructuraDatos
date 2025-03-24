# -*- coding: utf-8 -*-
"""
Practica de laboratorio 2.

Definición y manejo básico de un registro de Personas Vacunadas.

"""
from pr1_persona import *
from pr1_algoritmos import *

def ConvertirLinea(s:str) -> PersonaVacunada:
    """
    Convertir una linea de texto csv en un registro Persona
    Args:
        s = linea a procesar
    Return:
        PersonaVacunada con los datos contenidos en s.
    """
    s = s.rstrip("\n") #elimina \n si lo tuviera
    l = list()
    l = s.split(";")
    p = PersonaVacunada()
    if len(l) >= 6: #para evitar errores de formato
        p.id = l[0] #Codigo de identificacion
        p.nombre = l[1] #Nombre de la persona
        p.vacuna = l[2] #Vacuna suministrada
        p.fecha1 = l[3] #Fecha dosis 1
        p.fecha2 = l[4] #Fecha dosis 2
        p.fecha3 = l[5] #Fecha dosis 3
    return p
    
def LeerFichero(nom: str)->(bool, list):
    """ 
    Leer archivo de personas vacunadas.
    Args:
        nom = Nombre del archivo
    Return:
        abierto para lectura correctamente = True/False
        lista de personas leidas, vacía si no abierto
    """
    abierto = bool()
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
            p = ConvertirLinea(linea)
            lista.append(p)
        f.close()
    return abierto, lista

def BuscarPersonas (buscar: list, # Valores a buscar
               datos: list): # Lista de personas vacunadas 
    '''
    Ejecuta cada una de las busquedas del fichero pr1_algoritmos y muestra los resultados en pantalla. 
    Args:
        buscar = Elementos a buscar
        datos = lista de PersonaVacunada
    '''
    # Lista de funciones de búsqueda del fichero pr1_algoritmos, que fueron modificados previamente. 
    funciones_b = [
        ("Busqueda Secuencial", BusquedaSecuencial),
        ("Busqueda Secuencial Parada", BusquedaSecuencialParada),
        ("Busqueda Secuencial Centinela", BusquedaSecuencialCentinela),
        ("Busqueda Binaria", BusquedaBinaria),
    ]

    for nombre_b, funcion_b in funciones_b:
        print(nombre_b, ': \n')

        for id in buscar:
            # Muestra por pantalla el identificador a buscar, pasado en la lista buscar. 
            print('Identificador buscado: ', id)

            # Llamamos a cada funcion, de manera que devuelve:
                #encontrado -> bool para saber si está o no. 
                #pasos -> int con la cantidad de pasos llevados a cabo por la funcion. 
                #posicion -> int que por defecto es -1. Es decir, si no está, devuelve -1. 
            encontrado, pasos, posicion = funcion_b(datos, id)

            if encontrado:
                print('Encontrado.')
            else:
                print('No encontrado.')
            print('Posicion: ', posicion)
            print('Total pasos: ', pasos)
            print('\n')
    return

def main():
    """ Tarea 1: Implementar esta función principal para que:
    1) Se lean datos de personas desde una archivo csv,
    2) se almacenen en una lista y
    3) se muestren por pantalla
    """    
    fichero = "vacunaciones_small.csv"

    try: 
        # Abierto para lectura y datos que contiene los datos en una lista. 
        abierto, datos = LeerFichero(fichero)

    except:
        print('Error abriendo fichero.')

    else:

        # Comprobamos que el archivo esté para lectura. 
        if abierto:

            # Leemos los datos. 
            #for persona in datos:
            #    MostrarPersona(persona)

            # Definimos los ids que queremos buscar.
            buscar_id = ['0002JTX', '1111VAC', '0006HYR', '1543GYM', '0014FGV']

            # Llamamos a la funcion que nos imprime los valores por pantalla. 
            BuscarPersonas(buscar_id, datos)

        else:
            print('No se ha podido leer el fichero.')

if __name__ == '__main__':
    main()