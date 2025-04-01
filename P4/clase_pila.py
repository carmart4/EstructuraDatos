# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 17:06:25 2015

Clase Pila/Stack

"""

class Pila:
    def __init__(self):
        self.__elementos = []
    
    def Apilar(self,x):
        """ Apilar x en la pila """
        self.__elementos.append(x)
        
    def Desapilar(self):
        """ Eliminar un elemento de la pila """
        if self.EsVacia(): # no se puede eliminar
            raise RuntimeError("Desapilar: Intento de eliminar en pila vacía.")
        self.__elementos.pop()
    
    def Cima(self):
        """ Consultar el elemento en la cima de la pila """
        if self.EsVacia(): # no se puede consultar la cima
            raise RuntimeError("Cima: Intento de consultar en pila vacía.")
        ultimo = len(self.__elementos)-1
        return self.__elementos[ultimo]
    
    def EsVacia(self)->bool:
        """ Determinar si la pila está vacía """
        return len(self.__elementos) == 0
    
    def __str__ (self)->str:
        """ Generar string con el contenido de la pila """
        if self.EsVacia():
            s = "Pila Vacia"
        else:
            i = len(self.__elementos)-1
            s = ""
            while i > 0:
                s += str(self.__elementos[i]) + ";"
                i -= 1
            s += str(self.__elementos[0])
        return s
