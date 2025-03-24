# -*- coding: utf-8 -*-
"""Módulo auxiliar para Práctica 1 (2025).
Algoritmos de Búsqueda sobre listas.

Versión inicial no particularizada a ningún problema concreto.
Deberás realizar los cambios indicados en el guion de prácticas
y modificar este comentario. Así confirmaré sí lees el material proporcionado.

En este caso, el hecho de que no esté el id a buscar, 
la posicion '-1' lo hará saber. 

"""

from pr1_persona import PersonaVacunada  

def BusquedaSecuencial (v:list, #Lista de PersonaVacunada
						x:str) -> (bool, int):
    """ Busqueda secuencial basica (sin parada).
        Args:
            v = lista con los datos
            x = elemento buscado
        Return:
            bool = encontrado (enc) = True/False
            int = pasos realizados
    """
    pasos = 0 #Contador de pasos
    #enc = False
    i = 0
    pos = -1                                                # Linea adicional para devolver la posicion.
    while i < len(v):
        pasos += 2 #condicion de bucle + condicion if
        if v[i].id == x:                                    # Linea modificada para comparar exclusivamente el id.
            #enc = True
            pos = i                                         # Una vez encuentra el elemento, se le asigna el valor a la posicion. 
            pasos += 1 #enc = True
        i = i + 1
        pasos += 1 #i = i+1
    return pos, pasos
	
def BusquedaSecuencialParada   (v:list, #Lista de PersonaVacunada
							    x:str) -> (bool, int):
    """ Busqueda secuencial con parada.
        Args:
            v = lista con los datos
            x = elemento buscado
        Return:
            bool = encontrado (enc) = True/False
            int = pasos realizados
    """
    pasos = 0
    i = 0
    pos = -1                                                # Linea adicional para devolver la posicion.
    while i < len(v) and v[i].id != x:                      # Linea modificada para comparar exclusivamente el id.
        i = i + 1
        pasos += 3 #2 condiciones de bucle + asignacion
    if i == len(v):
        enc = False
    else:
        pos = i                                             # Una vez encuentra el elemento, se le asigna el valor a la posicion.
        #enc = True
    return pos, pasos 
	
def BusquedaSecuencialCentinela (v:list, #Lista de PersonaVacunada
                                x:str) -> (bool, int):
    """ Busqueda secuencial con centinela.
        Args:
            v = lista con los datos
            x = elemento buscado
        Return:
            bool = encontrado (enc) = True/False
            int = pasos realizados
    """
    p = PersonaVacunada()                                   # Creamos una instancia para la clase. 
    p.id = x                                                # Convertimos el str a una instancia de la clase. 
    v.append(p)                                             # Añadimos el id al vector pero como clase, ya no como str. 
    i = 0
    pasos = 0
    pos = -1                                                # Linea adicional para devolver la posicion.
    while v[i].id != x:                                     # Linea modificada para comparar exclusivamente el id.
        i = i + 1
        pasos += 2 #condicion bucle + asignacion
    if i == len(v)-1:
        enc = False
    else:
        pos = i                                             # Una vez encuentra el elemento, se le asigna el valor a la posicion.
        #enc = True
    v.pop()
    return pos, pasos

def BusquedaBinaria (v:list, #Lista de PersonaVacunada
                    x:str) -> (bool, int):
    """ Busqueda binaria en una lista ordenada.
        Args:
            v = lista con los datos
            x = elemento buscado
        Return:
            bool = encontrado (enc) = True/False
            int = pasos realizados
    """
    izq = 0
    der = len(v) - 1
    cen = (izq + der) // 2
    pasos = 0
    pos = -1                                                # Linea adicional para devolver la posicion.
    while izq <= der and v[cen].id != x:                    # Linea modificada para comparar exclusivamente el id.
        if x < v[cen].id:                           # Aprovechando la lista ordenada de ids, comparamos las primeras 4 posiciones.  
            der = cen - 1
        else:
            izq = cen + 1
        cen = (izq + der) // 2
        pasos += 5 #3 condiciones + 2 asignaciones
    if izq > der:
        enc = False
    else:
        pos = cen                                           # Una vez encuentra el elemento, se le asigna el valor a la posicion.
        #enc = True
    return pos, pasos