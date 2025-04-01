'''
Previo de laboratorio 4.

Analiza la corrección del uso de paréntesis “(“ y “)” en una cadena de texto.

Autor: Carlos Martinez
Fecha: 1/04/2025

'''

from clase_pila import Pila
from clase_cola import Cola
        
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

def ValidarFicheroPython (n: str, l:list, e:list, c:Cola) -> bool:
    '''
    Función que lee las lineas de un fichero que contiene código Python 
    y valida la concordancia de paréntesis de cada una de estas líneas.

    Args
    ------
    n = nombre del fichero.
    l = lista con los numeros de lineas que contienen un error.
    e = lista de errores que hay en la linea.
    p = cola con las lineas que contienen parentesis. 
    
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
                e.extend(errores)
                l.append(nlinea)
        f.close()

    return ok

def main():

    print(__doc__)

    fname = 'test.py' # Nombre del fichero
    lineas = list() # Numeros de las lineas que contienen errores
    errores = list() # Lista con los errores de las lineas
    c = Cola() # Numeros de todas las lineas que tienen parentesis

    if ValidarFicheroPython(fname, lineas, errores, c):
        
        print('Listado de errores fichero: ', fname)
        print('---')
        for i in range(len(errores)):
            print('Línea ', lineas[i])
            print(errores[i])
        print('---')    
        print('\nLíneas con paréntesis: ')
        print('---')
        print(c)
        print('---\n')

if __name__ == "__main__":
    main()    