# -*- coding: utf-8 -*-
"""
Pr.4: Ejemplo de uso de Pilas:
Analizar la concordancia de paréntesis.

@date: 26/03/2025
"""
from clase_pila import Pila
        
def AnalizarParentesis (e:str)->list:
    """
    Funcion que analiza la concordancia de paréntesis en una cadena

    Parameters
    ----------
    e : str
        Expresion con parentesis.

    Returns
    -------
    list
        Lista de errores.

    """
    p = Pila()
    lista_errores = []
    for i in range(len(e)):
        if e[i] == "(":
            p.Apilar(i)
        else:
            if e[i] == ")":
                try:
                    p.Desapilar()
                except:
                    lista_errores.append("')' no abierto en "+str(i))
    if not p.EsVacia():
        while not p.EsVacia():
            lista_errores.append("'(' no cerrado en "+str(p.Cima()))
            p.Desapilar()
    return lista_errores
