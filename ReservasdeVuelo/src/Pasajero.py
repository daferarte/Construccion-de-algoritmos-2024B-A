__author__ = "Daniel Fernando Arteaga Fajardo"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "daniel.arteagafajar@campusucc.edu.co"

class Pasajero:
    
    
    __method__='Constructor'
    __params__='Ninguno'
    __returns__='Ninguno'
    __descriptions__='Metodo constructor de la clase Pasajero'
    def __init__(self, cedula, nombre):
        self.__cedula = cedula
        self.__nombre = nombre
        
    # metodos 
    
    __method__='DarCedula'
    __params__='Ninguno'
    __returns__='Cedula'
    __descriptions__='Este metodo retorna la cedula del pasajero'
    def DarCedula(self):
        return self.__cedula
    
    __method__='ModificarCedula'
    __params__='Cedula'
    __returns__='Ninguno'
    __descriptions__='Este metodo modifica la cedula del pasajero'
    def ModificarCedula(self, cedula):
        self.__cedula = cedula
        
    __method__='DarNombre'
    __params__='Ninguno'
    __returns__='Nombre'
    __descriptions__='Este metodo retorna el Nombre del pasajero'
    def DarNombre(self):
        return self.__nombre
    
    __method__='ModificarNombre'
    __params__='Nombre'
    __returns__='Ninguno'
    __descriptions__='Este metodo modifica el Nombre del pasajero'
    def ModificarNombre(self, nombre):
        self.__nombre = nombre
        
    
    
    