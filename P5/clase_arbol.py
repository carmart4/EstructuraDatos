# -*- coding: utf-8 -*-
"""
Práctica 5: Clase árbol binario genérico. 

@date:02/04/2025
"""
class ArbolBinario:
    class __Nodo:
        """
        Clase Nodo, que representa los componentes del árbol binario
        Es una clase privada/interna de la clase ArbolBinario 
        """
                
        def __init__ (self, info, hizq=None, hder=None):
            """
            Crear un nuevo nodo con información, hijo izq. e hijo der.

            Parameters
            ----------
            info : Depende de la aplicación
                Información del nodo
            hizq : __Nodo, opcional
                Hijo izquierdo del nodo. The default is None.
            hder : __Nodo, opcional
                Hijo derecho del nodo. The default is None.

            Returns
            -------
            None.

            """
            self.info = info
            self.hizq = hizq
            self.hder = hder
        
        def GetInfo (self):
            """
            Obtener la información del nodo 

            Returns
            -------
            Desconicido, dependende de la aplicación
                Información del nodo.

            """
            return self.info
            
        def GetIzq (self): #-> __Nodo
            """
            Obtener el hijo izquierdo 

            Returns
            -------
            __Nodo
                Hijo izquierdo del nodo.

            """
            return self.hizq
        
        def GetDer (self): #-> __Nodo
            """
            Obtener el hijo derecho 

            Returns
            -------
            __Nodo
                Hijo derecho del nodo.

            """
            return self.hder
            
    """ Operaciones de la clase ArbolBinario """
    def __init__ (self, info = None, subizq = None, subder = None):
        """
        Constructor del árbol

        Parameters
        ----------
        info : Desconocido, depende de la aplicación, opcional
            Información de la raíz. The default is None.
        subizq : ArbolBinario, optional
            Subárbol izquierdo. The default is None.
        subder : ArbolBinario, optional
            Subárbol derecho. The default is None.

        Returns
        -------
        None.

        """
        
        # Creación del nodo raiz del árbol
        if info == None: #no información, árbol vacío
            self.__raiz = None
        else:
            if subizq == None: #subizq vacío
                subizq = ArbolBinario()
            if subder == None: #subder vacío
                subder = ArbolBinario()
            self.__raiz = ArbolBinario.__Nodo(info,subizq.__raiz,subder.__raiz)
    
    def EsVacio(self)->bool:
        """
        Determinar si árbol está vacío o no

        Returns
        -------
        bool
            True = árbol vacío, False = no vacío.

        """
        return self.__raiz == None
    
    def Raiz(self):
        """
        Obtener la información en la raíz del Árbol Binario

        Raises
        ------
        RuntimeError
            Si el árbol está vacío.

        Returns
        -------
        Desconocido, dependen de la aplicación
            Información de la raíz.

        """
        if self.EsVacio():
            raise RuntimeError ("Error: Intento de acceso hijo derecho de un árbol vacío.")
        else:
            return self.__raiz.GetInfo()

    def SubarbIzq(self): #-> ArbolBinario
        """
        Obtener el Árbol Binario a la izquierda del actual

        Raises
        ------
        RuntimeError
            Si el árbol está vacío.

        Returns
        -------
        a : ArbolBinario
            Subárbol izquierdo.

        """        
        if self.EsVacio():
            raise RuntimeError ("Error: Intento de acceso hijo izquierdo de un árbol vacío.")
        else:
            a = ArbolBinario()
            a.__raiz = self.__raiz.GetIzq()
            return a

    def SubarbDer(self): #-> ArbolBinario
        """
        Obtener el Árbol Binario a la derecha del actual

        Raises
        ------
        RuntimeError
            Si el árbol está vacío.

        Returns
        -------
        a : ArbolBinario
            Subárbol derecho.

        """
        if self.EsVacio():
            raise RuntimeError ("Error: Intento de acceso hijo derecho de un árbol vacío.")
        else:
            a = ArbolBinario()
            a.__raiz = self.__raiz.GetDer()
            return a
