'''
Practica de laboratorio 2.

Algoritmos de ordenación. 

En esta práctica vamos a abordar el cálculo empírico de costes de diversos 
algoritmos de ordenación. En concreto, se pretende obtener resultados 
experimentales del coste real en pasos de la implementación en Python 
de los dos algoritmos de ordenación analizados en las clases de teoría:

1. Ordenación por selección.
2. Quicksort.

Autor: Carlos Martinez
Fecha: 25/02/2025
'''
from pr2_persona import *
from pr2_algoritmos import *

def LeerFichero(nom: str) -> (bool, list):
    """ Leer archivo de personas vacunadas.
        Args:
            nom = Nombre del archivo
        Return:
            abierto para lectura correctamente = True/False
            lista de personas leidas, vacía si no abierto
    """
    abierto = False
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
            lista.append(linea)
        f.close()
    return abierto, lista

def ConvertirPersonas(l: list) -> list:
    '''
    Leer la lista l que contiene las personas en formato texto csv
    y devolverlas en objeto PersonaVacunada
    Args:
        l = Contiene la lista de personas en texto csv

    Returns:
        lv = Contiene la lista de personas como objetos
    '''
    lv = list()
    for p in l:
        persona = PersonaVacunada()
        persona.SetDatos(p)
        lv.append(persona)
    return lv

def EscribirFichero(fecha_citas: list,
                   f_salida: str,
                   copia1: list,
                   Fecha_inicio: Fecha) -> (bool, list, int):
    '''
    Escribir un fichero con el formato fecha;id;nombre;num_dosis
    de las personas que se vacunarán en los proximos días.
    ---
    Args:
        fecha_citas = lista de los días para agendar vacunacion
        f_salida = nombre del fichero de salida
        copia1 = lista de objeto Personas 
        Fecha_inicio = fecha desde la que se agendará
    Return:
        Creado para escritura correctamente = True/False
        n_citas_dias = lista con el total de citas por día
        total_citas = total de citas agendadas en los n dias 
    '''
    creado = False

    # Lista para guardar las citas agendadas por día
    n_citas_dias = [0 for i in range(len(fecha_citas))]

    # Total de citas agendadas para los n dias 
    total_citas = 0 

    try:
        f_sal = open(f_salida, 'w', encoding='utf-8')
    except:
        creado = False
    else:
        creado = True
        f_sal.write('fecha;id:nombre;nuevadosis\n')
        for f in fecha_citas:
            total_fecha = 0 # Total de citas agendadas por dia
            for persona in copia1:
                fecha_siguiente = persona.GetFecha_Sig()

                if f == Fecha_inicio: # Filtro para las fechas menores o iguales a 1-1-2022
                    if fecha_siguiente < Fecha_inicio or fecha_siguiente == Fecha_inicio:
                        total_fecha += 1
                        total_citas += 1
                        cita = str(f)+';'+str(persona.GetId())+';'+str(persona.GetNombre())+';'+str(persona.GetNumDosis()+1)+'\n'               
                        f_sal.write(cita)  
                else:
                    if fecha_siguiente == f:
                        total_fecha += 1
                        total_citas += 1
                        cita = str(f)+';'+str(persona.GetId())+';'+str(persona.GetNombre())+';'+str(persona.GetNumDosis()+1)+'\n'
                        f_sal.write(cita)  

            n_citas_dias[fecha_citas.index(f)] = total_fecha
              
        f_sal.close()    
    return creado, n_citas_dias, total_citas

def main():

    #f = 'vacunaciones_small.csv'
    #abierto, datos = LeerFichero(f)
    f2 = 'vacunaciones_big.csv'
    abierto2, datos2 = LeerFichero(f2)

    f_salida = 'citas.csv'
    
    # Ejercicio 1

    if abierto2:
        listaVacunados = ConvertirPersonas(datos2)

        # Generar dos copias de la lista utilizando como criterio
        # la fecha de la siguiente dosis.

        copia1 = listaVacunados.copy()
        copia2 = listaVacunados.copy()

        p1 = OrdSeleccion(copia1)
        p2 = OrdQuicksort(copia2)
        ratio = p1/p2

        # Mostrar el numero de pasos realizados por el algoritmo y la relacion entre ellos. 
        print('---')
        print('Selección: ', p1)
        print('Quicksort: ', p2)
        print('Ratio: ', round(ratio, 2))
        print('---')

        # Establecemos la fecha de inicio de las vacunaciones. 
        Fecha_inicio = Fecha()
        Fecha_inicio.AsignarFecha(1, 1, 2022)

        # Asignamos la cantidad de días para agendar
        NumDias = 7

        # Generar las citas de vacunacion para los n dias 
        fecha_citas = []
        for i in range(NumDias):
            f = Fecha_inicio
            f += i
            fecha_citas.append(f)

        creado, n_citas_dias, total_citas = EscribirFichero(fecha_citas, f_salida, copia2, Fecha_inicio)

        if creado:
            print('Fichero creado.')
            print('Total de citas: ', total_citas)
            for i in range(len(fecha_citas)):
                print('  ', fecha_citas[i], n_citas_dias[i])

        else:
            print('Error creando el fichero.')

if __name__ == '__main__':
    main()