# -*- coding: utf-8 -*- 
"""Práctica 1 (2025). Version 0
Definición y manejo básico de un registro de Personas Vacunadas

"""
from pr1_persona import PersonaVacunada

def ConvertirLinea(s:str)->PersonaVacunada:
    """Convertir una linea de texto csv en un registro Persona
    
        Args:
            s = linea a procesar
        Return:
            PersonaVacunada con los datos contenidos en s
    """
    s = s.rstrip("\n") #elimina \n si lo tuviera
    l = list()
    l = s.split(";")
    p = PersonaVacunada()
    if len(l) >= 6: #para evitar errores de formato
        p.id = l[0] #Codigo de identificacion
        p.nombre = l[1] #Nombre de la persona
        p.vacuna = l[2] #Vacuna suministrada
        p.fecha1 = l[3] #Fecha dosis 1
        p.fecha2 = l[4] #Fecha dosis 2
        p.fecha3 = l[5] #Fecha dosis 3
    return p
    
def LeerFichero(nom: str) -> (bool, list):
    """ Leer archivo de personas vacunadas.
        Args:
            nom = Nombre del archivo
        Return:
            abierto para lectura correctamente = True/False
            lista de personas leidas, vacía si no abierto
    """
    abierto = bool()
    lista = []
    try:
        f = open(nom)
    except:
        abierto = False
    else:
        abierto = True
        #Leer cabecera y no hacer nada con ella
        f.readline()
        #Leer las restantes lineas y convertirlas en personas vacunadas
        for linea in f:
            p = ConvertirLinea(linea)
            lista.append(p)
        f.close()
    return abierto, lista

def main():
    """ Tarea 1: Implementar esta función principal para que:
    1) Se lean datos de personas desde una archivo csv,
    2) se almacenen en una lista y
    3) se muestren por pantalla
    """    
    
if __name__ == '__main__':
    main()