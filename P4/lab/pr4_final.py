'''
Práctica 4.
Trabajo hecho por Jorge Ballesteros García y Carlos Santiago Martínez Torres.
Fecha: 03/04/2025
'''

from clase_pila import Pila
from clase_cola import Cola
from class_linea2 import Linea
        
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
        Lista de posición con los paréntesis abiertos (ini) y cerrados (fin)
        La lista quedará vacía si la línea analizada contiene algún error de paréntesis.


    """

    p = Pila()
    error = False
    lista_pos_parentesis = []
    for i in range(len(e)):
        if e[i] == "(":
            p.Apilar(i)

        else:
            if e[i] == ")":
                fin = i
                try:
                    ini = p.Cima()
                    p.Desapilar()
                    lista_pos_parentesis.append((ini, fin))
                except:
                    error = True
    if error:
        lista_pos_parentesis = [] #Hay el error de que la pila queda vacía y quedan muchos paréntesis cerrados.

    if not p.EsVacia():
        lista_pos_parentesis = [] #Hay el error de que quedan paréntesis abiertos en la pila p sin cerrar.

    return lista_pos_parentesis


def LeerFichero(nom:str)->bool:
    try:
        f = open(nom, encoding = 'UTF-8')
    except:
        ok = False
    else:
        ok = True
        c_parentesis = Cola()
        cont_lineas = 1
        for linea in f:
            cont_lineas+=1
            #Analizamos la concordancia de paréntesis.
            lista_pos_parentesis = AnalizarParentesis(linea)

            #Si la lista contiene las posiciones de los paréntesis abiertos y cerrados correctos, creamos un objeto de la clase Linea y 
            #rellenamos sus atributos con el número de linea, la linea de texto y la lista 
            #de tuplas con las posiciones de los paréntesis abiertos y cerrados.
            #Después guardamos en una cola el objeto.

            if lista_pos_parentesis:
                l = Linea(cont_lineas, linea, lista_pos_parentesis)
                c_parentesis.Encolar(l)
        

        from copy import deepcopy
        #Creamos aux que una copia profunda de la cola original y es con la que vamos a trabajar.

        aux = deepcopy(c_parentesis)

        while not aux.EsVacia():
            #Consultamos el primer elemento de la cola aux
            obj_linea = aux.Primero()
            #Ahora desencolamos dicho elemento
            aux.Desencolar()
            print("Línea: ", obj_linea.GetNumero())
            
            #Creamos la lista de tuplas con las tuplas obtenidas con GetPosParentesis()
            l_tuplas = obj_linea.GetPosParentesis()

            #Para cada tupla de la lista, obtenemos el texto de la línea (con los paréntesis incluidos)
            #y nos quedamos con el contenido que está entre los paréntesis de la línea.
            for tupla in l_tuplas:
                texto = obj_linea.GetTexto()
                print("     Contenido = ", texto[tupla[0]+1: tupla[1]])
        return ok

def main():
    print(__doc__)
    NOM_F = "test.py"
    valido = LeerFichero(NOM_F)
    if valido:
        print(valido)
    else:
        print("Error abriendo fichero.")

if __name__ == '__main__':
    main()