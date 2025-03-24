# -*- coding: utf-8 -*-
"""Módulo auxiliar para Práctica 2 (2025).
Algoritmos de Ordenación de listas.

Versión inicial no particularizada a ningún problema concreto.
Deberás realizar los cambios indicados en el guion de prácticas
y modificar este comentario.

@date: 17/02/2025
"""
from pr2_persona import PersonaVacunada
from pr2_fecha import Fecha

def OrdSeleccion (v:list)->int:
    """
    Algoritmo de ordenación por Selección
    Parameters
    ----------
    v : list
        lista con los datos.
    Returns
    -------
    int = pasos realizados
    """
    pasos = 0 #Contador de pasos    
    n = len(v)
    for i in range(n-1): #para todas las posiciones
        pos_min = i #primer minimo
        for j in range(i+1,n):
            pasos += 1
            if v[j].GetFecha_1() < v[pos_min].GetFecha_1():                         # Fila modificada para comparar fecha. 
                pos_min = j #nuevo minimo
        v[i],v[pos_min] = v[pos_min],v[i]
        pasos += 1
    return pasos

def OrdQuicksort (v:list)->int:
    """
    Algoritmo de ordenación Quicksort
    Parameters
    ----------
    v : list
        lista con los datos.
    Returns
    -------
    int = pasos realizados
    """
    #realizar la particion del toda la lista
    return Particion(v, 0, len(v)-1)    

def Particion (v:list, izq:int, der:int)->int: 
    """
    Función de partición del algoritmo Quicksort
    Parameters
    ----------
    v : list
        lista con los datos.
    izq : int
        limite inferior de la zona de partición.
    der : int
        limite superior de la zona de partición.
    Returns
    -------
    int = pasos realizados
    """
    pasos = 0 #Contador de pasos    
    piv = v[ (izq + der)//2 ].GetFecha_1()                                          # Fila modificada
    i = izq
    j = der
	#Contabilizar todos los pasos dentro de este bucle
    #incluida la condicion i<=j cuando es True
    while i <= j:
        while v[i].GetFecha_1() < piv: #parar si mal ubicado a la izquierda         # Fila modificada
            pasos += 1
            i += 1
        while v[j].GetFecha_1() > piv: #parar si mal ubicado a la derecha           # Fila modificada
            pasos += 1
            j -= 1
        if i < j: #intercambiar mal ubicados
            v[i],v[j] = v[j],v[i]
            pasos += 1
            i += 1
            j -= 1
        elif i == j: #forzar finalizar particion
            i += 1
            j -= 1
    #a partir de aqui no contabilizar pasos
    
    if izq < j: #continuar con particion izquierda
        pasos += Particion(v,izq,j)
    if i < der: #continuar con particion derecha
        pasos += Particion(v,i,der)
    return pasos
