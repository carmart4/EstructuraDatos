# -*- coding: utf-8 -*- 
"""
Clase Fecha
@date: 17/02/2025
"""
class Fecha:
    """
    Especificación del tipo Fecha
    Resumen de operaciones públicas:
        - Constructor: fecha por defecto 01/01/1970
        - AsignarFecha(self, d:int, m:int, a:int): Asignar un valor a una fecha.
        - IncrementarFecha(self): Incrementar en un 1 dia la fecha
        - DecrementarFecha(self): Decrementar en un 1 dia la fecha
        - MenorFecha(self, g:'Fecha')->bool: Comprobar si la fecha es menor que g.
        - VisualizarFecha(self): Mostrar la fecha por pantalla.
        - Operador + : Sumar a la fecha x días. No modifica la fecha self
        - Operador - : Restar a la fecha x días. No modifica la fecha self
        - Operador < : Comprobar si la fecha self es menor que g. Igual que MenorFecha()
        - Operador == : Comprobar si la fecha self es igual a la fecha g.
        - Operador != : Comprobar si la fecha self es diferente a la fecha g.
        - str(): Transformacion en string de la fecha.
    """
    
    def __init__(self):
        """Constructor.
        Establece como fecha por defecto 01/01/1970"""        
        self.__dia = 1
        self.__mes = 1
        self.__anyo = 1970
        return
   
    def AsignarFecha(self, d:int, m:int, a:int):
        """Asignar un valor a una fecha.
        Los atributos no se modifican si la fecha no es valida
        Parameters
        ----------
            d : int = dia
            m : int = mes
            a : int = año
        Returns
        -------
            None
        """
        if Fecha.__FechaValida(d,m,a):
            self.__dia = d
            self.__mes = m
            self.__anyo = a
        return
        
    def IncrementarFecha(self):
        """Incrementar en un 1 dia la fecha. Día siguiente."""
        if Fecha.__FechaValida(self.__dia+1,self.__mes,self.__anyo):
            self.__dia += 1
        else:
            if Fecha.__FechaValida(1,self.__mes+1,self.__anyo):
                self.__dia = 1
                self.__mes += 1
            else:
                self.__dia = 1
                self.__mes = 1
                self.__anyo += 1
        return
        
    def DecrementarFecha(self):
        """Decrementar en un 1 dia la fecha. Día anterior."""
        if Fecha.__FechaValida(self.__dia-1,self.__mes,self.__anyo):
            self.__dia -= 1
        else:
            dias_mes_ant = Fecha.__DiasMes(self.__mes-1,self.__anyo)
            if Fecha.__FechaValida(dias_mes_ant,self.__mes-1,self.__anyo):
                self.__dia = dias_mes_ant
                self.__mes -= 1
            else:
                self.__dia = 31
                self.__mes = 12
                self.__anyo -= 1
        return
       
    def MenorFecha(self, g: 'Fecha')->bool:
        """Comprobar si la fecha self es menor que g.
        Parameters
        ----------
            g: Fecha de referencia
        Returns
        -------
            True, si self es anterior a g
            False, si self no es anterior a g
        """
        menor = False
        if self.__anyo < g.__anyo:
            menor = True
        elif self.__anyo == g.__anyo:
            if self.__mes < g.__mes:
                menor = True
            elif self.__mes == g.__mes:
                if self.__dia < g.__dia:
                    menor = True
        return menor

    def VisualizarFecha(self):
        """Mostrar la fecha por pantalla.
        Formato: día/mes/año"""
        s = str(self.__dia) + "/" 
        s += str(self.__mes) + "/" 
        s += str(self.__anyo)
        print(s)
        return
    
    """ Operadores sobrecargados """
    
    def __add__(self, x:int)->'Fecha':
        """Operador +
        Sumar a la fecha x días. No modifica la fecha self
        Parameters
        ----------
            x: int días incrementados
        Returns
        -------
            Fecha resultante
        """
        res = Fecha()
        res.AsignarFecha(self.__dia,self.__mes,self.__anyo)
        if x > 0:
            for i in range(x):
                res.IncrementarFecha()
        return res

    def __sub__(self, x:int)->'Fecha':
        """Operador -
        Restar a la fecha x días. No modifica la fecha self
        Parameters
        ----------
            x: int días decrementados
        Returns
        -------
            Fecha resultante
        """
        res = Fecha()
        res.AsignarFecha(self.__dia,self.__mes,self.__anyo)
        if x > 0:
            for i in range(x):
                res.DecrementarFecha()
        return res

    def __lt__(self, g)->bool:
        """Operador <
        Comprobar si la fecha self es menor que g.
        Parameters
        ----------
            g: Fecha de referencia
        Returns
        -------
            True, si self es anterior a g
            False, si self no es anterior a g
        """
        return self.MenorFecha(g)

    def __eq__(self, g)->bool:
        """Operador ==
        Comprobar si la fecha self es igual a la fecha g.
        Parameters
        ----------
            g: Fecha de referencia
        Returns
        -------
            True, si self == g
            False, si self != g
        """
        igual = False
        if self.__dia == g.__dia and self.__mes == g.__mes and self.__anyo == g.__anyo:
            igual = True
        return igual

    def __ne__(self, g)->bool:
        """Operador !=
        Comprobar si la fecha self es diferente a la fecha g.
        Parameters
        ----------
            g: Fecha de referencia
        Returns
        -------
            True, si self != g
            False, si self == g
        """
        return not (self == g)

    def __str__(self)->str:
        """str()
        Transformacion en string de la fecha.
        Returns
        -------
            str en formato: día/mes/año        
        """
        s = str(self.__dia) + "/" 
        s += str(self.__mes) + "/" 
        s += str(self.__anyo)
        return s

    """ Aquí empiezan las fuciones auxiliares privadas """
    
    def __DiasMes(m:int, a:int)->int:
        """Devuelve el número de días del mes m en el año a.
        Parameters
        ----------
            m: int, mes
            a: int, año
        Returns
        -------
            int = número de días
        """
        meses31 = [1,3,5,7,8,10,12] #meses de 31 días
        meses30 = [4,6,9,11] #meses de 30 días
        dias = 0
        if m in meses31:
            dias = 31
        elif m in meses30:
            dias = 30
        elif m == 2: #febrero
            if Fecha.__Bisiesto(a):
                dias = 29
            else:
                dias = 28
        return dias
    
    def __Bisiesto(a:int)->int:
        """Indica si el año a es bisiesto.
        Parameters
        ----------
            a: int, año
        Returns
        -------
            True si a es bisiesto, False si no lo es
        """
        b = bool()

        if ( a % 400 ) == 0:
            b = True
        elif ( a % 100 ) == 0:
            b = False
        elif ( a % 4 ) == 0:
            b = True
        else:
            b = False
        return b
    
    def __FechaValida(d:int, m:int, a:int)->bool:
        """Indica la terna (d,m,a) representa una fecha válida. 
        Parameters
        ----------
            d: int
            m: int
            a: int
        Returns
        -------
            True si d-m-a es una fecha válida, False si no lo es
        """
        valida = bool()
        #todos los valores de a son validos
        if m >= 1 and m <= 12:
            if d >= 1 and d <= Fecha.__DiasMes(m,a):
                valida = True
            else:
                valida = False
        else:
            valida = False
        return valida
