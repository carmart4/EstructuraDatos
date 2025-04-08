'''
Clase línea que contendrá las posiciones en las que se encuentran los 
parentesis de una linea, el texto de la linea y una lista de tuplas
con las posiciones donde se abren y cierran los paréntesis. 

Autores: Jorge Ballesteros y Carlos Martinez
Fecha: 03-04-2025
'''

class Linea:
    def __init__(self, numlinea: int, texto: str, lista: list):
        '''
        Constructor de la clase línea que contendrá los argumentos:

        Args
        ----
        numlinea = número de la línea en el texto analizado.
        texto = texto completo de la línea (sin 'salto de linea').
        lista = lista de tuplas con las posiciones de apertura y cierre. 
        '''
        self.__numlinea = numlinea
        self.__tlinea = texto
        self.__lista_pos_parentesis = lista # Lista de tuplas (ini, fin) de cada una de las parejas correctamente formadas en la línea.


    def __str__(self)->str:
        """ Generar string con el número de la línea y la lista de los errores encontrados en ella """
        s = "Línea: " + str(self.__numlinea) + "\n"
        s += "\n".join(self.__lista_pos_parentesis) + "\n"
        return s
    
    def GetNumero(self):
        """ Consultamos el número de la línea """
        return self.__numlinea
    
    def GetTexto(self):
        """ Consultamos el contenido de la línea """
        return self.__tlinea
    
    def GetPosParentesis(self):
        """ Consultamos las posiciones de los paréntesis de apertura y de cierre de la línea """
        return self.__lista_pos_parentesis