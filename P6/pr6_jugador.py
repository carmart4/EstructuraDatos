# -*- coding: utf-8 -*-
"""
Módulo auxiliar para Práctica 6 (2025).
Definición de un registro de Jugador NBA.

Clase JugadorNBA

Este archivo no requiere ninguna modificación.


@date: 30/04/2025
"""

EQUIPOS = {"ATL":"Atlanta Hawks","BOS":"Boston Celtics","BKN":"Brooklyn Nets",\
           "CHA":"Charlotte Hornets","CHI":"Chicago Bulls","CLE":"Cleveland Cavaliers",\
           "DAL":"Dallas Mavericks","DEN":"Denver Nuggets","DET":"Detroit Pistons",\
           "GSW":"Golden State Warriors","HOU":"Houston Rockets","IND":"Indiana Pacers",\
           "LAC":"LA Clippers","LAL":"Los Angeles Lakers","MEM":"Memphis Grizzlies",\
           "MIA":"Miami Heat","MIL":"Milwaukee Bucks","MIN":"Minnesota Timberwolves",\
           "NOP":"New Orleans Pelicans","NYK":"New York Knicks","OKC":"Oklahoma City Thunder",\
           "ORL":"Orlando Magic","PHI":"Philadelphia 76ers","PHX":"Phoenix Suns",\
           "POR":"Portland Trail Blazers","SAC":"Sacramento Kings","SAS":"San Antonio Spurs",\
           "TOR":"Toronto Raptors","UTA":"Utah Jazz","WAS":"Washington Wizards"}


class JugadorNBA:
    """
    Especificación del tipo JugadorNBA
    Resumen de operaciones públicas:
        - Constructor
        - SetDatos(self, n:str, e:str, s:list): Asignar todos los datos
        - SetLinea(self,s:str): Poner datos a partir de una linea de texto csv
        - GetNombre(self)->str: Consultar el nombre
        - GetEquipo(self)->str: Consultar el equipo
        - GetEstadisticas(self)->list: Consultar las estadíticas
        - str(): Convertir en string del jugador		
    """
    def __init__(self):
        """
        Constructor de la clase

        Returns
        -------
        None.

        """
        self.__nombre = "<Sin nombre>" #Nombre del jugador
        self.__equipo = "NoT" #Equipo (abreviatura de 3 caracteres)
        self.__stats = list() #lista de estadísticas
        return

    def SetDatos(self, n:str, e:str, s:list):
        """
        Asignar los datos del Jugador (self)

        Parameters
        ----------
        n : str
            Nombre del jugador.
        e : str
            Equipo al que pertenece.
        s : list
            Lista con los datos estadísticos.

        Returns
        -------
        None.
        """
        if e in EQUIPOS:
            self.__nombre = n
            self.__equipo = e
            self.__stats = s
        return
    
    def SetLinea(self,s:str):
        """
        Establecer datos del jugador (self) a partir de una linea de texto csv

        Parameters
        ----------
            s = texto csv a procesar
            
        Returns
        -------
        None.
        """       
        s = s.rstrip("\n") #elimina \n si lo tuviera
        l = list()
        l = s.split(";")
        #nombre, equipo y lista de estadísticas
        self.SetDatos(l[0], l[1], l[2:])
        return        
    
    def GetNombre(self)->str:
        """
        Consultar el nombre del jugador

        Returns
        -------
        str
            nombre
        """
        return self.__nombre
    
    def GetEquipo(self)->str:
        """
        Consultar el equipo del jugador

        Returns
        -------
        str
            equipo
        """
        return self.__equipo
    
    def GetEstadisticas(self)->list:
        """
        Consultar los datos estadísticos del jugador

        Returns
        -------
        int
            puntos
        """
        return self.__stats
    
    def __str__(self)->str:
        """
        Convertir en string la informacion del jugador
        Returns
        -------
        str
            string con la informacion del jugador
        """
        s = self.__nombre + " (" + self.__equipo + ") "
        s += str(self.__stats) + "\n"
        return s
