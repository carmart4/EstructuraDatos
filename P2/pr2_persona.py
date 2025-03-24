# -*- coding: utf-8 -*- 
"""Módulo auxiliar para Práctica 2 (2025).
Definición de un registro de Personas Vacunadas contra Covid19.

Clase PersonaVacunada

Este archivo no requiere ninguna modificación.

@date: 17/02/2025
"""

from pr2_fecha import Fecha

class PersonaVacunada:
    """
    Especificación del tipo PersonaVacunada
    Resumen de operaciones públicas:
        - Constructor
        - SetDatos(self,s:str): Poner datos a partir de una linea de texto csv
        - GetId(self)->str: Consulta el identificador de la persona
        - GetNombre(self)->str: Consulta el nombre de la persona
        - GetVacuna(self)->str: Consulta la vacuna suministrada a la persona
        - GetFecha_1(self)->Fecha: Consulta la fecha de la dosis 1
        - GetFecha_2(self)->Fecha: Consulta la fecha de la dosis 2
        - GetFecha_3(self)->Fecha: Consulta la fecha de la dosis 3
        - GetNumDosis(self)->int: Consulta el número de dosis inyectadas a la persona
        - GetFecha_Sig(self)->Fecha: Consulta la fecha de la próxima dosis       
        - str(): Transformacion en string de la Persona.		
    """
    def __init__(self):
        """
        Constructor del tipo
        Returns
        -------
        None.
        """
        self.__id = str("<No disponible>") #Identificador de la persona
        self.__nombre = str("<No disponible>") #Nombre de la persona
        self.__vacuna = str("<No disponible>") #Vacuna suministrada
        self.__fecha1 = Fecha() #Fecha dosis 1
        self.__fecha2 = Fecha() #Fecha dosis 2
        self.__fecha3 = Fecha() #Fecha dosis 3
        self.__numdosis = int() #Número de dosis recibidas
        self.__fechasig = Fecha() #Fecha prevista para la siguiente dosis
        return

    def SetDatos(self,s:str):
        """Poner datos de la PersonaVacunada a partir de una linea de texto csv
        Args:
            s = texto csv a procesar
        Returns
        -------
        None.
        """
        s = s.rstrip("\n") #elimina \n si lo tuviera
        l = list()
        l = s.split(";")
        if len(l) >= 6: #para evitar errores de formato
            self.__id = l[0] #Codigo de identificacion
            self.__nombre = l[1] #Nombre de la persona
            self.__vacuna = l[2] #Vacuna suministrada
            if l[3] != "":
                self.__fecha1 = PersonaVacunada.__Str2Fecha(l[3]) #Fecha dosis 1
            if l[4] != "":
                self.__fecha2 = PersonaVacunada.__Str2Fecha(l[4]) #Fecha dosis 2
            if l[5] != "":
                self.__fecha3 = PersonaVacunada.__Str2Fecha(l[5]) #Fecha dosis 3
            ref = Fecha()
            self.__numdosis = 0
            if self.__fecha1 != ref: #Fecha diferente del valor por defecto
                self.__numdosis = 1
                if self.__fecha2 != ref:
                    self.__numdosis = 2
                    if self.__fecha3 != ref:
                        self.__numdosis = 3
            if self.__numdosis == 1:
                self.__fechasig = self.__fecha1 + 60 #2 meses despues de la 1
            elif self.__numdosis == 2:
                self.__fechasig = self.__fecha2 + 180 #6 meses despues de la 2
            else:
                self.__fechasig.AsignarFecha(31,12,9999)
        return 
    
    """ Operaciones de consulta de datos Get """
    
    def GetId(self)->str:
        """
        Consulta el identificador de la persona
        Returns
        -------
        str
            identificador de la persona.
        """
        return self.__id

    def GetNombre(self)->str:
        """
        Consulta el nombre de la persona
        Returns
        -------
        str
            nombre de la persona.
        """
        return self.__nombre
    
    def GetVacuna(self)->str:
        """
        Consulta la vacuna suministrada a la persona
        Returns
        -------
        str
            vacuna
        """
        return self.__vacuna
    
    def GetFecha_1(self)->Fecha:
        """
        Consulta la fecha de la dosis 1
        Returns
        -------
        Fecha
            Fecha de la dosis 1.
        """
        return self.__fecha1

    def GetFecha_2(self)->Fecha:
        """
        Consulta la fecha de la dosis 2
        Returns
        -------
        Fecha
            Fecha de la dosis 2.
        """
        return self.__fecha2

    def GetFecha_3(self)->Fecha:
        """
        Consulta la fecha de la dosis 3
        Returns
        -------
        Fecha
            Fecha de la dosis 3.
        """
        return self.__fecha3

    def GetNumDosis(self)->int:
        """
        Consulta el número de dosis inyectadas a la persona
        Returns
        -------
        int
            Número de dosis.
        """
        return self.__numdosis

    def GetFecha_Sig(self)->Fecha:
        """
        Consulta la fecha de la próxima dosis
        Returns
        -------
        Fecha
            Fecha de la próxima dosis. Si no hay prevista próxima dosis
            devuelve la fecha por defecto (1/1/2000)
        """
        return self.__fechasig

    """ Otras operaciones """

    def __Str2Fecha(s:str) -> Fecha:
        """
        Convertir un str en formato: año/mes/dia en un objeto Fecha
        Args:
            s str
        Returns
        -------
        Fecha
        """
        l = s.split("/")
        a = int(l[0])
        m = int(l[1])
        d = int(l[2])
        f = Fecha()
        f.AsignarFecha(d,m,a)
        return f

    def __str__(self)->str:
        """
        Convertir en string la informacion de una persona vacunada.
        Returns
        -------
        str
            string con la informacion de la persona.
        """
        def Convertir(f:Fecha)->str:
            """Función auxiliar para generar la cadena equivalente a una fecha"""
            ref = Fecha()
            if f == ref: #Si es el valor por defecto es que no hay fecha real
                s = "-"
            else:
                s = str(f)
            return s
            
        sep = " "*4
        s =  sep + "- ID: " + self.__id + "\n"
        s += sep + "- Nombre: " + self.__nombre + "\n"
        s += sep + "- Vacuna: " + self.__vacuna + "\n"
        s += sep + "- Dosis recibidas: " + str(self.__numdosis) + "\n"
        s1 = Convertir(self.__fecha1)
        s2 = Convertir(self.__fecha2)
        s3 = Convertir(self.__fecha3)
        s += sep + "- Fecha dosis 1: " + s1 + "\n"
        s += sep + "- Fecha dosis 2: " + s2 + "\n"
        s += sep + "- Fecha dosis 3: " + s3 + "\n"
        s4 = Convertir(self.__fechasig)
        s += sep + "- Fecha proxima dosis: " + s4 + "\n"
        return s
