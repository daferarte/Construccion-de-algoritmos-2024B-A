__author__ = "Daniel Fernando Arteaga Fajardo"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "daniel.arteagafajar@campusucc.edu.co"

from enum import Enum
from Pasajero import Pasajero

class Silla:
    
    class Clase(Enum):
        EJECUTIVA = 1
        ECONOMICA = 2
        
    class Ubicacion(Enum):
        VENTANA = 1
        PASILLO = 2
        CENTRO = 3
        
        
    __method__='Constructor'
    __params__='Ninguno'
    __returns__='Ninguno'
    __descriptions__='Metodo constructor de la clase Silla'
    def __init__(self, numero, clase:Clase, ubicacion:Ubicacion, pasajero:Pasajero = None):
        self.__numero = numero
        self.__clase = clase
        self.__ubicacion = ubicacion
        self.__pasajero = pasajero
        
    __method__='DarNumero'
    __params__='Ninguno'
    __returns__='numero'
    __descriptions__='Este metodo retorna el numero de la silla'
    def DarNumero(self):
        return self.__numero
    
    __method__='ModificarNumero'
    __params__='numero'
    __returns__='Ninguno'
    __descriptions__='Este metodo modifica el numero de la silla'
    def ModificarNumero(self, numero):
        self.__numero = numero
        
    __method__='DarClase'
    __params__='Ninguno'
    __returns__='Clase'
    __descriptions__='Este metodo retorna la Clase de la silla'
    def DarClase(self):
        return self.__clase
    
    __method__='ModificarClase'
    __params__='Clase'
    __returns__='Ninguno'
    __descriptions__='Este metodo modifica la Clase de la silla'
    def ModificarClase(self, clase):
        self.__clase = clase

    __method__='DarUbicacion'
    __params__='Ninguno'
    __returns__='Ubicacion'
    __descriptions__='Este metodo retorna la Ubicacion de la silla'
    def DarUbicacion(self):
        return self.__ubicacion
    
    __method__='ModificarUbicacion'
    __params__='Ubicacion'
    __returns__='Ninguno'
    __descriptions__='Este metodo modifica la Ubicacion de la silla'
    def ModificarUbicacion(self, ubicacion):
        self.__ubicacion = ubicacion
        
    __method__='DarClase'
    __params__='Ninguno'
    __returns__='Clase'
    __descriptions__='Este metodo retorna la Clase de la silla'
    def DarClase(self):
        return self.__clase
    
    __method__='AsignarPasajero'
    __params__='pasajero'
    __returns__='Ninguno'
    __descriptions__='Este metodo Asigna pasajeros a la silla'
    def AsignarPasajero(self, pasajero:Pasajero):
        self.__pasajero = pasajero
    
    __method__='DesasignarSilla'
    __params__='Ninguno'
    __returns__='Ninguno'
    __descriptions__='Este metodo deja la silla vacia'
    def DesasignarSilla(self):
        self.__pasajero = None
        
    __method__='SillaAsignada'
    __params__='Ninguno'
    __returns__='estado silla true = ocupada false = vacia'
    __descriptions__='Este metodo verifica si la silla esta vacia'
    def SillaAsignada(self):
        return self.__pasajero is not None
    
        
    
    