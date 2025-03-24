'''
Laboratorio 3.

- Definir una nueva carrera de atletismo.
- Registrar todos los atletas incluidos en los archivos siempre que cumplan los requisitos.
- El programa mostrará el número de atletas inscritos y sus datos.
- El programa también debe calcular la distribución por países de los atletas inscritos en la carrera.

Autor: Carlos Martinez
Fecha: 21/03/2025 
'''
from atleta import *
from carrera import *

def LeerFichero(nom:str, c:Carrera) -> (bool, list):
    '''
    Leer archivo de Atletas.
    Args:
        nom = Nombre del archivo
        c = Objeto Carrera que contiene
    Return:
        abierto para lectura correctamente = True/False
    '''
    abierto = False
    try:
        f = open(nom)
    except:
        abierto = False
    else:
        abierto = True

        # Leer cabecera y no hacer nada con ella.
        f.readline()

        # Leer las restantes lineas y convertirlas en personas vacunadas.
        for linea in f:
            linea = linea.rstrip("\n") # Elimina el salto de linea si lo tuviera.
            atleta = list()
            atleta = linea.split(';') # Separa los valores de cada linea por ';' y los guarda en una lista con 4 elementos.
            if len(atleta) >= 4: # Para verificar que se tienen los 4 espacios/atributos del atleta. 
                a = Atleta()
                a.SetValores(atleta[0], atleta[1], atleta[2], atleta[3])
                c.Inscribir(a)
        f.close()
    return abierto

def main():
    print(__doc__)

    # Configuramos las constantes. 
    ESPECIALIDAD = '10000m(H)'
    NOMBRECARRERA = '10000m(H) Semifinales'
    FICHERO = 'atletas_small.csv'
    FICHERO2 = 'atletas_big.csv'

    # Creamos el objeto carrera para registrar atletas.
    c = Carrera()
    c.SetEspecialidad(ESPECIALIDAD)
    c.SetNombre(NOMBRECARRERA)
    
    if LeerFichero(FICHERO2, c):

        paises = Atleta.PAISES # Referenciamos la lista que ya teniamos creada en la clase Atleta.
        total_pais = [0 for i in range(len(paises))] # A cada pais asignamos un total de 0 apariciones; aumentan cada vez que un Atleta sea de ese pais. 

        n_atletas = len(c.GetParticipantes()) 

        print('Número de atletas inscritos =', n_atletas)

        print('Datos de los atletas:')
        for i in c.GetParticipantes():
            pos = paises.index(i.GetPais()) # Obtenemos la posicion del pais dentro de la lista referenciada de paises
            total_pais[pos] += 1            # y sumamos la aparicion de dicho pais en la carrera. 
            print('     ', i)

        print('Distribución por paises:')
        for i in range(len(total_pais)):
            if total_pais[i] != 0:
                    print('     ',paises[i], ':' ,total_pais[i])   

if __name__ == '__main__':
    main()

