'''
Previo de laboratorio 4.

Analiza la corrección del uso de paréntesis “(“ y “)” en una cadena de texto.

Autor: Carlos Martinez
Fecha: 1/04/2025

'''
from clase_pila import Pila
from clase_cola import Cola
from clase_linea import Linea
        
def AnalizarParentesis (e:str)->list:
    """
    Funcion que analiza la concordancia de paréntesis en una cadena.

    Parameters
    ----------
    e : str
        Expresion con parentesis.

    Returns
    -------
    list
        Lista de errores.

    """
    parentesis = False
    p = Pila()
    lista_errores = []
    for i in range(len(e)):
        if e[i] == "(":
            p.Apilar(i)
            parentesis = True
        else:
            if e[i] == ")":
                parentesis = True
                try:
                    p.Desapilar()
                except:
                    lista_errores.append("')' no abierto en "+str(i))
            
    if not p.EsVacia():
        while not p.EsVacia():
            lista_errores.append("'(' no cerrado en "+str(p.Cima()))
            p.Desapilar()

    return lista_errores, parentesis

def ValidarFicheroPython (n: str, listalineas:list, c:Cola) -> bool:
    '''
    Función que lee las lineas de un fichero que contiene código Python 
    y valida la concordancia de paréntesis de cada una de estas líneas.

    Args
    ------
    n = nombre del fichero.
    listalineas = lista con objetos de la clase Linea.
    c = cola con las lineas que contienen parentesis. 
    
    Return
    ------
    ok = indica si se abrio o no el fichero.
    '''
    ok = False
    try:
        f = open(n)

    except:
        raise TypeError('No se pudo abrir el fichero')

    else:
        ok = True
        nlinea = 1
        for linea in f:
            nlinea +=1
            linea = linea.rstrip("\n")
            errores, parentesis = AnalizarParentesis(linea)
            if parentesis == True:
                    c.Encolar(nlinea)
            if len(errores) > 0:
                l = Linea()
                l.AddNumeroLinea(nlinea)
                l.AddErroresLinea(errores)
                listalineas.append(l)
        f.close()
    return ok

def Resultados(c:Cola, l:list):
    '''
    Funcion que imprime los resultados sobre 
    las lineas que contienen errores.

    Arg
    ---
    c = cola con las lineas con paréntesis
    l = lista de objetos de la clase Linea
    '''
    print('Resultados')
    print('==========')
    print('*Lineas con paréntesis: ')
    print(c)
    print()
    print('*Lineas con errores: ')
    for e in l:
        print(e)
    print()
    return

def main():

    print(__doc__)

    # Nombre del fichero a evaluar
    fname = 'test.py' 

    listalineas = list()
    ColaParentesis = Cola()

    if ValidarFicheroPython(fname, listalineas, ColaParentesis):
        Resultados(ColaParentesis, listalineas)

if __name__ == "__main__":
    main()    