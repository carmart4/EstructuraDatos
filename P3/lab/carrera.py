'''
Laboratorio 3. 

Programa que permite registrar a los atletas participantes 
en una carrera dentro de una competición de atletismo.

Autor: Carlos Martinez
Fecha: 21/03/2025

'''
# Importamos librerias o clases necesarias.
from atleta import *

class Carrera:
    '''
    Especificacion de la clase Carrera:
    --- 
    • Nombre: Nombre oficial de la carrera.
    • Especialidad: Especialidad de la carrera.
    • Participantes: Conjunto de atletas participantes en la carrera.
    '''
    # Definimos constantes.

    # Constructor de la clase. 
    def __init__(self):
        ''' 
        Construye un nuevo objeto con valores por defecto para sus atributos. 
        Alfanuméricos tendrán el valor '<Sin asignar>' y numéricos 0. 
        ---
        Argumentos:
            nombre = nombre de la carrera 
            especialidad = especialidad de la carrera
        '''
        self.__nombre = str('<Sin asignar>')
        self.__especialidad = str('<Sin asignar>')
        self.__participantes = list()
        return
    
    def __ValidarEspecialidad(e:str) -> bool:
        '''
        Valida que la especialidad a modificar sea correcta. 
        Arg: 
            e = especialidad que ingresa el usuario 
        return: 
            valido = indica si la especialidad ingresada es correcta o no
        '''
        valido = False
        if e in Atleta.ESPEC:
            valido = True
        return valido 
    
    def SetNombre(self, n:str):
        ''' 
        Permite modificar exclusivamente el nombre de la carrera. 
        ---
        Argumento:
            n = nombre de la carrera
        '''
        self.__nombre = n
        return
    
    def SetEspecialidad(self, e:str) -> bool:
        ''' 
        Permite modificar exclusivamente la especialidad de la carrera. 
        ---
        Arg:
            e: dato de la especialidad que ingresa el usuario.
        return:
            valido: valor booleano que indica si el dato ingresado es correcto o no.
        '''
        valido = False
        if Carrera.__ValidarEspecialidad(e):
            valido = True
            self.__especialidad = e
        return valido
        
    def Inscribir(self, a:Atleta) -> bool:
        '''
        Permite registrar un atleta participante en la carrera.
        De ser valida la especialidad, el atleta es añadido a la lista de participantes. 
        ---
        Argumento:
            a = objeto de tipo Atleta
        Return:
            valido = valor bool para saber si se inscribió o no el atleta
        '''
        valido = False
        if a.GetEspecialidad() == self.__especialidad:
            valido = True
            self.__participantes.append(a)
        return valido

    def GetNombre(self) -> str: 
        ''' 
        Permite conocer el nombre del atleta. 
        ---
        '''
        return self.__nombre
    
    def GetEspecialidad(self) -> str: 
        '''
        Permite conocer la especialidad del atleta. 
        ---
        '''
        return self.__especialidad
    
    def GetParticipantes(self):
        '''
        Permite conocer el conjunto de atletas participantes de la carrera.
        ---
        '''
        return self.__participantes