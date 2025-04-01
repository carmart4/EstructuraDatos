from clase_pila import Pila
        
def AnalizarParentesis (e:str)->list:
    """
    Funcion que analiza la concordancia de paréntesis en una cadena

    Parameters
    ----------
    e : str
        Expresion con parentesis.

    Returns
    -------
    list
        Lista de errores.

    """
    par = False
    p = Pila()
    lista_errores = []
    for i in range(len(e)):
        if e[i] == "(":
            p.Apilar(i)
            par = True
        else:
            if e[i] == ")":
                par = True
                try:
                    p.Desapilar()
                except:
                    lista_errores.append("')' no abierto en "+str(i))
            
    if not p.EsVacia():
        while not p.EsVacia():
            lista_errores.append("'(' no cerrado en "+str(p.Cima()))
            p.Desapilar()

    return lista_errores, par

def ValidarFicheroPython (n: str, l:list, e:list, parentesis:list) -> bool:
    '''
    Función que lee las lineas de un fichero que contiene código Python 
    y valida la concordancia de paréntesis de cada una de estas líneas.
    ---
    Args:
        n = nombre del fichero
        l = lista con el numero de linea que contiene el error
        e = lista de errores que hay en la linea
    Return:
        ok = indica si se abrio o no el fichero
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
            errores, p = AnalizarParentesis(linea)
            if len(errores) > 0:
                e.extend(AnalizarParentesis(linea))
                l.append(nlinea)
            if p:
                parentesis.append(nlinea)
                
        f.close()

    return ok

def main():

    fname = 'test.py'
    lineas = list()
    errores = list()
    parentesis = list() # de enteros

    if ValidarFicheroPython(fname, lineas, errores, parentesis):
        print(len(lineas))
        print(len(errores))
        print(len(parentesis))
        
        #for i in range(len(errores)):
        #    print('Línea ', lineas[i])
            #print(errores[i])

if __name__ == "__main__":
    main()    