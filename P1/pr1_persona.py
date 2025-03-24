# -*- coding: utf-8 -*-
"""Módulo auxiliar para Práctica 1 (2025).
Definición de un registro de Personas Vacunadas contra Covid19.
Incluye una función auxiliar para mostrar la información por pantalla.

Este archivo no requiere ninguna modificación.

"""

class PersonaVacunada:
    """Registro para representar datos de vacunacion de 1 persona.
    """
    def __init__(self):
        self.id = str() #Codigo de identificacion
        self.nombre = str() #Nombre de la persona
        self.vacuna = str() #Vacuna suministrada
        self.fecha1 = str() #Fecha dosis 1
        self.fecha2 = str() #Fecha dosis 2
        self.fecha3 = str() #Fecha dosis 3
    
def MostrarPersona(p:PersonaVacunada):
    """Mostrar en pantalla la informacion de una persona vacunada
        Args:
            p = persona de la que se muestra la informacion
    """
    sep = " "*4
    print("*** Datos de la Persona: ")
    print(sep + "- Id: " + p.id)
    print(sep + "- Nombre: " + p.nombre)
    print(sep + "- Vacuna: " + p.vacuna)
    print(sep + "- Fecha dosis 1: " + p.fecha1)
    print(sep + "- Fecha dosis 2: " + p.fecha2)
    print(sep + "- Fecha dosis 3: " + p.fecha3)
    return
