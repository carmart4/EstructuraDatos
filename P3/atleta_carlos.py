'''
Previo laboratorio. 

Definicion de una clase llamada Atleta, que representa a un 
atleta que puede participar en competiciones internacionales. 

Autor: Carlos Martinez
Fecha: 10/03/2025

'''
class Atleta:
    '''
    Especificacion del tipo persona Vacunada: 

    • Identificador: Un identificador alfanumérico que identifica al atleta.
    • Nombre: Nombre y apellidos del atleta (un único valor).
    • País: País al que se adscribe el atleta.
    • Especialidad: Especialidad en la que participa el atleta (solo una).
    
    '''
    # Definimos 'constantes'

    ESPEC = ["100m(H)", "100m(M)", "200m(H)", "200m(M)", "400m(H)", "400m(M)", "800m(H)", "800m(M)", 
                          "1500m(H)", "1500m(M)", "5000m(H)", "5000m(M)", "10000m(H)", "10000m(M)"]
    
    PAISES = ["ALE", "ARG", "AUS", "BEL", "BOL", "BRA", "CHI", "DIN", "ESP", 
            "FRA", "GBR", "GRE", "HOL", "HON", "ITA", "MEX", "POR", "SUE", "SUI", "URU"]

    def __init__(self, id='<Sin asignar>', nom='<Sin asignar>', pais='<Sin asignar>', esp='<Sin asignar>'):
        ''' 
        Construye un nuevo objeto con valores por defecto para sus atributos. 
        Alfanuméricos tendrán el valor '<Sin asignar>' y numéricos 0. 
        '''
        self.__id = id
        self.__nombre = nom
        self.__pais = pais
        self.__especialidad = esp
        return
    

    def __ValidarPais(p:str) -> bool:
        '''
        Valida que el país a modificar sea correcto. 
        Arg: 
            p = país que ingresa el usuario 
        return: 
            valido = indica si el país ingresado es correcto o no
        '''
        valido = False
        
        if p in Atleta.PAISES:
            valido = True

        return valido

    def __ValidarEspecialidad(e:str) -> bool:
        '''
        Valida que la especialidad a modificar sea correcta. 
        Arg: 
            e = especialidad que ingresa el usuario 
        return: 
            valido = indica si la especialidad ingresada es correcta o no
        '''
        valido = False
        
        if e in Atleta.ESPEC:
            valido = True

        return valido  
    
    def ValidarSet(self, v:bool):
        ''' 
        Esta funcion permite saber al usuario si las funciones SetPais y SetEspecialidad
        fueron ejecutadas correctamente. Es decir, si se hizo el cambio o no.
        Arg: 
            v= valor booleano de las funciones
        '''
        if v:
            print('Se ha hecho el cambio correctamente.')
        else:
            print('No se ha hecho el cambio correctamente. Intente con otro valor.')
        return
    
    def ValidarSetCompleto(self, v:bool, p:str, e:str):
        ''' 
        Esta funcion permite saber si la funcion SetValores fue ejecutada correctamente. 
        Si no, permite al usuario saber cual fue el error entre pais y especialidad. 
        Arg: 
            v= valor booleano de las funciones
        '''
        if v:
            print('Se ha hecho el cambio correctamente.')
        else:
            if not Atleta.__ValidarPais(p):
                print(f"Error: '{p}' no es un país valido.")

            elif not Atleta.__ValidarEspecialidad(e):
                print(f"Error: '{e}' no es una especialidad valida.")
        return

    ''' 
    Todas las operaciones Set deben ser TRUE/FALSE
    para saber si se ha modificado correctamente o no 
    '''

    def SetValores(self, id:str, nom:str, pais:str, esp:str) -> bool:
        ''' 
        Esta operación permite establecer los valores de todos los atributos del objeto. 
        No deben modificar ningún dato del objeto si cualquiera de los valores de entrada es incorrecto.

        Arg:    id, nom, pais, esp: Son los datos que ingresa el usuario.
        return: valido: valor booleano que indica si los datos ingresados son correctos o nos.
        '''
        valido = False
        if Atleta.__ValidarPais(pais) and Atleta.__ValidarEspecialidad(esp):
            valido = True
            self.__id = id
            self.__nombre = nom
            self.__pais = pais
            self.__especialidad = esp

        #self.ValidarSetCompleto(valido, pais, esp)
        return valido
    
    def SetId(self, i:str):
        ''' Permite modificar exclusivamente el identificador del atleta. '''
        self.__id = i
        return

    def SetNombre(self, n:str):
        ''' Permite modificar exclusivamente el nombre del atleta. '''
        self.__nombre = n
        return
    
    def SetPais(self, p:str) -> bool:
        ''' 
        Permite modificar exclusivamente el país del atleta. 
        No deben modificar ningún dato del objeto si cualquiera de los valores de entrada es incorrecto.

        Arg:    p: dato del país que ingresa el usuario.
        return: valido: valor booleano que indica si el dato ingresado es correcto o no.
        '''
        valido = False
        if Atleta.__ValidarPais(p):
            valido = True
            self.__pais = p

        #self.ValidarSet(valido)

        return valido
    
    def SetEspecialidad(self, e:str) -> bool:
        ''' 
        Permite modificar exclusivamente la especialidad en la que compite el atleta. 
        No deben modificar ningún dato del objeto si cualquiera de los valores de entrada es incorrecto.

        Arg:    e: dato de la especialidad que ingresa el usuario.
        return: valido: valor booleano que indica si el dato ingresado es correcto o no.
        '''
        valido = False
        if Atleta.__ValidarEspecialidad(e):
            valido = True
            self.__especialidad = e
        
        #self.ValidarSet(valido)

        return valido
    
    def GetId(self) -> str:
        ''' Permite conocer el identificador del atleta. '''
        return self.__id
    
    def GetNombre(self) -> str: 
        ''' Permite conocer el nombre del atleta. '''
        return self.__nombre
    
    def GetPais(self) -> str: 
        ''' Permite conocer el país del atleta. '''
        return self.__pais
    
    def GetEspecialidad(self) -> str: 
        ''' Permite conocer la especialidad del atleta. '''
        return self.__especialidad
    
    def __str__(self):
        a = self.GetId() + ';' + self.GetNombre() + ';' + self.GetPais() + ';' + self.GetEspecialidad()
        return a