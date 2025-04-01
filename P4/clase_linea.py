'''
Clase Linea, que representa lineas con errores.

Esta clase se llamará Linea y un objeto de esta clase tendrá como datos 
el número de línea dentro del archivo y la lista con los errores encontrados en ella.

Autor: Carlos Martinez
Fecha: 01/04/2025
'''
from clase_cola import Cola

class Linea:
    def __init__(self):
        self.__Nlineas = int()
        self.__Lerrores = Cola()

    def AddNumeroLinea(self, n:int):
        '''Añadimos el número de linea'''
        self.__Nlineas = n

    def AddErroresLinea(self, l:list):
        '''Añadimos cada error de la linea a la cola Lerrores'''
        for e in l:
            self.__Lerrores.Encolar(e)

    def __str__(self):
        '''Sobrecargar el operador para que se pueda obtener la versión texto de estos objetos'''
        if not self.__Lerrores.EsVacia():
            s = "Línea " + str(self.__Nlineas) + "\n"
            s += str(self.__Lerrores)
        return s
