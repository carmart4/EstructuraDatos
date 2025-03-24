# -*- coding: utf-8 -*-
"""Práctica 1 (2025). Version 0
Definición y manejo básico de un registro de Personas Vacunadas

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
    
def LeerFichero(nom: str) -> (bool, list):
    """ 
    Leer archivo de personas vacunadas.
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

def LeerFicheroPersonas(nom: str) -> (bool, list):
    """ Leer archivo de personas vacunadas.
        Args:
            nom = Nombre del archivo
        Return:
            abierto para lectura correctamente = True/False
            lista de personas leidas, vacía si no abierto
    """
    abierto = bool()
    lista_ids = []
    try:
        f = open(nom)
    except:
        abierto = False
    else:
        abierto = True

        #Leer las restantes lineas y convertirlas en personas vacunadas
        for linea in f:
            linea = linea.strip()
            lista_ids.append(linea)
        f.close()
    return abierto,lista_ids


def main():

    F_VACUNAS = 'vacunaciones_big.csv'
    F_VERIFICAR = "verificarL3.dat"

    try: 
        
        ok_vac, lista = LeerFichero(F_VACUNAS)
        ok_ids, lista_ids = LeerFicheroPersonas(F_VERIFICAR)

    except:
        print('Error abriendo fichero.')

    else:

        if ok_vac and ok_ids:

            lista_tallas = [100, 500, 1000, 2000, 5000]

            for n in lista_tallas:
                lista_recortada = lista[:n]

                cont_sec = 0
                cont_sec_p = 0
                cont_sec_c = 0
                cont_bin = 0
                cont_p_vacunadas = 0
                cont_pfizer = 0
                cont_moderna = 0
                cont_astra_zeneca = 0

                for id in lista_ids:
                    posicion, pasos_secuencial = BusquedaSecuencial(lista_recortada, id)
                    cont_sec += pasos_secuencial
                    posicion, pasos_secuencial_p = BusquedaSecuencialParada(lista_recortada, id)
                    cont_sec_p += pasos_secuencial_p
                    posicion, pasos_secuencial_c = BusquedaSecuencialCentinela(lista_recortada, id)
                    cont_sec_c += pasos_secuencial_c
                    posicion, pasos_binaria = BusquedaBinaria(lista_recortada, id)
                    cont_bin += pasos_binaria
                    if posicion > -1: # Si la posicion es mayor a -1, quiere decir que si está, y por lo tanto es una persona vacunada.
                        cont_p_vacunadas += 1
                        persona_vacunada = lista_recortada[posicion]
                        if persona_vacunada.vacuna == 'Pfizer':
                            cont_pfizer += 1
                        elif persona_vacunada.vacuna == 'Moderna':
                            cont_moderna += 1
                        else:
                            cont_astra_zeneca += 1

                print()
                print('Talla: ', n)
                
                #Las personas buscadas es la longitud de la lista_ids.
                personas_buscadas = len(lista_ids)
                cont_no_vacunadas = personas_buscadas - cont_p_vacunadas

                # Hacemos las operaciones
                prom_sec = cont_sec/personas_buscadas
                prom_sec_p = cont_sec_p/personas_buscadas
                prom_sec_c = cont_sec_c/personas_buscadas
                prom_bin = cont_bin/personas_buscadas
                
                print()
                print('Pacientes buscados: ', personas_buscadas)
                print('Vacunados: ', cont_p_vacunadas)
                print('         Pfizer: ', cont_pfizer)
                print('         Moderna: ', cont_moderna)
                print('         AztraZeneca: ', cont_astra_zeneca)
                print('No vacunados: ', cont_no_vacunadas)
                print()
                print('Promedio B. Secuencial: ', round(prom_sec, 2))
                print('Promedio B. Secuencial Parada: ', round(prom_sec_p, 2))
                print('Promedio B. Secuencial Centinela: ', round(prom_sec_c, 2))
                print('Promedio B. Secuencial Binaria: ', round(prom_bin, 2))

if __name__ == '__main__':
    main()